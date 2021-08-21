from django.core.validators import RegexValidator

phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
