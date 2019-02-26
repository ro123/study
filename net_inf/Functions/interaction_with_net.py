#проверка маски на бинарность
def ismaskbinary(mask):
    from functools import reduce
    mask = mask.split('.')    
    for el in mask:
        if len(el) != 8:
            return False
        else:
            continue
    newmask = []
    for el in mask:
        for x in el:
            newmask.append(x)
    #проверка на символы
    for el in newmask:
        if el != '1' and el != '0':
            return False
        else:
            continue
    #проверка на изменения
    binary = 0
    for el in range(0,len(newmask)-1):
        if newmask[el] != newmask[el + 1]:
            binary += 1
        else:
            continue
    if binary > 1:
        return False
    else:
        return True
    print(newmask)
    
def all_free_net_adr(first,last):
    fadr = [int(x) for x in first.split('.')]
    ladr = [int(x) for x in last.split('.')]
    while True:
        if fadr!=ladr:
            print(fadr)
            if fadr[3]<255:
                fadr[3] +=1
                continue
            else:
                fadr[3] = 0
                if fadr[2]<255:
                    fadr[2] +=1
                    continue
                else:
                    fadr[2]=0
                    if fadr[1]<255:
                        fadr[1]+=1
                        continue
                    else:
                        if fadr[0]<255:
                            fadr[0] += 1
                            continue
                        else:
                            continue
        else:
            print(ladr)
            break