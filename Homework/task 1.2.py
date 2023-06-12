# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

#import random
#my_favorite_songs = [
#    ['Waste a Moment', 3.03],
#    ['New Salvation', 4.02],
#    ['Staying\' Alive', 3.40],
#    ['Out of Touch', 3.03],
#    ['A Sorta Fairytale', 5.28],
#    ['Easy', 4.15],
#    ['Beautiful Day', 4.04],
#    ['Nowhere to Run', 2.58],
#    ['In This World', 4.02],
#]

#random_my_favorite_songs = random.sample(my_favorite_songs , 3 )
#total = sum([x[1] for x in random_my_favorite_songs])
#print(f"Три песни звучат {total} минут.")




# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

random_values = random.sample(list(my_favorite_songs_dict.values()), 3)
print(random_values)

total = sum([s for s  in random_values])

print(f"Вывод: Три песни звучат {total} минут")