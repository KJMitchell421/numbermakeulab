def is_even(number):
    if number % 2 == 0:
        return True
    else: 
        return False

def sum_between(start, end):
    summ = 0
    for i in range(start, end+1):
        summ += i
    return summ
        
number = int(input("Type a number: "))
start = int(input("Type a starting number: "))
end = int(input("Type a ending number: "))

if is_even(number):
    print(f"{number} is even,")
else:
    print(f"{number} is odd,")
    
print(f"sum:{sum_between(start, end)}")