 #
 # Encrypts a string using an XOR gate.
 # The ciphertext a sequence of numbers between 0 and 255, seperated by a '-' character. The character 'X' is used as padding to make the number 3 characters.
 # The 'mode' parameter is true for encryption, false for decryption
 # The 'password' parameter is the password used to en/decrypt the string
 # The 'input' paramater is the string to be en/decrypted
 #
def xor(mode, password, input):
	if(password.__len__()==0 or input.__len__()==0):
		return ""
	password = password.lower()
	if(mode):
		if(password.__len__()<input.__len__()):
			count = 0
			while(password.__len__()<input.__len__()):
				password += password[count]
				count = count + 1;
				if(count==password.__len__()):
					count = 0
	else:
		if(password.__len__()<(input.__len__()/4)):
			count = 0
			while(password.__len__()<(input.__len__()/4)):
				password += password[count]
				count = count + 1;
				if(count>=password.__len__()):
					count = 0
	outputString = ""
	cipherChars = input.split('-')
	for i in range(len(password)):
		if(mode):
			toAdd = ord(password[i]) ^ ord(input[i])
			if(i>0):
				outputString += "-"
			outputString += str(toAdd)
			if(toAdd<100):
				outputString += "X"
			if(toAdd<10):
				outputString += "X"
		else:
			thisChar = cipherChars[i]
			thisChar = thisChar.replace("X", "")
			outputString += chr(int(thisChar))
	return outputString

