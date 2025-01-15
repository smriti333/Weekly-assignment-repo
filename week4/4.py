#calling function 
def remove_last_char(input_string):
    if len(input_string) > 1:
        return input_string[-1]
    else:
        return input_string

#test function
print(remove_last_char("Pizza"))
print(remove_last_char("S"))
print(remove_last_char(""))