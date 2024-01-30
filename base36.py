def base36encode(input):
    lst36='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = int(input)
    base36 = ''
 
    if 0 <= number < len(lst36):
        return lst36[number]
 
    while number != 0:
        number, i = divmod(number, len(lst36))
        base36 = lst36[i] + base36
        
    return base36

print(base36encode(input()))