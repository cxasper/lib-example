from django.conf import settings

def sum_numbers(first_value, second_value):
    result = first_value + second_value
    if settings.DIVIDEND:
        return result/settings.DIVIDEND
    return result
