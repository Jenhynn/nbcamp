# 괄호 : 9012번
# 괄호 문자열 '(', ')' 이 올바르게 구성된 문자열 (VPS) 인지 판단하여 YES, NO 출력

# t = int(input())




# for _ in range(t):
#     ps = input()
#     left = ps.count('(')
#     right = ps.count(')')
#     print(left, right)
    # if left == right:
    #     print(left, right, 'YES')
    # else:
    #     print(left, right, 'NO')
    #개수만 같으면 안 되고 모양도 고려해야 함 ())(() 는 3 = 3 이지만 NO 가 나와야 함


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    #push, pop, is_empty
    def push(self, item):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = self.top.next
        return node.item

    def is_empty(self):
        return self.top is None


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