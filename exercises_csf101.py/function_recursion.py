def sum_of_digit(n):
    if n < 10:
        return n #base case
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return   sum_of_digit(remaining_digits + last_digit) # recursive case 
    
    
print(sum_of_digit(222)) 