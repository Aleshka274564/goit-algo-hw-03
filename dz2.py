import random

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    
    # случайные числa
    numbers = random.sample(range(min, max + 1), quantity)
    
    # cортируем список 
    numbers.sort()
    
    # результат
    return numbers

lottery_numbers = get_numbers_ticket(1, 67, 6)
print("Ваші лотерейні числа:", lottery_numbers)

bad_ticket = get_numbers_ticket(1, 1005, 5)
print("Перевірка помилки (має бути []):", bad_ticket)
