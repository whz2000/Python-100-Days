a = 10
b = 3
a += b  # a = 13
a *= a+2    # 13 * 15
print(a)

# 华氏温度转摄氏温度
f = float(input('请输入华氏温度：'))
t = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {t:.1f}摄氏度')


# 输入圆的半径，计算圆的周长和面积
f = float(input('请输入圆的半径: '))
circumference = f * 2 * 3.14
area = 3.14 * f ** 2
print(f'圆的周长为：{circumference:.1f}, 面积为：{area:.1f}')


# 输入年份判断是否是闰年
year = int(input('请输入年份: '))
a = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(a)

