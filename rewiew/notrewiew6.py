n = int(input())

three = 0
lastnum = 0
chotniy = 0
bolshefive = 0
bolshesemi = 1
nolipyat = 0
lastnumber = n % 10

while n > 0:
    s = n % 10

    if s == 3: three += 1
    elif s == lastnumber: lastnum += 1
    elif s % 2 == 0: chotniy += 1
    elif s > 5: bolshefive += s
    elif s > 7: bolshesemi *= s
    elif s == 0 or s == 5: nolipyat += 1