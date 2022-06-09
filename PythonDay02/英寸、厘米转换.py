# 英寸,厘米转换👇

# value = float(input('请输入长度: '))
# unit = input('请输入单位: ')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效的单位')

#优化版😀√
def Length_Conversion():
    Length = float(input('请输入长度:'))
    units = int(input("请选择转换的方式:\n\t1.英寸转厘米\n\t2.厘米转英寸"))
    if units == 1:
        print("%f英寸 = %f厘米" % (Length, Length * 2.54))
    elif units == 2:
        print("%f厘米 = %f英寸" % (Length, Length / 2.54))
    else:
        print("请选择有效的选项！")

Length_Conversion()