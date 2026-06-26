name = input("Здравствуйте! Напишите Ваше имя: ").capitalize()
age = int(input("Укажите Ваш возраст (полных лет): "))
height = float(input("Укажите Ваш рост в м, используя точку (напр. 1.75): "))
weight = float(input("Укажите Ваш вес в кг: "))


def BMI(user_height, user_weight):  # Вычисление ИМТ
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


def water_recomendation(user_weight):  # Вычисление нормы воды
    water_per_kg = 30
    return round(user_weight * water_per_kg / 1000)


print(f"""Отчет для пользователя: {name} ({age} г.)
Твой Индекс Массы Тела: {BMI(height, weight)} кг/м²
Рекомендуемая норма воды: {water_recomendation(weight)} л. в день

Расчет окончен. Будьте здоровы!""")
