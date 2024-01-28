from django import forms as f
from django.contrib.auth import forms
from django.contrib.auth import get_user_model


class UserLoginForm(forms.AuthenticationForm):
    username = f.CharField(
        max_length=50,
        label='E-mail',
        widget=f.TextInput(attrs={
            'class': 'auth-fields'
            }
        )
        )

    password = f.CharField(
        max_length=50,
        label='Пароль',
        widget=f.PasswordInput(attrs={
            'class': 'auth-fields'
            }
        )
        )

    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserRegistrationForm(forms.UserCreationForm):
    email = f.CharField(label='E-mail',
                        widget=f.EmailInput(
                            attrs={
                                'class': 'register-fields'
                            }
                        )
                        )
    password1 = f.CharField(max_length=255,
                            label='Пароль',
                            widget=f.PasswordInput(
                                attrs={
                                    'class': 'register-fields'
                                }
                            )
                            )
    password2 = f.CharField(max_length=255,
                            label='Повтор пароля',
                            widget=f.PasswordInput(
                                attrs={
                                    'class': 'register-fields'
                                }
                            )
                            )
    avatar = f.ImageField(
        label='Аватар',
        widget=f.FileInput(
            attrs={
                'class': 'register-fields'
            }
        ),
        required=False
    )
    birthday = f.DateField(
        label='Дата рождения',
        widget=f.DateInput(
            attrs={
                'class': 'register-fields'
            }
        ),
        required=False
    )
    phone_number = f.CharField(label='Номер телефона',
                               max_length=12,
                               widget=f.TextInput(
                                   attrs={
                                       'class': 'register-fields'
                                   }
                               ),
                               required=False
                               )
    country = f.CharField(label='Страна',
                          max_length=50,
                          widget=f.TextInput(
                              attrs={
                                  'class': 'register-fields'
                              }
                          ),
                          required=False
                          )

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name'
        ]

        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        widgets = {
            'email': f.EmailInput(
                attrs={
                    'class': 'register-fields'
                }
            ),
            'first_name': f.TextInput(
                attrs={
                    'class': 'register-fields'
                }
            ),
            'last_name': f.TextInput(
                attrs={
                    'class': 'register-fields'
                }
            ),
        }
    
    def clean_password(self):
        """Верификация пароля"""
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise f.ValidationError('Пароли не совпадают!')    
        return data['password']
    
    def clean_email(self):
        """Верификация эмейла"""
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise f.ValidationError('Этот эмейл уже используется!')
        return email


class UserConfirmForm(f.ModelForm):
    """Форма, куда нужно вводить код из эмейла"""
    temporary_password = f.CharField(
        max_length=6,
        label='Временный пароль',
        widget=f.TextInput(
            attrs={
                'class': 'register-fields'
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['temporary_password',]


class UserEditForm(f.ModelForm):
    """Форма для редактирования профиля пользователя"""
    avatar = f.ImageField(
        label='Аватар',
        widget=f.FileInput(
            attrs={
                'class': 'register-fields'
            }
        ),
        required=False
    )
    birthday = f.DateField(
        label='Дата рождения',
        widget=f.DateInput(
            attrs={
                'class': 'register-fields'
            }
        ),
        required=False
    )
    phone_number = f.CharField(
        label='Номер телефона',
        max_length=12,
        widget=f.TextInput(
            attrs={
                'class': 'register-fields'
            }
        ), required=False)
    country = f.CharField(
        label='Страна',
        max_length=50,
        widget=f.TextInput(
            attrs={
                'class': 'register-fields'
            }
        ),
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'phone_number',
            'birthday',
            'country'
        ]

        widgets = {
            'first_name': f.TextInput(
                attrs={'class': 'register-fields'
                       }
            ),
            'last_name': f.TextInput(
                attrs={'class': 'register-fields'
                       }
            ),
        }
