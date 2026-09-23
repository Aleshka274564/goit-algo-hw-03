from datetime import datetime

def get_days_from_today(date):
    try:
        
        user_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        # разница дат
        cons = today_date - user_date
        # разница в днях
        return cons.days
    except ValueError:
        # текст ошибки
        return "Неправильний формат дати. Очікується РРРР-ММ-ДД"

result = get_days_from_today("2025-10-09")

print("Количество дней:")
print(result)
