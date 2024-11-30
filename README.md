# Date Agent

## Overview

🚀 **Unveiling the Date Agent: Streamlining Period Calculations in Python!** 🚀

The Date Agent is designed to efficiently handle and calculate date-related tasks, with added support for various period formats and chain of thought processing.

## Features

1. **Initialization**: Defines quarter periods (Q1, Q2, Q3, Q4) for easy reference.
   
2. **`parse_period` Method**: Parses periods like "Q1 2023", "June 2024", and "mid Jan 2024" to return the correct start date.

3. **`calculate_days_between` Method**: Calculates the number of days between two given periods.

4. **`get_period_dates` Method**: Returns the start and end dates for specified periods, including quarters and months.

5. **`get_last_days_of_year` Method**: Provides the start and end dates for the last 'n' days of a given year.

6. **`get_days_from_date` Method**: Generates a period starting from a given date and lasting for a specified number of days.

## Example Usage

Here's how you can use the Date Agent:

```python
from datetime import datetime

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
