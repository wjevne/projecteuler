def fibonacci(end):
    prev = 0
    cur = 1
    
    yield prev
    while cur <= end:
        yield cur
        prev, cur = cur, prev + cur