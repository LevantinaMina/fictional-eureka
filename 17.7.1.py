#17.7.1 ПРОГРАММА, КОТОРАЯ СЧИТАЕТ ПРОИЗВЕДЕНИЕ ВСЕХ НЕЧЕТНЫХ ЧИСЕЛ ОТ 1 ДО 10
multipl = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    multipl *= i
print(multipl)