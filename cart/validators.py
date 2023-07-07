from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from re import match
from django.core.validators import RegexValidator


class PhoneNumberValidator:
    def __call__(self, number):
        phone_number_pattern = r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
        if not match( phone_number_pattern, number):
            return ValidationError('Invalid phone number')
        else:
            return ValidationError({'message':'Phone-number is valid'}, status=HTTP_202_ACCEPTED)

    # def get_help_text(self):
    #     return 'Your phone number must contain optional country code, optional parentheses for the area code, and separators between digits.'


class ZipCodeValidator:
    def __call__(self, zipcode):
        zipcode_pattern = r"^[0-9]{5}(?:-[0-9]{4})?$"
        if not match( zipcode_pattern, zipcode):
            return ValidationError('Invalid Zip-code number')
        else:
            return ValidationError({'message':'Zip-code number is valid'}, status=HTTP_202_ACCEPTED)

    # def get_help_text(self):
    #     return "Your zip-code must contain five digits, with an optional hyphen followed by four more digits. Valid examples include '12345' and '98765-4321'."


class eMoneyNumberValidator:
    def __call__(self, money_number):
        emoney_number_pattern = r"/^[0]?[6789]\d{9}$/"
        if not match( emoney_number_pattern, money_number):
            return ValidationError('Invalid transaction number')
        else:
            return ValidationError({'message':'Transaction number is valid'}, status=HTTP_202_ACCEPTED)

    # def get_help_text(self):
    #     return 'Your phone number must starts with an optional 0, followed by a digit from 6 to 9, and then followed by exactly nine digits.'


class eMoneyPinValidator:
    def __call__(self, money_pin):
        emoney_pin_pattern = r"[0-9]{4}"
        if not match( emoney_pin_pattern, money_pin):
            return ValidationError("Invalid transaction number's pin")
        else:
            return ValidationError({"message":"transaction number's pin is valid"}, status=HTTP_202_ACCEPTED)
        pass

    # def get_help_text(self):
    #     return 'Your pin must contain four digits.'