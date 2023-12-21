import unittest

import work_report
from work_report import calculate_vacation


class CalculateVacationTestCase(unittest.TestCase):

    def test_calculate_vacation(self):
        calculate_vacation()
        print(work_report.vacations_map)
        self.assertEqual("us", 'us')


# 需要命令行执行，否则无法识别单元测试
work_report.vacations_map = {}
work_report.clock_go_home = {"2023-12-01": "2023-12-01 19:41:27",
                             "2023-12-04": "2023-12-04 18:11:55",
                             "2023-12-05": "2023-12-05 18:08:39",
                             "2023-12-06": "2023-12-06 22:04:01",
                             "2023-12-07": "2023-12-08 00:11:08",
                             "2023-12-08": "2023-12-08 18:00:28",
                             "2023-12-11": "2023-12-12 04:03:32",
                             "2023-12-12": "2023-12-12 18:26:05",
                             "2023-12-13": "2023-12-13 18:30:41",
                             "2023-12-14": "2023-12-14 19:00:29",
                             "2023-12-15": "2023-12-15 18:24:23",
                             "2023-12-18": "2023-12-18 22:19:20",
                             "2023-12-19": "2023-12-19 18:51:39",
                             "2023-12-20": "2023-12-20 21:30:45",
                             "2023-12-21": "2023-12-21 09:27:37"}
unittest.main()
