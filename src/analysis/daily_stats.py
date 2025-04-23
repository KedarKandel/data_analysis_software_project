from statistics import mean, stdev
from typing import Dict, Any

def calculate_daily_stats(data: Dict[str, Any]) -> Dict[str, float]:
    """Calculate daily visitor statistics"""
    daily_counts = [
        day['total']
        for month in data['months']
        for day in month['days']
    ]
    
    return {
        'total': sum(daily_counts),
        'average': round(mean(daily_counts), 2),
        'std_dev': round(stdev(daily_counts), 2),
        'max': max(daily_counts),
        'min': min(daily_counts)
    }