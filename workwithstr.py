def maktab(arg):
    list_1.pop()
    list_2.append(3)

list_1=[8,12,10,9]
list_2=list_1
list_1.pop(1)
list_3=list_1
maktab(list_2)
sum_list=sum(list_3)
print(sum_list)
