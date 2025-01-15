def find_primenumbers(num):
    if num <= 1:
        raise ValueError(f"{num} is not a prime number.")
    for i in range(2, int(num**0.5)+1):
         if num % i == 0:
            return False
    return True

test_inputs=[2,3,4]
try:
    test_outputs={num: find_primenumbers(num) for num in test_inputs}
    print(test_outputs)
except ValueError as error:
    print(error)
      