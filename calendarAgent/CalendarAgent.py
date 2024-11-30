from datetime import datetime, timedelta
import re
from typing import Tuple, Optional

class DateAgent:
    def __init__(self):
        self.quarters = {
            "Q1": (1, 1, 3, 31),
            "Q2": (4, 1, 6, 30),
            "Q3": (7, 1, 9, 30),
            "Q4": (10, 1, 12, 31)
        }

    def parse_period(self, period: str) -> datetime:
        """
        Parses a period string (e.g., 'Q1 2023', 'June 2024', 'mid Jan 2024') and returns the start date.
        """
        match = re.match(r'(Q[1-4]) (\d{4})', period)
        if match:
            quarter, year = match.groups()
            start_month, start_day, _, _ = self.quarters[quarter]
            return datetime(int(year), start_month, start_day)
        
        match = re.match(r'(\w+) (\d{4})', period)
        if match:
            month, year = match.groups()
            start_date = datetime.strptime(f"1 {month} {year}", "%d %B %Y")
            return start_date
        
        match = re.match(r'mid (\w+) (\d{4})', period)
        if match:
            month, year = match.groups()
            start_date = datetime.strptime(f"15 {month} {year}", "%d %B %Y")
            return start_date
        
        raise ValueError(f"Invalid period format: {period}")

    def calculate_days_between(self, start_period: str, end_period: str) -> int:
        """
        Calculates the number of days between two periods.
        """
        start_date = self.parse_period(start_period)
        end_date = self.parse_period(end_period)
        return (end_date - start_date).days

    def get_period_dates(self, period: str) -> Tuple[datetime, datetime]:
        """
        Returns the start and end dates for a given period.
        """
        match = re.match(r'(Q[1-4]) (\d{4})', period)
        if match:
            quarter, year = match.groups()
            start_month, start_day, end_month, end_day = self.quarters[quarter]
            start_date = datetime(int(year), start_month, start_day)
            end_date = datetime(int(year), end_month, end_day)
            return start_date, end_date
        
        match = re.match(r'(\w+) (\d{4})', period)
        if match:
            month, year = match.groups()
            start_date = datetime.strptime(f"1 {month} {year}", "%d %B %Y")
            end_date = (start_date + timedelta(days=31)).replace(day=1) - timedelta(days=1)
            return start_date, end_date
        
        match = re.match(r'mid (\w+) (\d{4})', period)
        if match:
            month, year = match.groups()
            start_date = datetime.strptime(f"15 {month} {year}", "%d %B %Y")
            end_date = (start_date + timedelta(days=31)).replace(day=1) - timedelta(days=1)
            return start_date, end_date
        
        raise ValueError(f"Invalid period format: {period}")

    def get_last_days_of_year(self, year: int, days: int) -> Tuple[datetime, datetime]:
        """
        Returns the start and end dates for the last 'days' days of the given year.
        """
        end_date = datetime(year, 12, 31)
        start_date = end_date - timedelta(days=days-1)
        return start_date, end_date

    def get_days_from_date(self, start_date: datetime, days: int) -> Tuple[datetime, datetime]:
        """
        Returns the start and end dates for a period starting from 'start_date' and lasting 'days' days.
        """
        end_date = start_date + timedelta(days=days-1)
        return start_date, end_date

# Example usage
agent = DateAgent()

# First 125 days of any year
start_date = datetime(2023, 1, 1)
start_date, end_date = agent.get_days_from_date(start_date, 125)
print(f"First 125 days: {start_date} to {end_date}")

# Last 36 days of any year
start_date_end, end_date_end = agent.get_last_days_of_year(2023, 36)
print(f"Last 36 days: {start_date_end} to {end_date_end}")

# Calculate days between the periods
days_between_start = (end_date - start_date).days + 1
days_between_end = (end_date_end - start_date_end).days + 1

print(f"Days in first 125 days: {days_between_start}")
print(f"Days in last 36 days: {days_between_end}")

