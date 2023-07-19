# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

for n in range(100, 1000):
    num_list = list(str(n))
    result = 0
    for i in num_list:
        result = result + int(i) ** 3
    if result == n:
        print(f'{n}')

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# 将12345变成54321
# // 整除，舍弃小数部分
n1 = 12345 // 10000
n2 = 12345 // 1000 % 10
n3 = 12345 // 100 % 10
n4 = 12345 // 10 % 10
n5 = 12345 % 10
n = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(n)

# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

# 说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for i in range(0, 20):
    for m in range(0, 33):
        for n in range(3, 100, 3):
            if (i * 5) + (m * 3) + (n / 3) == 100 and i + m + n == 100:
                print(f'公鸡{i}只，母鸡{m}只，小鸡{n}只')

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

# 说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
# 玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
from random import randint

first_num = randint(1, 6) + randint(1, 6)
if first_num == 7 or first_num == 11:
    print(f'玩家摇出了{first_num}，玩家胜')
elif first_num == 2 or first_num == 3 or first_num == 12:
    print(f'玩家摇出了{first_num}，庄家胜')
else:
    while True:
        random_num = randint(1, 6) + randint(1, 6)
        if random_num == 7:
            print(f'不是第一次，玩家摇出了{random_num}，庄家胜')
            break
        elif random_num == first_num:
            print(f'第一次摇出的数字为{first_num}，玩家摇出了{random_num}，玩家胜')
            break

# 生成斐波那契数列的前20个数。
fib_list = [1, 1]
for i in range(2, 20):
    fib_list.append(fib_list[i - 1] + fib_list[i - 2])
print(fib_list)

# a = 0
# b = 1
# for _ in range(20):
#     a, b = b, a + b
#     print(a, end=' ')

# 找出10000以内的完美数
for i in range(1, 10000):
    result = 0
    for j in range(1, i):
        if i % j == 0:
            result += j
    if result == i:
        print(i)

# 输出100以内所有的素数
for i in range(2, 100):
    if i == 2:
        print(i, end=' ')
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:
            print(i, end=' ')
