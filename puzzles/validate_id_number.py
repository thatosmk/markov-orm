import re



# the len of this ID number is 13
# format {YYMMDD}{SSSS}{A}{Z}
# SSS - define gender -> 0000 - 4999 (Females) and 5000 - 9999 (Males)
# C - Citizenship, 0 - SA, 1 - Other
# A - usually 8 or 9 [ but can also be other values]
# Z  - check digit

def isdigits(id_number):
    # check if the ID number contains only digits
    if re.match('^[0-9]*$', str(id_number)):
        # also check the first 6 digits are YYMMDD
        if re.match('^[0-9]{6}',str(id_number)[0:6]):
            #checksum(id_number)
            print "Do check sum"

def checksum(id_number):
    # add al the digits in the odd positions (exclude the last digit)

    # move the even position into a field (bit stream)and multiply by 2

    # add the digits of the result in the result above, e.g, 21112 = 2+1+1+1+2

    # add the answer to the first result


    # subtract the second digit form 10, and the result must tally with the
    # last number in the ID Number.
    # ...if the result is 2digits, the last digit is used to compare agaisnt
    # checksum

    # conver the number into a int array
    numbers = [int(i) for i in str(id_number)]

    # initialise the odd_sum
    odd_sum = 0
    even_str=""
    # add all the numbers in off positions except for the last digit
    for i in range(12):
        # find when i is odd
        if(i%2 !=0):
            odd_sum += numbers[i]        
        else: 
           even_str += str(numbers[i]) 

    # add the even_str numbers
    even_sum  = sum(map(int, even_str)) 

    # add even_sum to odd_sum
    new_sum = even_sum + odd_sum
    new_sum_arr = [int(i) for i in str(new_sum)]
    # subtract the second digit(from new sum) from 10 and check with check digit
    result_checker = 10 - new_sum_arr[len(new_sum_arr)/2]

    if result_checker == numbers[len(numbers) - 1]: 
        print "Valid ID number"
   
    print "Invalid ID number"
       

isdigits(8801235111088)
