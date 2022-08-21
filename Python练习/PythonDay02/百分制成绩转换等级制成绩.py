# def Score_Conversion():
#     Score = float(input("请输入分数:\n"))
#     if Score >= 90:
#         print("此分数为A级")
#     elif Score >= 80 and Score > 90:
#         print("此分数为B级")
#     elif Score >=70 and Score > 80:
#         print("此分数为C级")
#     elif Score >=60 and Score > 70:
#         print("此分数为D级")
#     else:
#         print("此分数为E级")

# 优化版😊√
def Score_Conversion():
    Score = float(input("请输入分数:\n"))
    if Score >= 90:
        grade = "A"
    elif Score >= 80 and Score > 90:
        grade = "B"
    elif Score >=70 and Score > 80:
        grade = "C"
    elif Score >=60 and Score > 70:
        grade = "D"
    else:
        grade = "E"
    print("此分数的等级是:" + grade + "级")
Score_Conversion()