x = input()
y = []
for i in x:
    asc_number = ord(i)
    if ( asc_number >=65 and asc_number <=89) or (asc_number >=97 and asc_number <= 122):
        y.append(chr(asc_number+1))
    else:
        y.append(i)
print("".join(y))
