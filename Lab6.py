#lab 6, task 1
C = float(input("Введите количество секунд "))
Min = int(C / 60)
Ost = C - Min * 60
print("С начала последней минуты прошло",Ost,"секунд")

#lab 6, task 2
K = int(input("Введите номер дня года(число от 1 до 365) "))
N = 7
while True :
  if K < 1 or K > 365 :
    print("Такого дня не существует!")
    K = int(input("Введите номер дня года(число от 1 до 365) "))
  else :
    break
R = int(K / N)
Ost = K - R * 7
print("Номер дня недели равен",Ost)

#lab 6, task 3
K = int(input("Введите номер дня года(число от 1 до 365) "))
N = int(input("Введите номер дня недели(число от 1 до 7) "))
while True :
  if (K < 1 or K > 365) :
    print("Такого дня не существует!")
    K = int(input("Введите номер дня года(число от 1 до 365) "))
  elif (N < 1 or N > 7) :
    print("Такого дня недели не существует!")
    N = int(input("Введите номер дня недели(число от 1 до 7) "))
  else :
    break
ost1 = 7 - N
R = int(K / 7)
Ost = K - (R * 7 + ost1)
print("Номер дня недели равен",Ost)

#lab 6, task 4
A = float(input("Введите сторону прямоугольника "))
B = float(input("Введите другую сторону прямоугольника "))
C = float(input("Введите сторону квадрата "))
Sp = A * B
Sk = C * C
R = int(Sp / Sk)
if Sk > Sp :
  print("Квадрат больше прямоугольника")
else :
  print("Количество квадратов в прямоугольнике равно",R)

#lab 6, task 5
Year = int(input("Введите номер года(целое положительное число) "))
N = 100
while True :
  if Year <= 0 :
    Year = int(input("Введите номер года(целое положительное число) "))
  else :
    break
St = int(Year / N)
St1 = Year / 100
St2 = Year // 100
if St1 == St2 :
  print(St,"столетие")
else :
  print(St + 1,"столетие")
