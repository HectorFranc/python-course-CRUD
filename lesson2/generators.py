def fibonacci(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a + b


for e in fibonacci(35):
    print(e) # Prints fibonacci numbers < 35
