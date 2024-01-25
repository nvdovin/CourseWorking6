from django import template

register = template.Library()

@register.filter()
def paragrapher(text: str):
    new_text = []
    text_blocks = text.split('\r')
    for block in text_blocks:
        new_block = f"<p>{block}</p>"
        new_text.append(new_block)
    return "\n".join(new_text)