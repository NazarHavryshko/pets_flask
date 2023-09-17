import re


class UserInformationValidation:

    @staticmethod
    def validation_email(email: str) -> bool:

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'

        return True if re.match(pattern, email) else False

    @staticmethod
    def validation_password(password: str) -> bool:
        pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[A-Za-z\d]{6,16}$'

        return True if re.match(pattern, password) else False

    @staticmethod
    def validation_name(name: str) -> bool:
        pattern = r'^[a-zA-Z]{2,16}$'

        return True if re.match(pattern, name) else False

    @staticmethod
    def validation_phone(phone: str) -> bool:
        pattern = r'^\+380\d{9}$'

        return True if re.match(pattern, phone) else False
