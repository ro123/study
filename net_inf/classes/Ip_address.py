
class Ip_address():
    
    def __init__(self, dec_ip, bin_ip, pre_mask, dec_mask, bin_mask):
        self.dec_ip = dec_ip 
        self.bin_ip = bin_ip 
        self.dec_mask = dec_mask  
        self.pre_mask = pre_mask  
        self.bin_mask = bin_mask  
               
    def __str__(self):
        
        return f"{self.dec_ip} /{self.pre_mask}"
    
    def net_ip(self):
        net =[int(x) & int(y) for x,y in zip(((self.dec_ip).split('.')),((self.dec_mask).split('.')))]
        self.net = net
        return f"{net[0]}.{net[1]}.{net[2]}.{net[3]}"
    
    def broad(self):
        if self.pre_mask == '32':
            return 'There is no broadcast in 32 size network'
        elif self.pre_mask == '31':
            return 'There is no broadcast in 31 size network'
        else:
            wild_mask = [int(x) - int(y) for x,y in zip(['255','255','255','255'],(self.dec_mask).split('.'))]
            broadcast = [int(x) | y for x,y in zip(self.net,wild_mask)]
            self.broadcast = broadcast
            return f'{broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]}'
        
    def freeadr_amount(self):
        amount = 0
        if self.pre_mask == '32':
            amount = 1
        elif self.pre_mask == '31':
            amount =  2
        else:
            amount =  2**(32-int(self.pre_mask))-2
        self.amount = amount
        
    def first_adr(self):
        if self.pre_mask == '32':
            fadr = self.dec_ip
            self.fadr = fadr
            return fadr
        elif self.pre_mask == '31':
            fadr = self.net
            self.fadr = fadr
            return f'{fadr[0]}.{fadr[1]}.{fadr[2]}.{fadr[3]}'
        else:
            fadr = self.net[:]
            fadr[3] = fadr[3]+1
            self.fadr = fadr
            return f'{fadr[0]}.{fadr[1]}.{fadr[2]}.{fadr[3]}'
            
    def last_adr(self):
        if self.pre_mask == '32':
            return self.dec_ip
        elif self.pre_mask == '31':
            ladr = self.net
            ladr[3] = ladr[3]+1
            self.ladr = ladr
            return f'{ladr[0]}.{ladr[1]}.{ladr[2]}.{ladr[3]}'
        else:
            ladr = self.broadcast[:]
            ladr[3] = ladr[3]-1
            self.ladr = ladr
            return f'{ladr[0]}.{ladr[1]}.{ladr[2]}.{ladr[3]}'

    def output_info(self):
        output_list=[]
        self.net_ip()
        self.freeadr_amount()
        self.broad()
        self.first_adr()
        self.last_adr()
        output_list.append('\nInputed IP-address information:')
        output_list.append(f'IP-address in dotted format: {self.dec_ip} /{self.dec_mask}')
        output_list.append(f'IP-address in CIDR format: {self.dec_ip} /{self.pre_mask}')
        output_list.append(f'IP-address in binary format: {self.bin_ip} /{self.bin_mask}')
        output_list.append('\nNetwork information:')
        output_list.append(f'Network address is:  {self.net[0]}.{self.net[1]}.{self.net[2]}.{self.net[3]}')
        output_list.append(f'Broadcast address is:  {self.broadcast[0]}.{self.broadcast[1]}.{self.broadcast[2]}.{self.broadcast[3]}')
        output_list.append(f'Amount of free addresses in the network are:  {self.amount}')
        output_list.append(f'First free address in the network is:  {self.fadr[0]}.{self.fadr[1]}.{self.fadr[2]}.{self.fadr[3]}')
        output_list.append(f'Last free address in the network is:  {self.ladr[0]}.{self.ladr[1]}.{self.ladr[2]}.{self.ladr[3]}')
        self.output_list = output_list
        for el in output_list:
            print(el)    

    
    def import_to_excel(self):
        import xlwt
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('IP adr and net info')
        row = 0
        for st in self.output_list:
            sheet1.write(row,1,st)
            row += 1
        sheet2 = book.add_sheet('All available adr in net')
        
        list_of_adr = []
        while True:
            if self.fadr!=self.ladr:
                list_of_adr.append(f'{self.fadr[0]}.{self.fadr[1]}.{self.fadr[2]}.{self.fadr[3]}')
                if self.fadr[3]<255:
                    self.fadr[3] +=1
                    continue
                else:
                    self.fadr[3] = 0
                    if self.fadr[2]<255:
                        self.fadr[2] +=1
                        continue
                    else:
                        self.fadr[2]=0
                        if self.fadr[1]<255:
                            self.fadr[1]+=1
                            continue
                        else:
                            if self.fadr[0]<255:
                                self.fadr[0] += 1
                                continue
                            else:
                                continue
            else:
                list_of_adr.append(f'{self.ladr[0]}.{self.ladr[1]}.{self.ladr[2]}.{self.ladr[3]}')
                break
        row = 0
        for el in list_of_adr:
            sheet2.write(row,1,el)
            row += 1
        book.save(f'History/{self.dec_ip} {self.pre_mask}.xls')
