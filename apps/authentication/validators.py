from django.core.validators import RegexValidator


no_whitespaces = RegexValidator(
    regex = r'/s',
    message = 'Don\'t use Whitespaces',
    inverse_match = True
)
special_characters = RegexValidator(
    regex = r'[*&%$#@_-!]',
    message = 'Use at least 1 Special Character'
)
uppercase_letters = RegexValidator(
    regex = r'[A-Z]',
    message = 'Use at least 1 UPPERCASE letter'
)
lowercase_letters = RegexValidator(
    regex = r'[a-z]',
    message = 'Use at least 1 lowercase letter'
)
number_validator = RegexValidator(
    regex = r'\d+',
    message = 'Use at least 1 number'
)

cpf_validator = RegexValidator(
    regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message = 'CPF Inválido'
)