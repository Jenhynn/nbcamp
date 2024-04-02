

from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'commentdb.db')

db = SQLAlchemy(app)

# # 게시글 db 설정

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False)
#     title = db.Column(db.String, nullable=False)
#     contents = db.Column(db.String, nullable=False)

#     # 데이터 표시
#     def __repr__(self):
#         return f'{self.title} {self.contents} {self.username}'

# 댓글 db 설정


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    contents = db.Column(db.String, nullable=False)

    # 데이터 표시
    def __repr__(self):
        return f'{self.username}: {self.contents}'


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    comment_list = Comment.query.all()
    return render_template("test.html", data=comment_list)


# @app.route("/write")
# def post_create():
#     # 글쓰기 데이터
#     username_receive = request.args.get("username")
#     title_receive = request.args.get("title")
#     contents_receive = request.args.get("contents")

#     # 데이터 db에 저장
#     post = Post(username=username_receive,
#                 title=title_receive, contents=contents_receive)
#     db.session.add(post)
#     db.session.commit()
#     return redirect(url_for(''))

@app.route("/test")
def write_comment():
    # 데이터 받아오기
    username_comment = request.args.get("username")
    contents_comment = request.args.get("contents")

    # 데이터 db에 저장
    comment = Comment(username=username_comment, contents=contents_comment)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('home'))


# @app.route("/test/edit", methods=['PUT'])
# def edit_comment():
#     contents = request.form.get("contents")
#     comment = Comment.query.filter_by(contents=contents).first()
#     comment.username = 'new_username'
#     comment.contents = 'new_contents'
#     db.session.commit()

@app.route("/test/edit", methods=['POST'])
def edit_comment():
    updated_username = request.form.get("new_username")
    updated_contents = request.form.get("new_contents")
    original_contents = request.form.get("contents")

    comment = Comment.query.filter_by(contents=original_contents).first()

    if comment:
        comment.username = updated_username
        comment.contents = updated_contents
        db.session.commit()
        message = "댓글이 수정되었습니다."
    return redirect(url_for('home', message=message))


@app.route("/test/delete", methods=['POST'])
def delete_comment():
    contents = request.form.get("contents")
    comment = Comment.query.filter_by(contents=contents).first()
    if comment:
        db.session.delete(comment)
        db.session.commit()
    message = "댓글이 삭제되었습니다."
    return redirect(url_for('home', message=message))


if __name__ == "__main__":
    app.run(debug=True)
