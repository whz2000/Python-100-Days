# 英寸和厘米互换
length = float(input("请输入长度："))
unit = str(input("请输入单位："))
if unit == 'in' or unit == '英寸':
    print(f'{length: .2f}英寸等于{length * 2.54: .2f}厘米')
elif unit == 'cm' or unit == '厘米':
    print(f'{length: .2f}厘米等于{length * 0.3937: .2f}英寸')
else:
    print('请输入有效的单位')

# 百分制成绩转换为等级制成绩
score = int(input('请输入分数：'))
if 90 <= score <= 100:
    print(f'{score}对应的等级为A')
elif 80 <= score < 90:
    print(f'{score}对应的等级为B')
elif 70 <= score < 80:
    print(f'{score}对应的等级为C')
elif 60 <= score < 70:
    print(f'{score}对应的等级为D')
elif 0 <= score < 60:
    print(f'{score}对应的等级为E')
else:
    print('请输入合法的分数')

# 输入三条边长，如果能构成三角形就计算周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a and a - b < c and abs(a - b) < c and abs(a - c) < b and abs(b - c) < a:
    circumference = a + b + c
    print(f'三角形的周长为：{circumference: .2f}')
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'三角形的面积为：{s: .2f}')
else:
    print('不能构成三角形')








