# This is a file to be used for prompt engineering challenge 1

def process_user_data(data):
    result = []
    for d in data:
        if d.get('active', False):
            temp = {
                'name': d.get('name'),
                'email': d.get('email'),
                'last_login': d.get('last_login'),
                'score': calculate_score(d),
                'status': determine_status(d.get('last_login'))
            }
            result.append(temp)
    return result

def calculate_score(user):
    base_score = (user.get('clicks', 0) * 2 + user.get('shares', 0) * 3) / 5
    return round(base_score, 2)

def determine_status(last_login):
    from datetime import datetime, timedelta
    if not last_login:
        return 'unknown'
    days_inactive = (datetime.now() - datetime.strptime(last_login, "%Y-%m-%d")).days
    return 'inactive' if days_inactive > 30 else 'active'
