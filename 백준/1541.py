import re
expression = input()
num_list = re.split('[+-]',expression)
plus = int(num_list[0])
minus = 0
offset = len(num_list[0])
state = 0
for i in range(1,len(num_list)):
    if expression[offset] == '-' :
        state = 1
    if state :
        minus += int(num_list[i])
    else :
        plus += int(num_list[i])
    offset += 1+ len(num_list[i])
print(plus - minus)