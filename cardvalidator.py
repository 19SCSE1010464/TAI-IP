sum_odd_digits = 0
sum_even_digits = 0
total = 0
card_number = input("Enter card number")

# Remove any '-',' '
card_number = card_number.replace("-","")
card_number = card_number.replace(" ",'')
card_number = card_number[::-1]
print(card_number)

# Add all digits in odd places from right to left
for x in card_number[::2]:
    sum_odd_digits+= int(x)

# Double every second digits from right to left
for x in card_number[1::2]:
    x = int(x)*2
    if x>=10:
        sum_even_digits+=(1+(x%10))
    else:
        sum_even_digits+=x

# sum the total of step 2 and step 3
total = sum_odd_digits + sum_even_digits

# if total is divisible by 10 card is true
if total%10 ==0:
    print("True")
else:
    print('false')

# With Luhn Algorithm
def isValidNumber(input):

    input = input[::-1]

    input = [int(x) for x in input]
    for i in range(1,len(input),2):
        input[i]*=2
        if input[i]>9:
            input[i]= input[i]%10+1
    total = sum(input)
    return total%10 == 0
print(isValidNumber("3018161857595544"))









