def hitung_FPB(x, y):

    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0)) and (y % i == 0):
            fpb = i
    return fpb

num1 = int(input("Masukkan bilangan : "))
num2 = int(input("Masukkan bilangan : "))

print("FPB dari ", num1, "dan", num2, "=", hitung_FPB(num1, num2))
