print("""Вы - бабушка А. Очнулись вы в темном помещении. 
Ваши действия:
	1. Выглянуть в окно
	2. Позвать на помощь
	3. Попытаться позвонить""")
action = int(input("Выбор: "))

if action == 1:
	print("""Вы выглянули в окно и узнали, что находитесь 
на Пустошах. Перед домом пробегает двухметровый Радскорпион.
Просто так на улицу не высунешься.
Вы можете:
	1. Посмотреть в шкафчике с оружием.
	2. Выпить стелл-стимулятор и стать невидимым
	3. Просто рвануть на улицу и броситься на скорпиона
	""")
	action = int(input("Вы выбрали: "))

	if action == 1:
		print("""Там вы обнаружили ракетницу 'Толстяк'.
Взвалив ее на плечо, вы пошли в бой.""")

	elif action == 2:
		print("""Вы невидимы и поэтому решили, что скорпион
вас не заметит, и пошли на улицу.""")
		
	elif action == 3:
		print("""Непонятно, на что вы рассчитывали.
Сегодня скорпион поужинает бабушкой. Ваша жизнь окончена.""")


elif action == 2:
	print("""На помощь отозвались рейдеры и отобрали все 
деньги-крышки""")


elif action == 3:
	print("""Вы попытались позвонить, но единственное, 
что напоминает телефон это ваш башмак. Но это вас 
не остановило,и вы-таки с него дозвонились до базы 
супермутантов.""")