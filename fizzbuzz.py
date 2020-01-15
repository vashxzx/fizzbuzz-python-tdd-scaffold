def fb(a):

    r=""

    if a%3==0:r+= "Fizz"

    if a%5==0:r+= "Buzz"

    if r=="":r+=str(a)

    return r
