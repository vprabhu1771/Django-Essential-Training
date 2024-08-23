from django.core.exceptions import ValidationError


# creating a validator function
def validate_author_gmail_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("GMail ID is Required")