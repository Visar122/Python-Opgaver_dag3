def sum_equation(numbers):

    total = sum(numbers)
    
    if not numbers:
        return "0 = 0"
    else:
    
        equation = " + ".join(str(num) for num in numbers) + " = " + str(total)
        return equation


print(sum_equation([1, 5, 7]))  
     
