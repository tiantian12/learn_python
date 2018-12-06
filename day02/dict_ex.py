#coding=utf-8
list1=[11,22,33,44,55,66,77,88,99,100,111,122]
dic={}
# v1=[]
# v2=[]
# dic={}
# for i in list1:
#     if i<66:
#         v1.append(i)
#     else:
#         v2.append(i)
# dic['key1']=v1
# dic['key2']=v2
# print(dic)
for i in list1:
    if i<66:
        if "k1" in dic:
            dic["k1"].append(i)
        else:
            dic["k1"]=[i,]
    else:
        if "k2" in dic:
            dic["k2"].append(i)
        else:
            dic["k2"]=[i,]
print(dic)