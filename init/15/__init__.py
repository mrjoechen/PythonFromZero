chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))


cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0


while True:

    #输入年月日
    year = (int(input('请输入年：')))

    month = (int(input('请输入月份：')))

    day = (int(input('请输入日期：')))



    n = 0
    while zodiac_days[n] < (month, day):
        if month == 20 and day > 23 :
            break
        n += 1

    print(zodiac_name[n])

    print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))


    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1


    for each_key in zodiac_name:
        each_key_ = z_num[each_key]
        if each_key_ > 0:
            print('星座 %s 有 %s' % (each_key, each_key_))

    for each_key in chinese_zodiac:
        key_ = cz_num[each_key]
        if key_ > 0:
            print('生肖 %s 有 %s' % (each_key, key_))
