name = input("Здравствуйте! Напишите Ваше имя: ").capitalize()
age = int(input("Укажите Ваш возраст (полных лет): "))
weight = float(input("Укажите Ваш вес в кг: "))
height = float(input("Укажите Ваш рост в м, используя точку (напр. 1.75): "))

bmi_result = weight / (height ** 2)
bmi = round(bmi_result, 1)

water_per_kg = 30
water_recomend = weight * water_per_kg / 1000

print(f"""Отчет для пользователя: {name} ({age} г.
Ваш Индекс Массы Тела: {bmi} кг/м²
Рекомендуемая норма воды: {water_recomend} л. в день

print("Расчет окончен. Будьте здоровы!""")
