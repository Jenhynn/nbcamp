# 문자열 뒤집기
# b,d,p,q 로 이루어진 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램 작성

def mirror(list):
    result_list = []
    for i in range(len(list)):
        if list[i] == 'b':
            result_list.append('d')
        elif list[i] == 'd':
            result_list.append('b')
        elif list[i] == 'p':
            result_list.append('q')
        elif list[i] == 'q':
            result_list.append('p')
    result = ''.join(result_list[::-1])
    return result

t = int(input()) #line 1 = 총 문자열 개수 받기
# print(t)

for i in range(t):
    string = list(input())
    print(f'#{i+1}', mirror(string))


# print(num, list1, list2)

# print(mirror(list1), mirror(list2))



# for i in range(len(list1)):
#     if list1[i] == 'b':
#         result_list1.append('d')
#     elif list1[i] == 'd':
#         result_list1.append('b')
#     elif list1[i] == 'p':
#         result_list1.append('q')
#     elif list1[i] == 'q':
#         result_list1.append('p')
# result1 = ''.join(result_list1[::-1])
#
# for i in range(len(list2)):
#     if list2[i] == 'b':
#         result_list2.append('d')
#     elif list2[i] == 'd':
#         result_list2.append('b')
#     elif list2[i] == 'p':
#         result_list2.append('q')
#     elif list2[i] == 'q':
#         result_list2.append('p')
# result2 = ''.join(result_list2[::-1])

# print(result1, result2)