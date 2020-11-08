def print_function(n):
    sum = ''
    i = 1
    while i <= n:
        sum = sum + str(i)
        i = i+1
    return sum

n = int(input())
print(print_function(n))