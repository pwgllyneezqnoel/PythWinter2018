# Алгоритм:
# 1. Проверяем есть ли человек в списке допущенных к игре.
# 2. Игрок делает ставку 
# 3. Выбирает ставить на цвет или на число
# 4. Далее, считаем выигрыш или потерю 

import random

gold_list = ['Султанмурад', 'Андрей', 'Саид', 'Аня', 'Махач']

name = input('Добро пожаловать в казино-пери. Представьтесь \
пожалуйста: ')
player = {'Имя':name}
if name in gold_list:
	print('Проходите пожалуйста')
	player['Деньги'] = int(input('Сколько у Вас денег? '))
	while True:

else:
	print('Очень жаль, но вход только для сотрудников')
