# -*- coding: utf-8 -*-

import simple_draw as sd
import math


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def all_type_v4(start_x, start_y, angle, length, width):
    colour_list = [
        (1, 'RED'),
        (2, 'ORANGE'),
        (3, 'YELLOW'),
        (4, 'GREEN'),
        (5, 'CYAN'),
        (6, 'BLUE'),
        (7, 'PURPLE')
    ]
    form_list = [
        (0, 'Треугольник'),
        (1, 'Квадрат'),
        (2, 'Пятиугольник'),
        (3, 'Шестиугольник'),
    ]
    form_number_dict = {
        '0': 3,
        '1': 4,
        '2': 5,
        '3': 6
    }
    print('Список доступных цветов', colour_list)
    user_input = input("Введите, пожалуйста, номер цвета: ")
    number_colour = int(user_input)

    colour_number_dict = {
        '1': (255, 0, 0),
        '2': (255, 127, 0),
        '3': (255, 255, 0),
        '4': (0, 255, 0),
        '5': (0, 255, 255),
        '6': (0, 0, 255),
        '7': (255, 0, 255)
    }

    print('Список доступных фигур', form_list)
    user_input_2 = input("Введите, пожалуйста, номер фигуры: ")
    form = int(user_input_2)
    count_side = form_number_dict[str(form)]

    if form < 0 or form > 3:
        print('Введите корректное значение от 0 до 3')
    else:
        if number_colour < 1 or number_colour > 7:
            print('Введите корректное значение от 1 до 7')
        else:

            point = sd.get_point(start_x, start_y)
            radian = (angle * math.pi) / 180
            end_y = math.sin(radian) * length
            end_x = math.cos(radian) * length
            last_point = sd.get_point(end_x + start_x, end_y + start_y)
            sd.line(point, last_point, colour_number_dict[str(number_colour)], width)

            if count_side == int(count_side):
                for _ in range(count_side - 2):
                    point = last_point
                    sec_start_x = point.x
                    sec_start_y = point.y
                    angle += 180 - ((count_side - 2) * 180 / count_side)
                    radian = (angle * math.pi) / 180
                    end_y = math.sin(radian) * length
                    end_x = math.cos(radian) * length
                    last_point = sd.get_point(end_x + sec_start_x, end_y + sec_start_y)
                    sd.line(point, last_point, colour_number_dict[str(number_colour)], width)
                end_point = sd.get_point(start_x, start_y)
                sd.line(last_point, end_point, colour_number_dict[str(number_colour)], width)


all_type_v4(100, 100, 0, 200, 3)
sd.pause()
