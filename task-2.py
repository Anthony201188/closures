
# function checks for the number of zeros in a the LOCAL variable "number" 
def zero():
    zero = 0
    def count_zeros(number):
        return str(number).count(str(zero))
    return count_zeros


inner2 = zero()
print("Result: ", inner2) # to check if correct objects or incorrectly str/int are returned! 


print(inner2.__code__.co_varnames)
print(inner2.__code__.co_freevars)
print(inner2.__closure__[0].cell_contents) 
