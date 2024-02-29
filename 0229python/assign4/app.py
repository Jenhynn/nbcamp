from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
import random

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

# db 설정


class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'컴퓨터: {self.computer_choice} 사용자: {self.user_choice} 결과: {self.result}'


with app.app_context():
    db.create_all()


@app.route('/')
def rockscissorspaper():
    list = ["가위✌️", "바위✊", "보✋"]
    user = request.args.get('choice')  # form에서 보낸 데이터 받기

    if user is not None:
        computer = random.choice(list)
        if computer == user:
            result = "무승부입니다!"
        elif (user == "가위✌️" and computer == "바위✊") or (user == "바위✊" and computer == "보✋") or (user == "보✋" and computer == "가위✌️"):
            result = "졌습니다"
        else:
            result = "이겼습니다!"

        # 데이터 db에 저장
        history = GameHistory(
            user_choice=user, computer_choice=computer, result=result)
        db.session.add(history)
        db.session.commit()

        context = {
            '컴퓨터': computer,
            '사용자': user,
            '결과': result
        }

    else:
        context = {
            '컴퓨터': "",
            '사용자': "가위, 바위, 보 중 하나를 선택하세요",
            '결과': ""
        }

    histories = GameHistory.query.all()

    wins = GameHistory.query.filter_by(result="이겼습니다!").count()
    losses = GameHistory.query.filter_by(result="졌습니다").count()
    ties = GameHistory.query.filter_by(result="무승부입니다!").count()

    return render_template('index.html', data=context, histories=histories, wins=wins, losses=losses, ties=ties)


@app.route('/reset', methods=['POST'])
def reset_database():
    # 데이터베이스의 기록 삭제
    db.session.query(GameHistory).delete()
    db.session.commit()
    message = "게임 기록이 삭제되었습니다."
    return redirect(url_for('rockscissorspaper', message=message))

# return render_template('index.html', data=result)


# print(f"승: {win_count}, 패: {lose_count}, 무승부: {tie_count}")
# def ask():
#     while True:
#         user_input = input("다시 하시겠습니까? y/n ")
#         if user_input.lower() == 'y':
#             user_input = input("게임을 초기화하시겠습니까? y/n ")
#             if user_input.lower() == 'y':
#                 win_count = 0
#                 lose_count = 0
#                 tie_count = 0
#             elif user_input.lower() == 'n':
#                 return True
#             else:
#                 print("y 또는 n로 입력해주십시오.")
#             return True
#         elif user_input.lower() == 'n':
#             print("게임을 종료합니다.")
#             return False
#         else:
#             print("y 또는 n로 대답해 주십시오.")
if __name__ == '__main__':
    app.run(debug=True)
