# Entry point

from data_loading.loader import fetch_zoo_data, save_to_json
from data_loading.validator import validate_zoo_data
from analysis.daily_stats import calculate_daily_stats
from analysis.monthly_stats import calculate_monthly_stats
from reporting.console import print_report

API_URL = 'https://korkeasaarenkavijat.onrender.com/api/data/year'
DATA_PATH = '../data/raw/data.json'

def main():
    try:
        # Load and validate data
        data = fetch_zoo_data(API_URL)
        validate_zoo_data(data)
        save_to_json(data, DATA_PATH)
        
        # Perform analysis
        daily_stats = calculate_daily_stats(data)
        monthly_stats = calculate_monthly_stats(data)
        
        # Generate report
        print_report(
            year=data['year'],
            daily_stats=daily_stats,
            monthly_stats=monthly_stats
        )
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()