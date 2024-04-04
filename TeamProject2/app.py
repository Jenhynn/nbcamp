

from flask import Flask, render_template, request, redirect, url_for, jsonify
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
    if comment_list:
        username = comment_list[0].username
    else:
        username = None
    return render_template("test.html", data=comment_list, username=username)

# @app.route("/")
# def home():
#     try:
#         comment_list = Comment.query.all()
#         print(comment_list)  # Check the contents of comment_list in the console
#         return render_template("test.html", data=comment_list)
#     except Exception as e:
#         print(f"Error fetching comments: {e}")
#         return "Error fetching comments"


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

# 댓글 작성
@app.route("/comments/create", methods=['GET', 'POST'])
def write_comment():
    # 데이터 받아오기
    username_comment = request.form.get("username")
    contents_comment = request.form.get("contents")

    if request.method == 'POST':
        if Comment.query.filter_by(username=username_comment).first():
            comment = Comment.query.filter_by(
                username=username_comment).first()
        else:
            new_comment = Comment(username=username_comment,
                                  contents=contents_comment)
            db.session.add(new_comment)
        db.session.commit()
    return redirect(url_for('home'))


# # 댓글 조회
# @app.route("/comments", methods=['GET'])
# def get_comments():
#     comments = Comment.query.all()
#     return jsonify([{'id': comments.id, 'username': comments.username, 'contents': comments.contents}])


# @app.route("/comments/<int:id>", methods=['GET'])
# def display_comments(id):
#     comment = Comment.query.get_or_404(id)
#     return render_template('test.html', comment=comment)

# @app.route("/test/edit", methods=['PUT'])
# def edit_comment():
#     contents = request.form.get("contents")
#     comment = Comment.query.filter_by(contents=contents).first()
#     comment.username = 'new_username'
#     comment.contents = 'new_contents'
#     db.session.commit()

# @app.route("/test/edit", methods=['POST'])
# def edit_comment():
#     original_id = request.form.get("id")
#     # updated_username = request.form.get("new_username")
#     # updated_contents = request.form.get("new_contents")
#     comment = Comment.query.filter_by(contents=original_id).first()
#     print(original_id)
#     print(comment)
#     if comment:
#         print(comment)
#         # db.session.delete(comment)
#         # comment = Comment(username=updated_username, contents=updated_contents)
#         comment.username = updated_username
#         comment.contents = updated_contents
#         # db.session.add(comment)
#         db.session.commit()

#     return redirect(url_for('home'))

@app.route("/comments/<username>/edit-modal")
def edit_comment_modal(username):
    comment = Comment.query.filter_by(username=username).first()
    if comment:
        return render_template("edit_comment.html", comment=comment)
    else:
        # Handle the case where the comment does not exist
        return "Comment not found", 404


@app.route("/comments/<username>/edit", methods=['GET', 'POST'])
def edit_comment(username):
    if request.method == 'POST':
        comment_id = request.form.get("comment_id")
        updated_username = request.form.get("new_username")
        updated_contents = request.form.get("new_contents")

        comment = Comment.query.filter_by(id=comment_id).first()
        if comment:
            # db.session.delete(comment)
            # comment = Comment(username=updated_username, contents=updated_contents)
            comment.username = updated_username
            comment.contents = updated_contents
            # db.session.add(comment)
            db.session.commit()

        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


# @app.route("/test/edit/<int:comment_id>")
# def edit_comment_modal(comment_id):
#     comment = Comment.query.get(comment_id)
#     return render_template("edit_comment.html", comment=comment)


@app.route("/comments/<username>/delete", methods=['POST'])
def delete_comment(username):
    comment = Comment.query.filter_by(username=username).first()
    if comment:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
