# 奶茶10元/杯，买3送1或买5送2，有N>=0元钱，最多可以买多少杯

money = int(input('please input the money: '))
buy_m = money // 10  #实际买的杯数
send1 = buy_m // 3  #买3送1杯数
send2 = (buy_m // 5) * 2  #买5送2杯数
if send1 < send2:  #判断送的杯数哪个最好
    send = send2
else:
    send = send1
total = buy_m + send 
print('最多买{0}杯'.format(total))