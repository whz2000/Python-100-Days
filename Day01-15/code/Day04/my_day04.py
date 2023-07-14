# 输入一个正整数判断它是不是素数
# number = int(input("请输入一个正整数"))
# for i in range(2, number):
#     if number % i == 0:
#         print("这个数字不是素数")
#         break
#     elif i == number - 1:
#         print("这个数字是素数")
#     else:
#         continue

# 练习2：输入两个正整数，计算它们的最大公约数和最小公倍数
# num1 = int(input("请输入一个正整数"))
# num2 = int(input("请输入一个正整数"))
# maxNum = max(num1, num2)
# minNum = min(num1, num2)
# a = 1
# for i in range(1, minNum + 1):
#     if num1 % i ==0 and num2 % i == 0:
#         a = i
# print(f'最大公约数为：{a}')
# for j in range(maxNum, num1 * num2 + 1):
#     if j % num1 == 0 and j % num2 == 0:
#         b = j
#         print(f'最小公倍数为: {b}')
#         break

# 打印三角形图案
# for i in range(1, 6):
#     print('*' * i)
#
# print()
#
# for i in range(5, 0, -1):
#     print('*' * i)
#
# print()
#
# for i in range(1, 6):
#     print(' ' * (5 - i) + '*' * (2 * i - 1) + ' ' * (5 - i))
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()
