def is_armstrong_number(number):
    c_number = [int(i) for i in str(number)]
    r_sum = 0
    print(c_number)
    for i in c_number:
        r_sum += i ** len(c_number)

    return number == r_sum
