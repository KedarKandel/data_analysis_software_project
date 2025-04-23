# Console output formatter

def print_report(year: int, daily_stats: dict, monthly_stats: dict) -> None:
    """Print formatted report to console"""
    print(f"\n{' ZOO VISITORS ANALYSIS ':=^50}")
    print(f"\nYear: {year}\n")
    
    print("=== Daily Statistics ===")
    print(f"Total visitors: {daily_stats['total']:,}")
    print(f"Average daily: {daily_stats['average']:,}")
    print(f"Standard deviation: {daily_stats['std_dev']:,}")
    print(f"Peak day: {daily_stats['max']:,} visitors")
    print(f"Quietest day: {daily_stats['min']:,} visitors\n")
    
    print("=== Monthly Highlights ===")
    for month, stats in monthly_stats.items():
        print(f"Month {month}: {stats['total']:,} visitors")