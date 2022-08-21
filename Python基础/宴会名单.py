invitation_list = ['黄林鸿', '陈柏榆', '黄智浩', '曾望', '张宇杰']
print("初始嘉宾名单:")
print(invitation_list)
invitation_letter = "我想邀请您于6月30日晚上7点于学校饭堂二楼共进晚餐。"

"""无法赴约"""
unavailable_list = "曾望"
invitation_list.remove(unavailable_list)
print("可以赴约的嘉宾有：", invitation_list)
print("无法赴约的嘉宾有：" + unavailable_list)

invitation_list.insert(3, "廖裕强")
print("新的嘉宾名单：", invitation_list)


print("\n邀请方找到了一张更大的桌子，可以容纳更多嘉宾了。")
new_invitation_list = ['罗浩川', '朱志诚', '李芳明', '陈嘉豪']
print("新邀请的嘉宾有：", new_invitation_list)
invitation_list.insert(0, '罗浩川')
invitation_list.insert(4, '朱志诚')
invitation_list.insert(5, '李芳明')
invitation_list.append('陈嘉豪')
print("\n")

print("全部嘉宾：", invitation_list)
print("\n")
for i in range(0, 9):
    print(f"{invitation_list[i]}" + "," + invitation_letter)
# print(invitation_list[0] + "," +invitation_letter)
# print(invitation_list[1] + "," +invitation_letter)
# print(invitation_list[2] + "," +invitation_letter)
# print(invitation_list[3] + "," +invitation_letter)
# print(invitation_list[4] + "," +invitation_letter)
# print(invitation_list[5] + "," +invitation_letter)
# print(invitation_list[6] + "," +invitation_letter)
# print(invitation_list[7] + "," +invitation_letter)
# print(invitation_list[8] + "," +invitation_letter)
print("\n")
#删除名单
apology_letter = "很抱歉因新购买的餐桌无法按时送到，无法坐下太多人，此次聚餐取消。"
for x in range(0, 6):
    cancel_invite_list = invitation_list.pop()
    print(cancel_invite_list + "," + apology_letter)

# cancel_invite_list_1 = invitation_list.pop()
# cancel_invite_list_2 = invitation_list.pop()
# cancel_invite_list_3 = invitation_list.pop()
# cancel_invite_list_4 = invitation_list.pop()
# cancel_invite_list_5 = invitation_list.pop()
# cancel_invite_list_6 = invitation_list.pop()
# print(cancel_invite_list_1 + "," + apology_letter)
# print(cancel_invite_list_2 + "," + apology_letter)
# print(cancel_invite_list_3 + "," + apology_letter)
# print(cancel_invite_list_4 + "," + apology_letter)
# print(cancel_invite_list_5 + "," + apology_letter)
# print(cancel_invite_list_6 + "," + apology_letter)

print("\n")
print("允许前来的嘉宾：")
print(invitation_list)
num = len(invitation_list)
print("一共邀约了", num, "名嘉宾")
for i in range(0, 3):
    i + 1
    print(invitation_list[i] + "," + invitation_letter)
for i in range(3):
    i = 0
    del invitation_list[i]
print(invitation_list)
