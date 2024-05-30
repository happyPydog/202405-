from datetime import datetime


class Holiday:
    def get_theme(self) -> str:
        today = self.get_today()
        if today.month == 12 and today.day == 25:
            return "Merry Xmas"
        return "Today is not Xmas"

    def get_today(self):
        return datetime.now().date()
