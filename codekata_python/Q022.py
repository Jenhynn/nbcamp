#아이스 아메리카노
#한 잔에 5500원. money로 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 배열에 넣기

def solution(money):
    money = int(money)
    cups = money // 5500
    change = money % 5500
    answer = [cups, change]
    return answer

print(solution(15000))