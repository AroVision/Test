# import turtle
# import random
#
# ekran = turtle.Screen()
# zolw = turtle.Turtle()
#
# def draw():
#     zolw.penup()
#     kolor_wypelnienia = (0.1, 0.0, 0.9)
#     zolw.fillcolor(kolor_wypelnienia)
#     zolw.begin_fill()
#     for _ in range(4):
#         zolw.forward(100)
#         zolw.left(90)
#     zolw.end_fill()
#     zolw.penup()
#
#
# for _ in range(1000):
#     zolw.hideturtle()
#     zolw.speed(1000)
#     zolw.penup()
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     zolw.goto(x, y)
#     zolw.pendown()
#     draw()
#     zolw.penup()
#
# ekran.exitonclick()
# import turtle

#
# import turtle
# t = turtle.Turtle
# turtle.pensize(5)
# turtle.hideturtle()
# turtle.pendown()
# turtle.pencolor('black')
# turtle.forward(100)
# turtle.right(144)
# for t in range(4):
#     turtle.forward(100)
#     turtle.right(75)

# import turtle
#
# t = turtle.Turtle()
# turtle.bgcolor('black')
#
# t.pencolor("red")
# t.right(75)
# t.forward(100)
#
# for i in range(4):
#     t.pencolor("red")
#     t.right(144)
#     t.forward(100)
#
# turtle.done()







# import turtle
# t = turtle.Turtle()
# turtle.bgcolor('black')
# t.speed(1)
# for i in range(2):
#     t.pencolor("red")
#     t.forward(100)
#     t.left(60)
#     t.forward(50)
#     t.left(120)



# t = turtle.Turtle
# turtle.fillcolor('black')
# turtle.bgcolor('yellow')
# turtle.speed(3)
# turtle.pensize(5)
# turtle.pencolor('blue')
# turtle.pendown()
# for t in range(6):
#     turtle.forward(100)
#     turtle.right(60)
# turtle.begin_fill()
# turtle.circle(50)
# turtle.end_fill()
# turtle.done()
# turtle.exitonclick()

# 100, 75 50*
# import turtle
# turtle.hideturtle()
# turtle.goto(0, -300)
# turtle.bgcolor('cyan')
# turtle.speed(5)
# turtle.pensize(5)
# turtle.pencolor('white')
# turtle.fillcolor('white')
# turtle.pendown()
# turtle.begin_fill()
# turtle.circle(100)
# turtle.goto(0, -100)
# turtle.circle(60)
# turtle.goto(0, 20)
# turtle.circle(40)
# turtle.end_fill()
# turtle.exitonclick()
#
# import turtle
# turtle.pencolor("Red")
# t = turtle
# turtle.right(90)
# for t in range(2):
#     turtle.forward(50)
#     turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(80)
# turtle.left(130)
# turtle.forward(80)
# turtle.right(130)
# turtle.forward(30)
# turtle.left(130)
# turtle.forward(100)
# turtle.right(130)
# turtle.forward(30)
# turtle.left(130)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(100)
#
# import turtle
#
# screen = turtle.Screen()
#
# screen.setup(800, 600)
#
# circle = turtle.Turtle()
#
# circle.shape('circle')
#
# circle.color('red')
#
# circle.speed('fastest')
#
# circle.up()
#
# square = turtle.Turtle()
#
# square.shape('square')
#
# square.color('green')
#
# square.speed('fastest')
#
# square.up()
#
# circle.goto(0, 280)
#
# circle.stamp()
#
# k = 0
#
# for i in range(1, 17):
#
#    y = 30 * i
#
#    for j in range(i - k):
#
#        x = 30 * j
#
#        square.goto(x, -y + 280)
#
#        square.stamp()
#
#        square.goto(-x, -y + 280)
#
#        square.stamp()
#
#    if i % 4 == 0:
#
#        x = 30 * (j + 1)
#
#        circle.color('red')
#
#        circle.goto(-x, -y + 280)
#
#        circle.stamp()
#
#        circle.goto(x, -y + 280)
#
#        circle.stamp()
#
#        k += 2
#
#    if i % 4 == 3:
#
#        x = 30 * (j + 1)
#
#        circle.color('yellow')
#
#        circle.goto(-x, -y + 280)
#
#        circle.stamp()
#
#        circle.goto(x, -y + 280)
#
#        circle.stamp()
#
# square.color('brown')
#
# for i in range(17, 20):
#
#    y = 30 * i
#
#    for j in range(3):
#
#        x = 30 * j
#
#        square.goto(x, -y + 280)
#
#        square.stamp()
#
#        square.goto(-x, -y + 280)
#
#        square.stamp()
#
# turtle.exitonclick()
#
#
#
# import turtle
#
# # Utwórz okno graficzne
# okno = turtle.Screen()
# okno.bgcolor("lightblue")
#
# # Utwórz dwa obiekty Turtle
# zolw1 = turtle.Turtle()
# zolw2 = turtle.Turtle()
#
# # Ustaw parametry pierwszego żółwia
# zolw1.color("blue")
# zolw1.shape("turtle")
# zolw1.speed(1)
#
# # Ustaw parametry drugiego żółwia
# zolw2.color("red")
# zolw2.shape("triangle")
# zolw2.speed(1)
#
# # Żółw 1 rysuje kwadrat
# for _ in range(4):
#     zolw1.forward(100)
#     zolw1.left(90)
#
# # Przesuń żółwia 2 na nową pozycję
# zolw2.penup()
# zolw2.goto(-50, -50)
# zolw2.pendown()
#
# # Żółw 2 rysuje trójkąt
# for _ in range(3):
#     zolw2.forward(100)
#     zolw2.left(120)
#
# # Zamknij okno po kliknięciu
# okno.exitonclick()

# "15 Listopada 2023"
# import turtle
# t = turtle


# "1. Kwadrat"
# # for t in range(4):
# #     turtle.forward(50)
# #     turtle.left(90)
# # turtle.exitonclick()
#
# # "2. Koło"
# # # turtle.begin_fill()
# # # turtle.fillcolor("Red")
# # # turtle.circle(60)
# # # turtle.end_fill()
# # # turtle.penup()
# # # turtle.goto(70, 150)
# # # turtle.pendown()
# # # turtle.circle(100)
# # # turtle.exitonclick()
# #
# # "3. Kwiat"
# # # import turtle
# # # wn = turtle.Screen()
# # # wn.bgcolor('blue')
# # # Albert = turtle.Turtle()
# # # Albert.speed(0)
# # # Albert.color('white')
# # # rotate=int(360)
# # # def drawCircles(t,size):
# # #     for i in range(100000000):
# # #         t.circle(size)
# # #         size=size-4
# # # def drawSpecial(t,size,repeat):
# # #   for i in range (repeat):
# # #     drawCircles(t,size)
# # #     t.right(360/repeat)
# # # drawSpecial(Albert,100,10)
# # # Steve = turtle.Turtle()
# # # Steve.speed(0)
# # # Steve.color('yellow')
# # # rotate=int(90)
# # # def drawCircles(t,size):
# # #     for i in range(4):
# # #         t.circle(size)
# # #         size=size-10
# # # def drawSpecial(t,size,repeat):
# # #     for i in range (repeat):
# # #         drawCircles(t,size)
# # #         t.right(360/repeat)
# # # drawSpecial(Steve,100,10)
# # # Barry = turtle.Turtle()
# # # Barry.speed(0)
# # # Barry.color('blue')
# # # rotate=int(80)
# # # def drawCircles(t,size):
# # #     for i in range(4):
# # #         t.circle(size)
# # #         size=size-5
# # # def drawSpecial(t,size,repeat):
# # #     for i in range (repeat):
# # #         drawCircles(t,size)
# # #         t.right(360/repeat)
# # # drawSpecial(Barry,100,10)
# # # Terry = turtle.Turtle()
# # # Terry.speed(0)
# # # Terry.color('orange')
# # # rotate=int(90)
# # # def drawCircles(t,size):
# # #     for i in range(4):
# # #         t.circle(size)
# # #         size=size-19
# # # def drawSpecial(t,size,repeat):
# # #     for i in range (repeat):
# # #         drawCircles(t,size)
# # #         t.right(360/repeat)
# # # drawSpecial(Terry,100,10)
# # # Will = turtle.Turtle()
# # # Will.speed(0)
# # # Will.color('pink')
# # # rotate=int(90)
# # # def drawCircles(t,size):
# # #     for i in range(4):
# # #         t.circle(size)
# # #         size=size-20
# # # def drawSpecial(t,size,repeat):
# # #     for i in range (repeat):
# # #         drawCircles(t,size)
# # #         t.right(360/repeat)
# # # drawSpecial(Will,100,10)
# # #
# # # turtle.done()
# #
# # "4. Drzewo binarne"
# # # from turtle import *
# # #
# # # def draw_branch(branch_length):
# # #     if branch_length > 5:
# # #         forward(branch_length)
# # #         right(20)
# # #         draw_branch(branch_length - 15)
# # #         left(40)
# # #         draw_branch(branch_length - 15)
# # #         right(20)
# # #         backward(branch_length)
# # #
# # # speed("fastest")
# # # left(90)
# # # draw_branch(80)
# # #
# # # done()
# #
# # "5. Znak olimpijski"
# # tp = turtle.pendown()
# # turtle.pensize(5)
# # turtle.pencolor("Blue")
# # turtle.circle(50)
# # turtle.pencolor("Black")
# # turtle.penup()
# # turtle.goto(120, 0)
# # turtle.pendown()
# # turtle.circle(50)
# # turtle.pencolor("Red")
# # turtle.goto(240, 0)
# # turtle.circle(50)
# # turtle.goto(0,200)
# # turtle.circle(50)
#
#
# # # IST = int(input("Insert Number \n"))
# # # if IST % 2 == 0:
# # #     print("Your number is even")
# # # else:
# # #     print("Your number is odd")
# # NUM = input("Insert more than 1 number. \n")
# # LIST = []
# # LIST.append(NUM)
# # NUM = float(NUM)
# # SUM = sum(LIST)
# # AVG = SUM / len(LIST)
# # print("The average of your numbers in your list is", AVG, ".")
# #
# #
# # # list = []
# # # liczba = input("Podaj liczbę")
# # # list.append(liczba)
#
# # def srednia_uzytkownika():
# #     lista = []
# #     while True:
# #         liczba = input("Podaj liczbę (lub wpisz 'koniec' aby zakończyć): ")
# #         if liczba.lower() == 'koniec':
# #             break
# #         try:
# #             liczba = float(liczba)
# #             lista.append(liczba)
# #         except ValueError:
# #             print("To nie jest liczba. Podaj liczbę lub wpisz 'koniec'.")
# #
# #     if not lista:
# #         return 0
# #     return sum(lista) / len(lista)
# #
# # # Obliczanie średniej wartości dla listy wprowadzonej przez użytkownika
# # wynik = srednia_uzytkownika()
# # print("Średnia wartość:", wynik)
# # def Pairs()
# #
# # Pairs = [('a', 1), ('b', 2), ('c', 3)]
# # NOTEBOOK = {Pairs}
# # print(NOTEBOOK)
#
# # def lista_na_slownik(pary):
# #     return dict(pary)
# #
# # # Przykładowe użycie:
# # pary = [('a', 1), ('b', 2), ('c', 3)]
# # wynik = lista_na_slownik(pary)
# # print(wynik)
#
#
# #
# # NUM = int(input("Insert a number. \n"))
# # if NUM < 0:
# #     print("Your number is negative.")
# # elif NUM >= 0:
# #     print("Your number is not negative")
#
#
#
#
#
# # SNTC = input("Write something \n")
# # RSNTC = SNTC[::-1]
# # print("Your sentence spelled backwards:", RSNTC)
#
#
# # print("Calculator")
# # def Calculator():
# #     NUM1 = float(input("Choose a Number \n"))
# #     NUM2 = float(input("Now choose a second Number \n"))
# #     Choice = input("Choose: Add or Substract? \n")
# #     if Choice == "Add":
# #         print("Your Summary is:", NUM1 + NUM2)
# #     elif Choice == "Substract":
# #         print("Your substraction is:", NUM1 - NUM2)
# #     else:
# #       print("Sorry, there is no such command like that.")
# # Calculator()

# from Tests import *      # importowoanie pliku stworzonego przez nas (a właściwie dwóch funkcji z niego)
#
# num1 = 10.9
# num2 = 5.0
#
# result_add = add(num1, num2)
# result_substract = substract(num1, num2)
#
# result_multi = multi(num1, num2)
# result_div = div(num1, num2)
#
# print(f"dodawanie: {result_add}")
# print(f"odejmowanie: {result_substract}")
# print(f"multi: {result_multi}")
# print(f"dzielenie: {result_div}")
# c = result_multi2
# print(c)
from ACV import *