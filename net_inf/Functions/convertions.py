def binary_to_decimal(binary):
    binary = binary.split('.')
    binary = [str(int(x,2)) for x in binary]
    strbinary = '.'.join(binary)
    return strbinary

def decimal_to_binary(decimal):
    decimal = decimal.split('.')
    for i in range(len(decimal)):
        decimal[i] = bin(int(decimal[i]))
        if len(decimal[i]) - 2 < 8:
            decimal[i] = '0'*(10 - len(decimal[i]))+str(decimal[i][2:])
        else:
            decimal[i] = str(decimal[i][2:])
    strdecimal = '.'.join(decimal)
    return strdecimal

def binary_to_prefix(binary):
    binary = list(binary)
    binary = [x for x in binary if x!='.']
    prefix = 0
    state = 0
    while state == 0:
        for x in binary:
            if x == '1':
                prefix +=1
                continue
            else:
                state = 1
                break
    return str(prefix)

def decimal_to_prefix(decimal):
    #import decimal_to_binary
    #import binary_to_prefix
    prefix = binary_to_prefix(decimal_to_binary(decimal))
    return prefix

def prefix_to_binary(prefix):
    binary = list('1'*int(prefix) + '0'*(32-int(prefix)))
    strbinary = ''
    for i in range(len(binary)):
        if i==7 or i ==15 or i ==23:
            strbinary = strbinary + binary[i] + '.'
        else:
            strbinary += binary[i]
    return strbinary

def prefix_to_decimal(prefix):
    #import prefix_to_binary
    #import binary_to_decimal
    decimal = binary_to_decimal(prefix_to_binary(prefix))
    return decimal