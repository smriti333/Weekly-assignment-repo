def find_factors(num):
    if num == 0:
        raise ValueError
    elif num < 0:
        raise ValueError
    factors= [i for i in range(1,num +1) if num % i == 0]
    return factors

test_inputs =  [1,6]
test_outputs = {num: find_factors(num) for num in test_inputs}
print(test_outputs)
