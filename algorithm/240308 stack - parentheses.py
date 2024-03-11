# 괄호 : 9012번
# 괄호 문자열 '(', ')' 이 올바르게 구성된 문자열 (VPS) 인지 판단하여 YES, NO 출력

# Stack
# 여는 괄호가 나오면 push
# 닫는 괄호가 나오면 pop
# 끝까지 반복했을 때 스택이 비어 있어야 함


t = int(input())
# class 없이 풀어보자

for _ in range(t):
    string = input()
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                print(stack)
                stack.pop()
            else:
                print('NO')
                print(stack)
                break


















class Stack:
    def __init__(self):
        self.stacklist = []

    def push(self, item):
        self.stacklist.append(item)

    def pop(self):
        return self.stacklist.pop()

    def top(self):
        return self.stacklist[-1] # return 맞아?

    def is_empty(self):
        len(self.stacklist)







# print(stack)




# def parentheses(s):
#     pair = {')': '('}
#     open = '('
#     stack = []
#
#     for char in s:
#         if char in open:
#             stack.append(char)
#         else:
#             if not stack:
#                 return 'No'
#             top = stack.pop()
#             if pair[top] != top:
#                 return 'No'
#
#     return not stack
#
# print(parentheses('())(()'))
# print(parentheses('(()())((()))'))
