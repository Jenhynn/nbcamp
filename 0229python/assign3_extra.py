# 3.클래스 사용해보기
# 내용
#     1. Member 클래스와 Post 클래스 정의하기
#     2. Member 클래스에는 회원 이름 (name), 회원 아이디 (username), 비밀번호(password) 속성을 가지고 있어야 함
#     3. Member 클래스에는 display 메소드가 있어야 함 - 회원 이름과 아이디를 print 해주는 메소드
#     4. Post 클래스에는 게시물 제목(title), 게시물 내용 (content), 작성자(author-username 저장) 속성을 가지고 있어야 함
#     5. 회원 인스턴스 세 개 이상, members 라는 빈 리스트에 append로 저장 & 리스트 돌면서 회원들 이름 프린트
#     6. 각각의 회원이 게시글을 세 개 이상 작성하는 코드 (총 9개 이상) 게시글 인스턴스는 post 라는 빈리스트에 append로 저장
#         - for 문을 돌면서 특정 유저가 작성한 게시글 제목 모두 프린트
#         - for 문을 돌면서 특정 단어가 content에 포함된 게시글 제목 모두

# +추가 과제
#     1. 사용자가 터미널에서 input을 이용하여 Member 인스턴스 만들 수 있게
#     2. post 도 터미널에서 생성할 수 있게
#     3. (심화) 비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장


import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(self.name, self.username)

    # TODO: 비밀번호 해시화 저장
    def hash_password(self):
        # print(self.password)
        hashed = hashlib.sha256()
        hashed.update(self.password.encode('utf-8'))
        self.hashed_password = hashed.hexdigest()
        print("해시화된 비밀번호: ", self.hashed_password)
        return self.hashed_password


class Post:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        # print(self.title, author, self.content)

    def save_post(self, posts):
        posts.append(self)


# ----- 코드 실행 ------
members = []
posts = []
js_titles = []
post = []

m1 = Member("John", "JohnSmith", "js1234")
m2 = Member("Alice", "AliceAppleseed", "alicepassword")
m3 = Member("Robert", "RobertParrot", "passwordbob")

m1.display()
m1.hash_password()
m2.display()
m2.hash_password()
m3.display()
m3.hash_password()

p1 = Post("제목", "JohnSmith", "너무")
p2 = Post("제목2","JohnSmith","나무")
p3 = Post("제목3", "JohnSmith", "진짜")

q1 = Post("제목4","AliceAppleseed","너무 너무")
q2 = Post("제목5","AliceAppleseed","이건 없음")
q3 = Post("제목6","AliceAppleseed","너무너무너무")

r1 = Post("제목7", "RobertParrot", "안 너무")
r2 = Post("제목8", "RobertParrot", "정말")
r3 = Post("제목9", "RobertParrot", "정말정말")


p1.save_post(posts)
p2.save_post(posts)
p3.save_post(posts)

q1.save_post(posts)
q2.save_post(posts)
q3.save_post(posts)

r1.save_post(posts)
r2.save_post(posts)
r3.save_post(posts)

filter_author = m1

#TODO ----특정 유저가 작성한 제목 프린트----

print("Posts by: ", filter_author.name)
for i in posts:
    if i.author == "JohnSmith":
        members.append(i.title)

print(members)


# TODO ----특정 키워드가 내용에 포함된 제목 프린트----

filter_keyword = "너무"

print("다음 키워드를 포함하는 제목: ", filter_keyword)
for i in posts:
    if "너무" in i.content:
        post.append(i.title)

print(post)


# TODO: 추가 과제
# Member 인스턴스 추가

input_name = str(input("회원이름을 입력하세요: "))
input_username = str(input("닉네임을 입력하세요: "))
input_password = str(input("비밀번호를 입력하세요: "))

print([input_name, input_username, input_password])

m_new = Member(input_name, input_username, input_password)
m_new.display()

# Post 인스턴스 추가
input_title = str(input("제목: "))
input_author = str(input("작성자: "))
input_content = str(input("내용: "))

print([input_title, input_author, input_content])

p_new = Post(input_title, input_author, input_content)

print(post)
