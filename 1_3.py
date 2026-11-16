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
        steps += 1
    return steps

def describe(number, steps):
    if is_even(number):
        if steps > 10:
            return "even and long"
        else:
            return "even and quick"
    else:
        if steps <= 10:
            return "odd and quick"
        else:
            return "odd and long"

def sum_between(start, end):
    summ = 0
    for i in range(start, end+1):
        summ += i
    return summ

times = int(input("how many numbers do you want to test"))
biggest_journey = 0
last_num = 0
for i in range(times):
    number = int(input("Type a number greater than 0: "))
    if number <= 0:
        print("thats not allowed")
    else:
        steps = steps_to_one(number)
        if biggest_journey < steps:
            biggest_journey = steps
            last_num = number 
        print(f"{number}:{steps} steps, {describe(number, steps)}")
print(f"longest journey {last_num} with {biggest_journey}")
