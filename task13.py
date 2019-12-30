n = int(input("Введите число: "))
print("Ответ:")
print([i**2 for i in range(1,x+1) if i**2 <= n])