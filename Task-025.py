#Identity Operator

# == check kore value same kina
# is check kore memory te same object kina

list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1

# Value compare
print("list1 == list2 :", list1 == list2)

# Object compare
print("list1 is list2 :", list1 is list2)

# list3 hocche list1 er same object
print("list1 is list3 :", list1 is list3)

# is not check kore object different kina
print("list1 is not list2 :", list1 is not list2)