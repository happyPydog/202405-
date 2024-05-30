import unittest
import datetime

from holiday import Holiday


class TestHoliday(unittest.TestCase):
    def setUp(self) -> None:
        self.holiday = Holiday()

    def test_get_theme_is_xmax(self):
        self.given_today(month=12, day=25)
        self.expected_theme_should_be(theme="Merry Xmas")

    def test_get_theme_not_xmax(self):
        self.given_today(month=11, day=25)
        self.expected_theme_should_be(theme="Today is not Xmas")

    def expected_theme_should_be(self, theme):
        assert self.holiday.get_theme() == theme

    def given_today(self, month, day):
        self.holiday.get_today = lambda: datetime.date(2000, month, day)
