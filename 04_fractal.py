# -*- coding: utf-8 -*-
import math
import random
import simple_draw as sd

sd.resolution = (1200, 600)


# #
# # # 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# # # Функция должна принимать параметры:
# # # - точка начала рисования,
# # # - угол рисования,
# # # - длина ветвей,
# # # Отклонение ветвей от угла рисования принять 30 градусов,
# #
# # def left_branch(start_x, start_y, variation, angle, length):
# #     start_point = sd.get_point(start_x, start_y)
# #     left_angle = angle + variation
# #     radian = (left_angle * math.pi) / 180
# #     end_y = math.sin(radian) * length
# #     end_x = math.cos(radian) * length
# #     last_point = sd.get_point(end_x + start_x, end_y + start_y)
# #     sd.line(start_point, last_point, width=3)
# #
# #
# # def right_branch(start_x, start_y, variation, angle, length):
# #     start_point = sd.get_point(start_x, start_y)
# #     right_angle = angle - variation
# #     radian = (right_angle * math.pi) / 180
# #     end_y = math.sin(radian) * length
# #     end_x = math.cos(radian) * length
# #     last_point = sd.get_point(end_x + start_x, end_y + start_y)
# #     sd.line(start_point, last_point, width=3)
# #
# #
# # def draw_branches_v1(start_x, start_y, angle, length):
# #     right_branc(start_x, start_y, 30, angle, length)
# #     left_branc(start_x, start_y, 30, angle, length)
# #
# #
# #
# #
# # draw_branches_v1(100, 100, 90, 100)
#
# # 2) Сделать draw_branches рекурсивной
# # - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# # - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
# #   с параметром "угол рисования" равным углу только что нарисованной ветви,
# #   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви
#
# def draw_branches_v2(start_x, start_y, angle, variation, length):
#     root_start_point = sd.get_point(start_x, start_y)
#     root_angle = angle
#     root_radian = (root_angle * math.pi) / 180
#     root_end_y = math.sin(root_radian) * length
#     root_end_x = math.cos(root_radian) * length
#     root_last_point = sd.get_point(root_end_x + start_x, root_end_y + start_y)
#     sd.line(root_start_point, root_last_point, width=2)
#
#     if length < 5:
#         return
#
#     start_point = sd.get_point(root_last_point.x, root_last_point.y)
#     left_angle = angle + variation
#     left_radian = (left_angle * math.pi) / 180
#     left_end_y = math.sin(left_radian) * length
#     left_end_x = math.cos(left_radian) * length
#     left_last_point = sd.get_point(left_end_x + root_last_point.x, left_end_y + root_last_point.y)
#     sd.line(start_point, left_last_point, width=2)
#
#     right_angle = angle - variation
#     right_radian = (right_angle * math.pi) / 180
#     right_end_y = math.sin(right_radian) * length
#     right_end_x = math.cos(right_radian) * length
#     right_last_point = sd.get_point(right_end_x + root_last_point.x, right_end_y + root_last_point.y)
#     sd.line(start_point, right_last_point, width=2)
#
#     draw_branches_v2(right_last_point.x, right_last_point.y, right_angle, variation, length * 0.75)
#     draw_branches_v2(left_last_point.x, left_last_point.y, left_angle, variation, length * 0.75)
#
#
# draw_branches_v2(500, 30, 90, 32, 90)
#
# # 3) первоначальный вызов:
# # root_point = get_point(300, 30)
# # draw_bunches(start_point=root_point, angle=90, length=100)
#
# # Пригодятся функции
# # sd.get_point()
# # sd.get_vector()
# # Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg
#
# # можно поиграть -шрифтами- цветами и углами отклонения
#
#

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
#

# Пригодятся функции
# sd.random_number()
def draw_branches_v3(start_x, start_y, angle, variation, length):
    root_start_point = sd.get_point(start_x, start_y)
    root_angle = angle
    root_radian = (root_angle * math.pi) / 180
    root_end_y = math.sin(root_radian) * length
    root_end_x = math.cos(root_radian) * length
    root_last_point = sd.get_point(root_end_x + start_x, root_end_y + start_y)
    sd.line(root_start_point, root_last_point, width=2)

    if length < 1:
        return

    start_point = sd.get_point(root_last_point.x, root_last_point.y)
    left_angle = angle + variation
    left_radian = (left_angle * math.pi) / 180
    left_end_y = math.sin(left_radian) * length
    left_end_x = math.cos(left_radian) * length
    left_last_point = sd.get_point(left_end_x + root_last_point.x, left_end_y + root_last_point.y)
    sd.line(start_point, left_last_point, width=2)

    right_angle = angle - variation
    right_radian = (right_angle * math.pi) / 180
    right_end_y = math.sin(right_radian) * length
    right_end_x = math.cos(right_radian) * length
    right_last_point = sd.get_point(right_end_x + root_last_point.x, right_end_y + root_last_point.y)
    sd.line(start_point, right_last_point, width=2)

    draw_branches_v3(right_last_point.x, right_last_point.y, right_angle, variation,
                     length * random.randrange(6,8)/10)
    draw_branches_v3(left_last_point.x, left_last_point.y, left_angle, variation, length * random.randrange(6,8)/10)


draw_branches_v3(500, 30, 90, 32, 100)

sd.pause()
