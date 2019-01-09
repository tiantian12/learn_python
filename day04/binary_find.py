#-*-coding:utf-8-*-
def binary_find(datasource,find_n):
    mid=int(len(datasource)/2)
    if mid>0: 
        if datasource[mid]>find_n:
            binary_find(datasource[:mid],find_n)
        elif datasource[mid]<find_n:
            binary_find(datasource[mid:], find_n)
        else:
            print("you find it")
    else:
        print("you not find it")

if __name__=="__main__":
    dataList=list(range(0,600,3))
    print(dataList)
    binary_find(dataList,2)