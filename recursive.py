# 재귀함수 호출.
# for i in range(1, 6):
#     print(i)
#     if i == 5:
#         print("end")
# 함수를 이용
def count_num(i):  # 첫번째 사람
    print(i)
    if i == 5:
        print("end")
        return
    count_num(i+1)


count_num(1)
