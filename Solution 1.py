# The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that
# match the next digit in the list. The list is circular, so the digit after the last digit is the first digit
# in the list.
#
# For example:
#
# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2)
# matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

my_list = []

with open("input1.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            # print ("End of file")
            break
        my_list.append(c)

print(my_list)


count = 0



for i in range(len(my_list)):
    try:
        if(my_list[i]==my_list[i+1] and i<len(my_list)-1):
            print(my_list[i])
            count+=int(my_list[i])
    except:
        print("error")

    if (i + 1 == len(my_list)):
        print(my_list[i])
        if (my_list[i] == my_list[0]):
            count += int(my_list[0])


print(count)

