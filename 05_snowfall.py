# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1800, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

def random_values_snow():
    return {

        'start_x': random.randrange(50, 1600),
        'start_y': random.randrange(500, 650, 50),
        'a_list': random.randrange(1, 8) / 10,
        'b_list': random.randrange(1, 8) / 10,
        'c_list': random.randrange(30, 60),
        'length_list': random.randrange(20, 50),

    }


# factor_a - место    ответвления    лучиков
# factor_b - длина    лучиков
# factor_c - угол    отклонения    лучиков

all_random_values = []

for _ in range(N):
    all_random_values.append(random_values_snow())

sd.start_drawing()

while True:
    # sd.clear_screen()
    for i in all_random_values:

        point_starter = sd.get_point(i['start_x'], i['start_y'])
        sd.snowflake(point_starter, i['length_list'], sd.background_color, i['a_list'], i['b_list'], i['c_list'])

        i['start_y'] -= 10
        if i['start_y'] < 1:
            all_random_values.remove(i)
        i['start_x'] -= sd.randint(-10, 10)

        point_starter = sd.get_point(i['start_x'], i['start_y'])
        sd.snowflake(point_starter, i['length_list'], sd.COLOR_WHITE, i['a_list'], i['b_list'], i['c_list'])

    all_random_values.append(random_values_snow())

    sd.finish_drawing()

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
