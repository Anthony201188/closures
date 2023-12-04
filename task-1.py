#- look at the following functions:

def triple():
    a = 3
    def multiply(b):
        return a * b
    return multiply
triple()(6)

inner = triple()

# - what is the free variable? ANSWER: a = 3
# - what is the closure? ANSWER: the instance of the function tripple called inner so, inner = triple() which will be 3

""" ** use the following expressions to check **
inner.__ code__.co_varnames and
inner. code__.co_freevars, and 
inner.__ closure__[0].cell_contents 
to double check."""

print(inner.__code__.co_varnames)
print(inner.__code__.co_freevars)
print(inner.__closure__[0].cell_contents)












