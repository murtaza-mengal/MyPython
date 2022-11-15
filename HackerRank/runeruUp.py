
# work perfect in test

# Runer up value mean second largest num
new_list=[]
for i in arr:
    if i not in new_list:
       new_list.append(i)
    
new_list.remove(max(new_list))
print(max(new_list))