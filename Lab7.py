#lab 7, task 1
A = float(input("Введите число A "))
B = float(input("Введите число B "))
C1 = bool(A > 2)
C2 = bool(B <= 3)
print("Неравенство (A > 2):",C1)
print("Неравенство (B <= 3):",C2)

#lab 7, task 2
A = float(input("Введите число A "))
B = float(input("Введите число B "))
C = float(input("Введите число С "))
Ist = bool(A < B < C)
print("Двойное неравенство A < B < C:",Ist)

#lab 7, task 3
A = float(input("Введите число A "))
if (9 < A < 100) and (A % 2 == 0) :
  print("Число А является чётным двузначным: True")
else :
  print("Число А является чётным двузначным: False")

#lab 7, task 4
A = float(input("Введите трёхзначное число A "))
while (A < 100) and (A > 999) :
  print("Это не трехзначное число!")
  A = float(input("Введите трёхзначное число A "))
Ist = bool((A // 100) < ((A // 10) % 10) < (A % 10) or (A % 10) < ((A // 10) % 10) < (A // 100))
print(Ist)

#lab 7, task 5
A = float(input("Введите четырёхзначное число A "))
while True :
  if (A < 1000 or A > 9999) :
    print("Это не четырёхзначное число!")
    A = float(input("Введите четырёхзначное число A "))
  else :
    break
Ist = bool(A % 100 == A // 100)
print("Это четырёхзначное число можно прочитать одинаково в обе стороны:",Ist)
  
#lab 7, task 6
a = float(input("Введите число "))
b = float(input("Введите число "))
c = float(input("Введите число "))
Ist = bool(a**2 + b**2 == c**2)
print("Треугольник со сторонами a, b, c прямоугольный:",Ist)

#lab 7, task 7
a = float(input("Введите число "))
b = float(input("Введите число "))
c = float(input("Введите число "))
Ist = bool(a + b >= c)
print("Треугольник со сторонами a, b, с существует:",Ist)
