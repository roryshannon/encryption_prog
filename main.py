import os # os for exit function, random for the random key, math for specifically the math.floor, the operator for the xor function, time for waiting with .sleep
from random import randint
import math
from operator import xor
import time


print('Hello and welcome to the Encryption process! Please select an option by entering its number below!\n') # outside the menu so when we loop below the welcom is only said once
while True: #infinite loop to go back to menu as soon as other functions are done while True: #loops forever, but using the if and return will break out of the function if any of the conditions are met, otherwise loops

	def menu(): #making menu function
	
			print('This is the menu, please chose an option!')
			print('\tEncrypt using a ceasar cipher! : 1')
			print('\tEncrypt using a one time pad! : 2')
			print('\tDecrypt a ceasar cipher. : 3')
			print('\tDecrypt a one time pad. : 4')
			print('\tBrute force a caesar ;) :5')
			print('\tExit :( : 6')
			menu_choice = input()
		
			if menu_choice == '1': #all the menu choices 
				print('you chose', menu_choice)
				encrypt_caesar()
				
			elif menu_choice == '2':
				print('you chose', menu_choice)
				encrypt_otp()
				
			elif menu_choice == '3':
				print('you chose', menu_choice)
				decrypt_caesar()
				
			elif menu_choice == '4':
				print('you chose', menu_choice)
				decrypt_otp()
				
				
			elif menu_choice == '5':
				print('you chose,', menu_choice)
				brute_force()
				
			elif menu_choice == '6':
				print('you chose', menu_choice)
				print('thanks for using my program!')
				exit()
			else:
				print('please input a valid menu choice!\n')    
		
		
	
	
	def read_from_file(): # reading in from the file
		while True: #loops the process of inoutting file name
			filename = input('what is the name of your text file ') #lets user input file name
			try: #checking if there is a valid file in that location, if an error occurs tells user that program cant find the file
				document = open(filename) 
				break # if successful breaks loop
			except: 
				print("unable to find file, makesure to add '.txt'\n")
				time.sleep(3)
				
	
		
	
		text = [] #defining the list
	
		for line in document: # for statement goes through document and adds each line to the list
			line = line.replace("\n", "") 
			text.append(line)
		
		return text 
	
			
	
	def create_caesar_key():
		key_list = [] #makes the list which will contain the key
		rand_int = 0 #sets var rand_int to 0, not sure if i need to do this but hey it works so shh
		
		for i in range(1,9):
			rand_int = randint(33, 126) # see? i am using it? maybe not the most effiecint but gets the random number to add to key list to make key
			key_list.append(rand_int)
			
				
		key = [] # making those random numbers their ascii equivalents
		for i in key_list:
			letter = chr(i)
			key.append(letter)
			
		print('Key: ', ''.join(key)) #printing the key with all the square brackest and ''s 
		
		return key
	
	def calculate_offset(key):
		key_total = 0 #declaring total of all key numbers added together
		
		for i in key: #turning the key into a number
			number = ord(i)
			key_total += number #adding all of the now number values to the total
		
		offset = key_total/8.0 # doing all the calculations to get the offset
		offset = math.floor(offset) 
		offset -= 32	
		
		return offset		
	
	def encrypt_text(text, offset):
		
		number_list = [] #list that's going to be full of the ascii value of each encrypted letter
		string_text = text[0] # the string version of list so we can modify each letter individually 
		#print(string_text) # test print 
		
		for i in string_text: # going through all of the above string
			number = ord(i) 
			
			if number != 32: # 32 is ascii value for space so any character that is not space is changed
				number += offset
			if number > 126: #great than 126 must loop back to A
				number -= 94
			number_list.append(number)
			
		encrypted_list = [] # declaring my encrypted list 
	
		for i in number_list: #making each number in the list a letter/ ascii convert
			letter = chr(i)
			encrypted_list.append(letter)
		
		print('Encrypted text: ', ''.join(encrypted_list))
		print('\n')
		
		cipher_text = ''.join(encrypted_list)	
		
		return cipher_text
		
	def UploadToFile(cipher_text): # uploads text parameter as a file
	
		file = input("\nEnter the name of the file you would like your ciphertext saved to.\n")
		file = open(file, 'w') #making this w not a intentionally writes over anything already in the file to avoid errors
		file.write(cipher_text)			
		print('\n file saved! \n')								
																					
	def encrypt_caesar(): #master encryption function, calls other encryption functions
		text = read_from_file()
		
		print('\n', text[0], '\n')
		
		key = create_caesar_key()
		
		offset = calculate_offset(key)
		
		cipher_text = encrypt_text(text, offset)
		
		UploadToFile(cipher_text)
		
		
	
	
	def get_decrypted_key():
		userInput = input("Enter your 8 digit key.\n")
		while len(userInput) != 8:
			userInput = input("Key is incorrect length! Please retry.\n")
		return(userInput)
		
	
	def decrypt_message(text, key):
		
		offset = calculate_offset(key)
		
		number_list = []
		
		string_text = text[0]
		for i in string_text: # going through all of the above string
			number = ord(i) 
			
			if number != 32: # 32 is ascii value for space so any character that is not space is changed
				number -= offset
			if number < 32: #less than 32 must loop back up to A on decrypt
				number += 94
			number_list.append(number)
							
		decrypted_list = [] # declaring my encrypted list 
		for i in number_list: #making each number in the list a letter/ ascii convert
			letter = chr(i)
			decrypted_list.append(letter)
	
		print('Decrypted text: ', ''.join(decrypted_list))
		print('\n')
	
	def decrypt_caesar():
		text = read_from_file()
		
		key = get_decrypted_key()
		
		plain_text = decrypt_message(text, key)
		
		
	
		
	def create_otp_key(text):
		key_list = [] #makes the list which will contain the key
		rand_int = 0 #sets var rand_int to 0, not sure if i need to do this but hey it works so shh
		
		string_text = text[0]
		
		for i in string_text:
			rand_int = randint(50, 75) # see? i am using it? maybe not the most effiecint but gets the random number to add to key list to make key
			letter = chr(rand_int)
			key_list.append(letter)
			
			
		print('Key: ', ''.join(key_list)) #printing the key with all the square brackest and ''s 
		
		str_key = ''.join(key_list)
		return str_key 
	
	def otp_XOR_op(key, text):
		#print(text)
		#print('Key: ', ''.join(key))
		
		string_text = text[0] # making text list into a single string
		xorable_list_text = []
		
		for i in string_text: # going through all of the above string
			number = ord(i)
			xorable_list_text.append(number)
		
		key_string = key[0] # making a string of the key
		xorable_list_key = []
		test=[]
		
		for i in key: # going through all of the key
			number = ord(i) 
			xorable_list_key.append(number)
		
		cipher = []
		count = 0
		
		for i in xorable_list_key:
			xored = xor(i, xorable_list_text[count])
			count += 1
			cipher.append(xored)
				
		
	#really huge wrong way i first tried example
		#for binaryi in bin_list_key:
			#for binaryj in bin_list
				#for i in binaryi:
					#boo_a = i
					#print(boo_a)
				#for j in binaryj:
					#boo_b = j
					#print(boo_b)
				#bin_cipher_list.append(bin_cipher)
				
				
		cipher_text = []
		for i in cipher:
			letter = chr(i)
			cipher_text.append(letter)
		
		
		
		print('\nEncrypted text: ', ''.join(cipher_text))
		print('\n')
		
		otp_encryption = ''.join(cipher_text)
		return otp_encryption
	
	def encrypt_otp():
		text = read_from_file()
		
		key = create_otp_key(text)
		
		cipher_text = otp_XOR_op(key, text)	
		
		print('upload cipher text')
		UploadToFile(cipher_text)
		print('upload key text name')
		UploadToFile(key)
	
	
	def get_otp_decrypt_key():
		while True: #loops the process of inoutting file name
			filename = input('what is the name of your otp key file ') #lets user input file name
			try: #checking if there is a valid file in that location, if an error occurs tells user that program cant find the file
				document = open(filename) 
				break # if successful breaks loop
			except: 
				print("unable to find file, makesure to add '.txt'\n")
				time.sleep(2)
	
		
	
		text = [] #defining the list
	
		for line in document: # for statement goes through document and adds each line to the list
			line = line.replace("\n", "") 
			text.append(line)
		
		string_key = text[0]
		"".join(string_key.split())
		print(string_key)
		return text 
		
	def decrypted_otp_text(key, text):
		
		string_text = text[0] # making text list into a single string
		xorable_list_text = []
		
		for i in string_text: # going through all of the above string
			number = ord(i)
			xorable_list_text.append(number)
		
		key_string = key[0] # making a string of the key
		xorable_list_key = []
		test=[]
		
		for i in key_string: # going through all of the key
			number = ord(i) 
			xorable_list_key.append(number)
		
		cipher = []
		count = 0
		
		for i in xorable_list_key:
			xored = xor(i, xorable_list_text[count])
			count += 1
			cipher.append(xored)
		
		cipher_text = []
		for i in cipher:
			letter = chr(i)
			cipher_text.append(letter)
		
		
		
		print('\nEncrypted text: ', ''.join(cipher_text))
		print('\n')
		
		otp_encryption = ''.join(cipher_text)
		return otp_encryption
		
	
	def decrypt_otp():
		text = read_from_file()
		
		key = get_otp_decrypt_key()
	
		decrypted = decrypted_otp_text(key, text)
		
		print(decrypted)
	
	def brute_solve_caesar(text):
		ascii_list = []
		str_text = ''.join(text) #making the cipher text list a string
		
		print(str_text)
		
		
		for i in str_text:
			ascii_list.append(ord(i))	
	
		count = 1
		offset = 1
		for i in range(94):
			for i in ascii_list:
				if ascii_list[i] < 126:
					new_letter = chr((ascii_list[count]) - offset) 
				else:
					ascii_list[count] -= 94
				count += 1
				offset += 1
			
	
	def brute_force():
		text = read_from_file()
			
		plain_text = brute_solve_caesar(text)
			
			
	menu()
