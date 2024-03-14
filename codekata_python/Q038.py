# 옷가게 할인받기
# 10만원 이상 사면 5%, 30만원 이상 사면 10%, 50만원 이상 사면 20% 할인
# price 가 주어질 때 지불해야 할 금액을 정수로 return 하도록


def solution(price):
    if price >= 500000:
        price = 0.8 * price
    elif price >= 300000:
        price = 0.9 * price
    elif price >= 100000:
        price = 0.95 * price
    else:
        pass
    return int(price)


#다른 사람 풀이 참고: dictionary 이용
def solution2(price):
    discount_rates = {500000:0.8, 300000:0.9, 100000:0.95}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(discount_rate * price)


print(solution(150000))
print(solution(580000))