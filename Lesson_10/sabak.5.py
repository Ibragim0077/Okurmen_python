words = input("Enter you FIO:")
print(*words.split(), sep='\n')

F_I_O = input("Enter you FIO:")
f_i_o = F_I_O.split()
print(F'{f_i_o[0][0]}.{f_i_o[1][0]}.{f_i_o[2][0]}')

ip_address = input("Enter your ip address:")
i_a = ip_address.split(',')
print(i_a)
for ip in i_a:
    if int (ip) < 0 or int(ip) > 255:
        print("No")
        break
else:
        print("Yes")

numbers = [8,9,10,11]
numbers[1] = 17
print(numbers)
numbers.extend([4,5,6])
print(numbers)
numbers.pop
















































































