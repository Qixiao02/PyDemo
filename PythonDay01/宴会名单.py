invitation_list = ['黄林鸿', '陈柏榆', '黄智浩', '曾望', '张宇杰']
# print(invitation_list)
invitation_letter = "我想邀请您于6月30日晚上7点于学校饭堂二楼共进晚餐。"

"""无法赴约"""
unavailable_list = "曾望"
invitation_list.remove(unavailable_list)
print("可以赴约的嘉宾有：")
print(invitation_list)
print("无法赴约的嘉宾有：" + unavailable_list)

invitation_list.insert(3, "廖裕强")
print("新的嘉宾名单：")
print(invitation_list)
# print(invitation_list[0] + "," +invitation_letter)
# print(invitation_list[1] + "," +invitation_letter)
# print(invitation_list[2] + "," +invitation_letter)
# print(invitation_list[3] + "," +invitation_letter)
# print(invitation_list[4] + "," +invitation_letter)

# for i in range(0, 8):
#     i = invitation_list[0]+1
#     print(invitation_letter + i)

print("\n邀请方找到了一张更大的桌子，可以容纳更多嘉宾了。")
print("新邀请的嘉宾")
new_invitation_list = ['罗浩川', '朱志诚', '李芳明', '陈嘉豪']

invitation_list.insert(0, '罗浩川')
invitation_list.insert(4, '朱志诚')
invitation_list.insert(5, '李芳明')
invitation_list.append('陈嘉豪')
print(new_invitation_list)
print("全部嘉宾：")
print(invitation_list)
print(invitation_list[0] + "," +invitation_letter)
print(invitation_list[1] + "," +invitation_letter)
print(invitation_list[2] + "," +invitation_letter)
print(invitation_list[3] + "," +invitation_letter)
print(invitation_list[4] + "," +invitation_letter)
print(invitation_list[5] + "," +invitation_letter)
print(invitation_list[6] + "," +invitation_letter)
print(invitation_list[7] + "," +invitation_letter)
print(invitation_list[8] + "," +invitation_letter)
