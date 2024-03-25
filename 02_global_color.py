# -*- coding: utf-8 -*-
import simple_draw as sd
import math


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def all_type_v3(start_x, start_y, count_side, angle, length, width):
    colour_list = [
        (1, 'RED'),
        (2, 'ORANGE'),
        (3, 'YELLOW'),
        (4, 'GREEN'),
        (5, 'CYAN'),
        (6, 'BLUE'),
        (7, 'PURPLE')
    ]
    print('Список доступных цветов', colour_list)
    user_input = input("Введите, пожалуйста, номер цвета: ")
    number_colour = int(user_input)

    number_list = {
        '1': (255, 0, 0),
        '2': (255, 127, 0),
        '3': (255, 255, 0),
        '4': (0, 255, 0),
        '5': (0, 255, 255),
        '6': (0, 0, 255),
        '7': (255, 0, 255)
    }
    if number_colour < 1 or number_colour > 7:
        print('Введите корректное значение от 1 до 7')
    else:
        point = sd.get_point(start_x, start_y)
        radian = (angle * math.pi) / 180
        end_y = math.sin(radian) * length
        end_x = math.cos(radian) * length
        last_point = sd.get_point(end_x+start_x, end_y+start_y)
        sd.line(point, last_point, number_list[str(number_colour)], width)

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
                sd.line(point, last_point, number_list[str(number_colour)], width)
            end_point = sd.get_point(start_x, start_y)
            sd.line(last_point, end_point, number_list[str(number_colour)], width)


all_type_v3(100, 100, 5, 0, 200, 3)

sd.pause()
