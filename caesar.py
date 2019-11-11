# Takes inputs for message and shift, initalises encrypted 
def main():
	print ("Welcome to Caesar Shift\n")
	print ("=======================\n")
	print ("1. Encrypt\n2. Decrypt\n3.Read file")
	option = int(input("Option: "))

	message = input(str("Please enter a statement: "))
	shift = int(input("Enter shift number: "))

	if option == 1:
		encrypt(message, shift)
	elif option == 2:
		decrypt(message, shift)
	else:
		print("Error - Invalid Choice")
		main()

def encrypt(message, shift):
	encrypted = ''
	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) + shift
				if num > ord('z'):
					num -= 26
					encrypted += chr(num)
				elif num < ord('a'):
					num += 26
					encrypted += chr(num)
				else:
					encrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i]) + shift
				if num > ord('Z'):
					num -= 26
					encrypted += chr(num)
				elif num< ord('A'):
					num += 26
					encrypted += 26
				else:
					encrypted += chr(num)
		elif ord(message[i]) == 32:
			encrypted += ' '
		else:
			encrypted += message[i]
	print(encrypted)
	filewrite(encrypted)

def filewrite(encrypted):
	file = open('messages.txt', 'w')
	file.write(encrypted)
	file.close()
	print (f"The message {encrypted}, has been successfully written to {file.name}")

def decrypt(message, shift):
	decrypted = ''
	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) - shift
				if num > ord('z'):
					num -= 26
					decrypted += chr(num)
				elif num < ord('a'):
					num += 26
					decrypted += chr(num)
				else:
					decrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i]) - shift
				if num > ord('Z'):
					num -= 26
					decrypted += chr(num)
				elif num< ord('A'):
					num += 26
					decrypted += chr(num)
				else:
					decrypted += chr(num)
		elif ord(message[i]) == 32:
			decrypted += ' '
		else:
			decrypted += message[i]
	print(decrypted)

def fileRead():
	message = ''
	file = open("message.txt", "r")
	message += file.readline()
	shift = int(input("Enter shift: "))
	file.close()
	decrypt(message, shift)

if __name__ == "__main__":
	main()