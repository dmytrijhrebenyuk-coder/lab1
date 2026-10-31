def calculate_days(start_km=10.0, increase_percent=10.0, target_km=50.0):
    """
    Розрахунок кількості днів, за які спортсмен подолає цільову дистанцію.
    Повертає кортеж: (дні для сумарної дистанції, дні для денної дистанції).
    """
    # 1. Якщо мається на увазі сумарна дистанція за всі дні:
    days_total = 1
    current_day_km = start_km
    total_km = start_km
    while total_km < target_km:
        current_day_km *= (1 + increase_percent / 100)
        total_km += current_day_km
        days_total += 1

    # 2. Якщо мається на увазі дистанція за один день:
    days_single = 1
    day_km = start_km
    while day_km < target_km:
        day_km *= (1 + increase_percent / 100)
        days_single += 1

    return days_total, round(total_km, 2), days_single, round(day_km, 2)