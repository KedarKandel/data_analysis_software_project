from collections import defaultdict
from statistics import mean, stdev
from typing import Dict, Any
from utils.date_helpers import format_month_name

def calculate_monthly_stats(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Calculate detailed statistics for each month
    Returns: {
        "1": {
            "name": "January",
            "total": 15000,
            "daily_avg": 500.0,
            "daily_std": 150.2,
            "peak_day": {"date": "2025-01-15", "visitors": 1200},
            "quietest_day": {"date": "2025-01-03", "visitors": 150},
            "days_recorded": 31,
            "trend": "increasing"  # or "decreasing"/"stable"
        },
        ...
    }
    """
    monthly_stats = defaultdict(dict)
    previous_month_total = None
    
    for month_data in data['months']:
        month_num = month_data['month'] + 1  # Convert 0-11 to 1-12
        days = month_data['days']
        daily_counts = [day['total'] for day in days]
        
        # Basic statistics
        monthly_stats[month_num] = {
            'name': format_month_name(month_num),
            'total': month_data['total'],
            'daily_avg': round(mean(daily_counts), 2),
            'daily_std': round(stdev(daily_counts), 2) if len(daily_counts) > 1 else 0.0,
            'days_recorded': len(days)
        }
        
        # Day extremes with dates
        peak_day = max(days, key=lambda x: x['total'])
        quietest_day = min(days, key=lambda x: x['total'])
        
        monthly_stats[month_num].update({
            'peak_day': {
                'date': f"{data['year']}-{month_num:02d}-{peak_day['day']:02d}",
                'visitors': peak_day['total']
            },
            'quietest_day': {
                'date': f"{data['year']}-{month_num:02d}-{quietest_day['day']:02d}",
                'visitors': quietest_day['total']
            }
        })
        
        # Trend analysis
        if previous_month_total is not None:
            trend = (
                'increasing' if month_data['total'] > previous_month_total else
                'decreasing' if month_data['total'] < previous_month_total else
                'stable'
            )
            monthly_stats[month_num]['trend'] = trend
            monthly_stats[month_num]['change_pct'] = round(
                ((month_data['total'] - previous_month_total) / previous_month_total) * 100, 2
            )
        else:
            monthly_stats[month_num]['trend'] = 'baseline'
            monthly_stats[month_num]['change_pct'] = 0.0
        
        previous_month_total = month_data['total']
    
    return dict(monthly_stats)

def get_monthly_comparison(monthly_stats: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compare months against each other
    Returns: {
        "busiest_month": {"month": 7, "name": "July", "visitors": 25000},
        "quietest_month": {"month": 1, "name": "January", "visitors": 10000},
        "most_consistent": {"month": 4, "name": "April", "std_dev": 85.3},
        "most_variable": {"month": 12, "name": "December", "std_dev": 420.1}
    }
    """
    if not monthly_stats:
        return {}
    
    months = list(monthly_stats.values())
    
    busiest = max(months, key=lambda x: x['total'])
    quietest = min(months, key=lambda x: x['total'])
    most_consistent = min(months, key=lambda x: x['daily_std'])
    most_variable = max(months, key=lambda x: x['daily_std'])
    
    return {
        'busiest_month': {
            'month': next(k for k, v in monthly_stats.items() if v['name'] == busiest['name']),
            'name': busiest['name'],
            'visitors': busiest['total']
        },
        'quietest_month': {
            'month': next(k for k, v in monthly_stats.items() if v['name'] == quietest['name']),
            'name': quietest['name'],
            'visitors': quietest['total']
        },
        'most_consistent': {
            'month': next(k for k, v in monthly_stats.items() if v['name'] == most_consistent['name']),
            'name': most_consistent['name'],
            'std_dev': most_consistent['daily_std']
        },
        'most_variable': {
            'month': next(k for k, v in monthly_stats.items() if v['name'] == most_variable['name']),
            'name': most_variable['name'],
            'std_dev': most_variable['daily_std']
        }
    }

def detect_seasonal_patterns(monthly_stats: Dict[str, Any]) -> Dict[str, Any]:
    """
    Identify seasonal trends in the data
    Returns: {
        "peak_season": {"months": [6,7,8], "avg_visitors": 22000},
        "off_season": {"months": [1,2,11], "avg_visitors": 9000},
        "shoulder_months": [4,5,9,10]
    }
    """
    if len(monthly_stats) < 12:
        return {'warning': 'Insufficient data for full seasonal analysis'}
    
    # Group by season
    seasons = {
        'Winter': [12, 1, 2],
        'Spring': [3, 4, 5],
        'Summer': [6, 7, 8],
        'Fall': [9, 10, 11]
    }
    
    seasonal_avgs = {
        season: round(mean(
            monthly_stats[str(m)]['total'] for m in months
        ), 2)
        for season, months in seasons.items()
    }
    
    peak_season = max(seasonal_avgs.items(), key=lambda x: x[1])
    off_season = min(seasonal_avgs.items(), key=lambda x: x[1])
    
    return {
        'peak_season': {
            'name': peak_season[0],
            'months': seasons[peak_season[0]],
            'avg_visitors': peak_season[1]
        },
        'off_season': {
            'name': off_season[0],
            'months': seasons[off_season[0]],
            'avg_visitors': off_season[1]
        },
        'seasonal_avgs': seasonal_avgs
    }