#lab 4, task 1
a = float(input("Введите угол а в градусах "))
R = 0
R = a * (3.14 / 180)
print("Угол а в радианах равен",R)

#lab 4, task 2
a = float(input("Введите угол а в радианах "))
D = 0
D = a * 180 / 3.14
print("Угол а в градусах равен",D)

#lab 4, task 3
X = float(input("Введите к-во кг конфет "))
A = float(input("Введите стоимость Х кг конфет "))
Y = float(input("Введите другое к-во кг конфет "))
kg = 0
kg = A / X
StoimY = kg * Y
print("Стоимость 1ого кг конфет равна",kg)
print("Стоимость",Y,"кг конфет равна",StoimY)

#lab 4, task 4
V1 = float(input("Введите скорость 1ого автомобиля "))
V2 = float(input("Введите скорость 2ого автомобиля "))
S = float(input("Введите начальное расстояние между автомобилями "))
T = float(input("Введите к-во часов в пути "))
print("Конечное расстояние равно",S + V1*T + V2*T)

#lab 4, task 5
A = float(input("Введите число, не равное 0 "))
B = float(input("Введите число "))
while True :
  if A == 0 :
    print("Коэффициент А не может быть равен 0")
    A = float(input("Введите число, не равное 0 "))
  else :
    break
x = - (B / A)
print("Корень уравнения равен",x)

#lab 4, task 6
A1 = float(input("Введите число "))
B1 = float(input("Введите число "))
C1 = float(input("Введите число "))
A2 = float(input("Введите число "))
B2 = float(input("Введите число "))
C2 = float(input("Введите число "))
x = 0
y = 0
y = (C2*A1 - A2*C1) / (B2*A1 - A2*B1)
x = (C1 - B1*y) / A1
print("Решение системы","(",x,",",y,")")

