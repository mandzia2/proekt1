import random

# Списки для генерации ников
adjectives = ['Сильный', 'Умный', 'Красивый', 'Быстрый', 'Ловкий']
nouns = ['Лев', 'Тигр', 'Орел', 'Волк', 'Ястреб']

# Функция для генерации ника
def generate_username():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(100, 999)
    username = f"{adjective}_{noun}_{number}"
    return username

# Генерируем и выводим 5 ников
for _ in range(100):
    username = generate_username()
    print(username)