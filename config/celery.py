import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime
from service_app.emailer import send_yandex_message

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')

app = Celery("config", broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

# заносим таски в очередь

app.conf.beat_schedule = {
    'check_new_tasks': { 
        'task': 'config.celery.check_new_tasks',
        'schedule': crontab()
        },
}


def send_messages_tasks(status: str, 
                        current_datetime: dict, 
                        mailing_datetime: dict, mailing_header: str, 
                        mail_message: str, emails: list):
    """ Функция, созданная непосредственно для отправки писем средствами самой Джанго"""
    from service_app import models as m

    if status == 'ACT' and current_datetime == mailing_datetime:
        send_yandex_message(mailing_header, mail_message, emails)
        
        logs = m.Logs(date=current_datetime, status='Отправлено', response='200')
        logs.save()
        print('I`m still working!') 
    print(f'''
Current
{current_datetime}

Mailing
{mailing_datetime}
''')
    return None


@app.task
def check_new_tasks():
    """
Здесь будем забирать данные по рассылкам из нашей БД, проходиться по ней, 
и на основании полученных результатов будем раскидывать по тем, или иным задачкам все это дело.
То есть формируем все необходимое прямо тут.    
    """
# Импортируем модель здесь, потому что иначе проект упадет.
    from service_app import models as m 
    data = m.Mailing.objects.all()
    pk_list = m.Mailing.objects.values_list('pk', flat=True)
    print(pk_list)

# В цикле проходимся по всем строкам в БД и парсим данные
    current_datetime = datetime.now()
    
    try:
        for current_pk in pk_list:
            print(current_pk)
            current_row = data.get(pk=current_pk)
            print(current_row)

            mailing_header = current_row.mail_header
            mail_message = current_row.mail_message
            mailing_day = current_row.mailing_day
            mailing_time = current_row.mailing_time
            mailing_status = current_row.mailing_status
            mailing_day_of_month = current_row.mailing_day_of_month
            recepients = current_row.recepient.all().values('name', 'surame', 'email')
            emails = []
            for r in recepients:
                emails.append(r['email'])

# Прохоимся по всем записям в БД раз в миуту, сравниваем полученные данные по времени, дням и пр. из данных рассылки
# с текущими. Если получили совпадение - отправляем письмо. Все просто, да? 

            print(f"""

Mailing datetime in cycle
{mailing_time}
{mailing_day}
{mailing_day_of_month}

""")

            if mailing_time != None and mailing_day != None and mailing_day_of_month != None:

                current_datetime_dict = {
                    'hour': current_datetime.hour,
                    'minute': current_datetime.minute,
                    'day_of_month': current_datetime.day,
                    'day_of_week': current_datetime.strftime('%A')[:3].lower()
                }

                mailing_dict = {
                    'hour': mailing_time.hour,
                    'minute': mailing_time.minute,
                    'day_of_month': mailing_day_of_month, 
                    'day_of_week': mailing_day,
                    
                }

            elif mailing_time != None and mailing_day != None and mailing_day_of_month == None:

                current_datetime_dict = {
                    'hour': current_datetime.hour,
                    'minute': current_datetime.minute,
                    'day_of_week': current_datetime.strftime('%A')[:3].lower()
                }

                mailing_dict = {
                    'hour': mailing_time.hour,
                    'minute': mailing_time.minute, 
                    'day_of_week': mailing_day,
                    
                }

            elif mailing_time != None and mailing_day == None and mailing_day_of_month != None:

                current_datetime_dict = {
                    'hour': current_datetime.hour,
                    'minute': current_datetime.minute,
                    'day_of_month': current_datetime.day
                }

                mailing_dict = {
                    'hour': mailing_time.hour,
                    'minute': mailing_time.minute,
                    'day_of_month': mailing_day_of_month
                    
                }
            
            elif mailing_time != None and mailing_day == None and mailing_day_of_month == None:

                current_datetime_dict = {
                    'hour': current_datetime.hour,
                    'minute': current_datetime.minute
                }

                mailing_dict = {
                    'hour': mailing_time.hour,
                    'minute': mailing_time.minute                    
                }

            elif mailing_time == None and mailing_day == None and mailing_day_of_month == None:
                
                current_datetime_dict = True
                mailing_dict = True
            
            else:
                current_datetime_dict = True
                mailing_dict = False

            send_messages_tasks(mailing_status, current_datetime_dict, mailing_dict, mailing_header, mail_message, emails)

    except Exception as error:
        print('ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR')
        print(error)
        logs = m.Logs(date=current_datetime, status='He oтправлено', response='500')
        logs.save()
