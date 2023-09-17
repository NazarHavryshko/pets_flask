import unittest

from website.validations import UserInformationValidation as UIV


class TestUserInformationValidation(unittest.TestCase):

    def test_validation_email(self):

        test_cases = (
            {
                'argument': 'test123@test.test',
                'expected_result': True
            },
            {
                'argument': 'testф123@test.test',
                'expected_result': False
            },
            {
                'argument': 'test123test.test',
                'expected_result': False
            },
            {
                'argument': 'test123@testtest',
                'expected_result': False
            },
            {
                'argument': 'test123@test.t1est',
                'expected_result': False
            },
            {
                'argument': 'test123@tes1t.test',
                'expected_result': False
            },
            {
                'argument': 'test123@tes-t.test',
                'expected_result': True
            },
            {
                'argument': 't@$est123@test.test',
                'expected_result': False
            },
            {
                'argument': 'te@st123@test.test',
                'expected_result': False
            },
            {
                'argument': 'test123@test.t+est',
                'expected_result': False
            },
            {
                'argument': 'te()st123@test.test',
                'expected_result': False
            },
            {
                'argument': '',
                'expected_result': False
            },
        )

        for test_case in test_cases:
            self.assertEqual(UIV.validation_email(test_case['argument']), test_case['expected_result'])

    def test_validation_password(self):

        test_cases = (
            {
                'argument': '123QWErty123',
                'expected_result': True
            },
            {
                'argument': '123qwerty123',
                'expected_result': False
            },
            {
                'argument': '',
                'expected_result': False
            },
            {
                'argument': '123QWERTY123',
                'expected_result': False
            },
            {
                'argument': '12QQww',
                'expected_result': True
            },
            {
                'argument': '12QQw',
                'expected_result': False
            },
            {
                'argument': '123QW Erty123',
                'expected_result': False
            },
            {
                'argument': '0123456789QWErty',
                'expected_result': True
            },
            {
                'argument': '0123456789QWErty132',
                'expected_result': False
            },
            {
                'argument': '123QWErty123+',
                'expected_result': False
            },
            {
                'argument': '123QWErty123-',
                'expected_result': False
            },
            {
                'argument': '123QWErty123*',
                'expected_result': False
            },
            {
                'argument': '123QWErty123/',
                'expected_result': False
            },
            {
                'argument': '123QWErty123(',
                'expected_result': False
            },
            {
                'argument': '123QWErty123)',
                'expected_result': False
            },
            {
                'argument': '123QWErty123@',
                'expected_result': False
            },
            {
                'argument': '123АБВабв123-',
                'expected_result': False
            },
            {
                'argument': '123QWErty123=',
                'expected_result': False
            },
        )

        for test_case in test_cases:
            test = UIV.validation_password(test_case['argument'])
            if test != test_case['expected_result']:
                print(test_case['argument'], test)
            self.assertEqual(test, test_case['expected_result'])

    def test_validation_name(self):

        test_cases = (
            {
                'argument': 'Test',
                'expected_result': True
            },
            {
                'argument': ' ',
                'expected_result': False
            },
            {
                'argument': 'te',
                'expected_result': True
            },
            {
                'argument': 't',
                'expected_result': False
            },
            {
                'argument': 'qwertyuIopasDfGH',
                'expected_result': True
            },
            {
                'argument': 'qwertyuIopasDfGHJ',
                'expected_result': False
            },
            {
                'argument': 'qwertyuIopa123',
                'expected_result': False
            },
            {
                'argument': 'иауглйц',
                'expected_result': False
            },
            {
                'argument': 'qwert-',
                'expected_result': False
            },
            {
                'argument': 'qwert+',
                'expected_result': False
            },
            {
                'argument': 'qwert*',
                'expected_result': False
            },
            {
                'argument': 'qwert/',
                'expected_result': False
            },
            {
                'argument': 'qwert(',
                'expected_result': False
            },
            {
                'argument': 'qwert)',
                'expected_result': False
            },
            {
                'argument': 'qwert"',
                'expected_result': False
            },
            {
                'argument': '.qwert',
                'expected_result': False
            },
        )

        for test_case in test_cases:
            self.assertEqual(UIV.validation_name(test_case['argument']), test_case['expected_result'])

    def test_validation_phone(self):

        test_cases = (
            {
                'argument': '+380000111222',
                'expected_result': True
            },
            {
                'argument': '+38000011122',
                'expected_result': False
            },
            {
                'argument': '+3800001112221',
                'expected_result': False
            },
            {
                'argument': '-380000111222',
                'expected_result': False
            },
            {
                'argument': '+280000111222',
                'expected_result': False
            },
            {
                'argument': '+370000111222',
                'expected_result': False
            },
            {
                'argument': '+380000111+02',
                'expected_result': False
            },
            {
                'argument': '+3800O0111222',
                'expected_result': False
            },
            {
                'argument': '+38O000111222',
                'expected_result': False
            },
            {
                'argument': '+381000111222',
                'expected_result': False
            },
            {
                'argument': '+380О00111222',
                'expected_result': False
            },
            {
                'argument': ' ',
                'expected_result': False
            },
            {
                'argument': '+3800*0111222',
                'expected_result': False
            },
            {
                'argument': '+3800+0111222',
                'expected_result': False
            },
            {
                'argument': '+380()0111222',
                'expected_result': False
            },
        )

        for test_case in test_cases:
            self.assertEqual(UIV.validation_phone(test_case['argument']), test_case['expected_result'])


