import math


print(5 // 2)
print(5 / 2)
print(5 % 2)

print(
    f"{math.floor(5.6)} {math.floor(1.01)}"
)  # apenas inteiro == maior inteiro menor que o número 5,0 -> 5; 4,9 -> 4
print(
    f"{math.ceil(5.9)} {math.ceil(1.0000000001)}"
)  # 6 2 # aumenta pro próximo inteiro se tiver decimal

print("+++++++++++++++++++++++++")
print(0.1 + 0.2 == 0.3)  # False
print(0.1 + 0.2)  # 0.30000000000000004
numero = 0.1 + 0.2
print(0.3 == round(numero, 1))  # True
print("+++++++++++++++++++++++++")
