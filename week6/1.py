def integar_to_binary(num):
    if num < 1:
        raise ValueError("The integar must be positive!")

    else:
       print(f"The binary represention of {num} is {bin(num)[2:]}")

try:
    num=int(input("Enter the positive integar: "))
    integar_to_binary(num)
except ValueError as error:
    print(error)

  

