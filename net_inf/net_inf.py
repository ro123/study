from functions.interaction_with_user import input_and_define_adr
from functions.interaction_with_user import input_and_define_mask
from functions.interaction_with_user import repeat_or_exit
from functions.convertions import binary_to_decimal  
from functions.convertions import binary_to_prefix
from functions.convertions import decimal_to_binary
from functions.convertions import decimal_to_prefix
from functions.convertions import prefix_to_binary
from functions.convertions import prefix_to_decimal
from classes.Ip_address import Ip_address

      
if __name__ == '__main__':    

	while True:
		
		add_adr = input_and_define_adr()	
		if add_adr.get('dec_ip') != None:
			dec_ip = add_adr['dec_ip']
			bin_ip = decimal_to_binary(dec_ip)
		else:
			bin_ip = add_adr['bin_ip']
			dec_ip = binary_to_decimal(bin_ip)
			
		
		add_mask = input_and_define_mask()
		if add_mask.get('pre_mask') != None:
			pre_mask = add_mask['pre_mask']
			bin_mask = prefix_to_binary(pre_mask)
			dec_mask = prefix_to_decimal(pre_mask)
		elif add_mask.get('bin_mask') != None:
			bin_mask = add_mask['bin_mask']
			pre_mask = binary_to_prefix(bin_mask)
			dec_mask = binary_to_decimal(bin_mask)
		else:
			dec_mask = add_mask['dec_mask']
			pre_mask = decimal_to_prefix(dec_mask)
			bin_mask = decimal_to_binary(dec_mask)
			if pre_mask == '32' or pre_mask == '31':
				print('32 and 31 size network have specific rules')
		
		add_adr = Ip_address(dec_ip,bin_ip,pre_mask,dec_mask,bin_mask)
			
		print(add_adr.net_ip())
		add_adr.output_info()

		
		while True:
			choice = input('\nWould you like to import this information and all free-o-use ip addresses to  excel file? y/n  ')
			if choice.lower() == 'y':
				add_adr.import_to_excel()
				print('\nFile has been saved in History folder')
				break
			elif choice.lower() == 'n':
				break
			else:
				continue
			
		if repeat_or_exit() == True:
			continue
		else:
			break

	
