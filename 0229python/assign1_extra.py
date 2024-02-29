# 1. Up Down 게임 만들기 !
# -> 컴퓨터가 생각한 숫자를 맞추는 게임으로, 플레이어는 숫자를 입력하고 컴퓨터가 생각한 숫자와 비교하여 up&down 힌트를 받아가며 숫자를 맞추는 게임
# 내용:
#     1. 플레이어와 컴퓨터가 참여하는 업다운 게임을
#     2. 프로그램은 다음과 같은 기능을 포함해야
#     - 컴퓨터는 1~100 사이의 랜덤한 숫자를 생성합니다
#     - 플레이어는 숫자를 입력하고, 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공합니다
#     - 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줍니다
#     - 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다

# +추가 도전 과제
#     1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력해 유효한 범위 내의 숫자를 입력하도록 유도
#     2. 플레이어가 게임을 반복하고 싶을 경우 게임 재시작 여부를 묻고 그에 따라 게임을 초기화 또는 종료하는 기능 추가
#     3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고 다음 게임에서 표시하는 기능 구현



import random
import pickle


def guess_number ():
    random_number = random.randint(1, 100)
    print(random_number)
    count = 0
    with open("test.pickle", "rb") as f:
        max_count = pickle.load(f)
    print("이전 플레이어 최고 시도 횟수: "+ str(max_count))

    while True:
        number = int(input("1에서 100 사이의 숫자를 입력하세요: "))
        if number > 100 or number == 0:
            print("유효한 숫자를 입력하세요.")
        elif number > random_number:
            print("DOWN")
            count += 1
        elif number < random_number:
            print("UP")
            count += 1
        else:
            print("정답입니다!")
            count += 1
            break

    print(f"시도한 횟수: {count}번")

    if count >= max_count:
        max_count = count
    else:
        max_count = max_count

    print(f"최고 시도 횟수: {max_count}")
    with open("test.pickle", "wb") as f:
        pickle.dump(max_count, f)


guess_number()

while True:
    user_input = input("게임을 다시 하시겠습니까? y/n")
    if user_input.lower() == 'y': #lower()붙여서 대문자를 입력해도 받아들이기
        guess_number()
    elif user_input.lower() == 'n':
        print("게임을 종료합니다.")
        break
    else:
        print("y 또는 n로 대답해 주십시오.")



# 시도 횟수를 제한할 때 (7번)
# def guess_number ():
#     random_number = random.randint(1, 100)
#     print(random_number)
#
#     for number in range(1, 6):
#         number = int(input("1에서 100 사이의 숫자를 입력하세요: "))
#
#         if number == random_number:
#             print("정답입니다!")
#             break
#         elif number < random_number:
#             print("UP")
#         else:
#             print("DOWN")
#
# guess_number()


#
# #시도한 횟수 설정하는 것
#
# count = 0
# for num in num_list:
#     if number: #한 번 함수를 통과하면
#         count += 1
#
# print(count)
#
# #while, for loop 반복문
#
# while number > random_number:
#     print("Down")
#     #새로운 숫자를 입력하세요
#     if number == random_number:
#         print("정답입니다!")
#

#while 문에 대해서 더 공부해보기

