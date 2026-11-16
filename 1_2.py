def is_even(number):
    if number % 2 == 0:
        return True
    else: 
        return False

def next_step(number):
    if is_even(number):
        return number // 2
    else:
        return (number * 3) + 1

def steps_to_one(number):
    steps = 0
    while number != 1:
        number = next_step(number)
        print(number)
        steps += 1
    print("steps:")
    return steps
    
number = int(input("Type a number greater than 0: "))
print(steps_to_one(number))