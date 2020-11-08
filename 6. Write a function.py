#Write a function

def is_leap(year):
    
    if year%4 == 0:
        if year > 2000:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True

    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))