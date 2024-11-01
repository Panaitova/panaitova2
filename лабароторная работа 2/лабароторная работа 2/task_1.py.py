money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0  # Счетчик месяцев
current_money = money_capital + salary

while current_money >= spend:
    months += 1
    current_money -= spend
    spend *= (1 + increase)
    current_money += salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
