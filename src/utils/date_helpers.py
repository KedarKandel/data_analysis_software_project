# Date formatting/parsing

from datetime import datetime
from typing import Optional

MONTH_NAMES = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

def format_month_name(month_num: int) -> str:
    """Convert month number (1-12) to full name"""
    if 1 <= month_num <= 12:
        return MONTH_NAMES[month_num - 1]
    raise ValueError("Month must be between 1 and 12")

def parse_date(date_str: str, fmt: str = "%Y-%m-%d") -> Optional[datetime]:
    """Safely parse date string to datetime object"""
    try:
        return datetime.strptime(date_str, fmt)
    except (ValueError, TypeError):
        return None