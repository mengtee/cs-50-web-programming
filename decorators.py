# Functional programming, adding some stuff to a function using a function

# decorator
def annouce(f):
    # wrapper is a closure
    def wrapper():
        print("About to run a functions...")
        f()
        print("Done with the function.")
    # Returning back the wrapper function 
    return wrapper

@annouce
def hello():
    print("Hello world")