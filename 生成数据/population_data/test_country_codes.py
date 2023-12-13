import unittest
from country_codes import get_country_code


class CountryCodeTestCase(unittest.TestCase):

    def test_get_country_code(self):
        code = get_country_code("United States")
        self.assertEqual(code, 'us')

    def test_get_country_code_2(self):
        code = get_country_code("United States")
        self.assertEqual(code, 'af')


# 需要命令行执行，否则无法识别单元测试
unittest.main()
