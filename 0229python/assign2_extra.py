# 2. 가위바위보 게임 만들기!
#     1. 플레이어와 컴퓨터가 참여하는 가위바위보 게임 만들기
#     2. 게임 순서
#         - 플레이어가 가위, 바위, 보 중 하나 임력
#         - 컴퓨터도 가위, 바위, 보 중 하나 무작위 선택
#         - 플레이어와 컴퓨터의 선택을 비교하여 승패 판정
#         - 결과를 출력하여 승리, 패배, 무승부 알림
#         - 게임을 반복하거나 종료할 수 있는 기능 추가

# +추가과제
# 1. 게임의 승,패,무승부 횟수를 기록하고, 게임 종료시에 플레이어에게 통계 제공
# 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램 개선
# 3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 게임을 초기화하거나 종료하는 기능


import random


list = ["가위", "바위", "보"]


def ask():
    while True:
        user_input = input("다시 하시겠습니까? y/n ")
        if user_input.lower() == 'y':
            user_input = input("게임을 초기화하시겠습니까? y/n ")
            if user_input.lower() == 'y':
                win_count = 0
                lose_count = 0
                tie_count = 0
            elif user_input.lower() == 'n':
                return True
            else:
                print("y 또는 n로 입력해주십시오.")
            return True
        elif user_input.lower() == 'n':
            print("게임을 종료합니다.")
            return False
        else:
            print("y 또는 n로 대답해 주십시오.")


def rockscissorspaper():
    win_count = 0
    lose_count = 0
    tie_count = 0

    while True:
        computer = random.choice(list)
        print(computer)
        user = input("가위, 바위, 보 중 하나를 입력하세요: ")
        if user not in list:
            print("다시 입력하세요.")
            continue

        if user == computer:
            print("무승부입니다!")
            tie_count += 1
        elif (user == "가위" and computer == "바위") or (user == "바위" and computer == "보") or (user == "보" and computer == "가위"):
            print("졌습니다")
            lose_count += 1
        else:
            print("이겼습니다!")
            win_count += 1

        if not ask():
            break

    print(f"승: {win_count}, 패: {lose_count}, 무승부: {tie_count}")


rockscissorspaper()

# TODO: 승/패/무승부 횟수 기록, 게임 종료시 플레이어에게 통계 제공
# win_count, lose_count, tie_count 를 설정하여 횟수 기록. ask() 함수는 마지막에 if not ask()로 한 번에 통일함

# TODO: y/n 입력시 대소문자 구분하지 않도록 개선
# user_input에 lower 함수를 적용하여 Y/N 를 입력해도 y/n 로 인식되도록 설정함.


# TODO: 재시작 여부 묻고 게임을 초기화하거나 종료하는 기능
# 다시 하겠다고 한 경우에 게임을 초기화하고 다시 하지 않는 경우에 게임을 종료함.
