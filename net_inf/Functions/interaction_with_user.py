#ввод и определение типа адреса
def input_and_define_adr():
    import re   
    while True:
        adr = input('Please input an ip address in any format:  ')
        if re.match(r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",adr) != None:
            print("This is the ip address in decimal format")
            return {'dec_ip':adr}
            break
        elif re.match(r"([0-1]{8})\.([0-1]{8})\.([0-1]{8})\.([0-1]{8})",adr) != None:
            print('This is the ip address in binary format')
            return {'bin_ip':adr}
            break
        else:
            print('Wrong address format. Please try again.')
            continue
 
 #ввод и определение типа маски
def input_and_define_mask():
    import re
    from Functions.interaction_with_net import ismaskbinary
    while True:
        mask = input('Please input mask in any format:   ')
        if re.match(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}0",mask) != None:
            print("This is the mask in decimal format")
            return {'dec_mask':mask}
            break
        elif ismaskbinary(mask) != False:
            print("This is the mask in binary format")
            return {'bin_mask':mask}
            break
        elif mask.isdigit() and float(mask) in range(0,33):
            print("This is the mask in prefix format")
            return {'pre_mask':mask}
            break
        else:
            print('Wrong mask format. Please try again.')
            continue

def repeat_or_exit():
    while True:
        appstatus = input('\nWould you like to continue using app? y/n  ')
        if appstatus.lower() == 'y':
            return True
            break
        elif appstatus.lower() == 'n':
            print('Good luck')
            return False
            break
        else:
            print('Can not define answer. Please try again.')
            continue