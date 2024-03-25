# # -*- coding: utf-8 -*-

import simple_draw as sd



# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle(start_x, start_y, angle, length,width):
    point = sd.get_point(start_x,start_y)
    line = sd.get_vector(point,angle,length,width)
    line.draw()
    line = sd.get_vector(line.end_point,angle + 120, length,width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 240, length, width)
    line.draw()

triangle(100,100,0,100,5)

def squad(start_x, start_y, angle, length,width):
    point = sd.get_point(start_x,start_y)
    line = sd.get_vector(point,angle,length,width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 90, length, width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 180, length, width)
    line.draw()
    line = sd.get_vector(line.end_point,angle + 270, length,width)
    line.draw()

squad(400,100,0,100,5)

def pentagon(start_x, start_y, angle, length,width):
    point = sd.get_point(start_x,start_y)
    line = sd.get_vector(point,angle,length,width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 72, length, width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 72*2, length, width)
    line.draw()
    line = sd.get_vector(line.end_point,angle + 72*3, length,width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 72*4, length, width)
    line.draw()

pentagon(100,300,0,100,5)

def hexagon(start_x, start_y, angle, length,width):
    point = sd.get_point(start_x,start_y)
    line = sd.get_vector(point,angle,length,width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 60, length, width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 60*2, length, width)
    line.draw()
    line = sd.get_vector(line.end_point,angle + 60*3, length,width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 60 * 4, length, width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 60 * 5, length, width)
    line.draw()

hexagon(400,300,0,100,5)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def all_type(start_x, start_y, count_side, angle, length, width):
    point = sd.get_point(start_x, start_y)
    line = sd.get_vector(point, angle, length, width)
    line.draw()
    if count_side == 3:
        for _ in range(count_side - 2):
            angle += 120
            line = sd.get_vector(line.end_point, angle, length, width)
            line.draw()
        sd.line(line.end_point, point, width=width)
    elif count_side == 4:
        for _ in range(count_side - 2):
            angle += 90
            line = sd.get_vector(line.end_point, angle, length, width)
            line.draw()
        sd.line(line.end_point, point, width=width)
    elif count_side == 5:
        for _ in range(count_side - 2):
            angle += 72
            line = sd.get_vector(line.end_point, angle, length, width)
            line.draw()
        sd.line(line.end_point, point, width=width)
    elif count_side == 6:
        for _ in range(count_side - 2):
            angle += 60
            line = sd.get_vector(line.end_point, angle, length, width)
            line.draw()
        sd.line(line.end_point, point, width=width)


all_type(200, 0, 3, 70, 100, 3)

def all_type_v2(start_x, start_y, count_side, angle, length, width):
    point = sd.get_point(start_x, start_y)
    line = sd.get_vector(point, angle, length, width)
    line.draw()
    if count_side == int(count_side):
        for _ in range(count_side - 2):
            angle += 180-((count_side-2)*180/count_side)
            line = sd.get_vector(line.end_point, angle, length, width)
            line.draw()
        sd.line(line.end_point, point, width=width)


all_type_v2(200, 200, 3, 0, 100, 3)
sd.pause()
