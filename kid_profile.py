# Вводим имя и номер шкафчика ребенка
name = input()
storage_number = list(input())
# Получаем удобную карточку для детского сада
print(f'Группа №{storage_number[0]}.')
print(f'{storage_number[2]}. {name}.')
number = ''.join(storage_number)
print(f'Шкафчик: {number}.')
print(f'Кроватка: {storage_number[1]}.')
