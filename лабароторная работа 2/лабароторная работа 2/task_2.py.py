import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_needed_capital = 0  # Общая подушка безопастности

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
# Считаем расходы за каждый месяц
for _ in range(months):
    # Рассчитываем нехватку средств текущего месяца
    if spend > salary:
        deficit = spend - salary
        total_needed_capital += deficit  # Суммируем нехватку в общую подушку безопастности

    # Увеличиваем расходы для следующего месяца
    spend *= (1 + increase)

# Округляем до целого числа
total_needed_capital = math.ceil(total_needed_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {total_needed_capital}")

