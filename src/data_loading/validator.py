def validate_zoo_data(data: dict) -> bool:
    """Validate the structure of zoo data"""
    required_keys = {'year', 'total', 'months'}
    if not all(key in data for key in required_keys):
        raise ValueError("Missing required top-level keys")
    
    for month in data['months']:
        if not isinstance(month.get('month'), int):
            raise ValueError("Invalid month format")
        if not all(k in month for k in ('total', 'days')):
            raise ValueError("Missing month-level keys")
            
        for day in month['days']:
            if not all(k in day for k in ('day', 'total', 'id')):
                raise ValueError("Missing day-level keys")
    return True