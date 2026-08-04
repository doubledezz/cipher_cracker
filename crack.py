# CAESAR CIPHER CRACKER

# FUNCTION TO DECRYPT UPPER CHARACTER
def decrypt_upper_char(char, key):
	shifted_number = (ord(char) - ord("A") - key) % 26	# HERE WE CONVERT THE CHARACTERS TO NUMBERS, SUBTRACT THE KEY AND THEN BACK TO CHAR
	return chr(shifted_number + ord("A"))

# FUNCTION TO DECRYPT LOWER CHARACTER
def decrypt_lower_char(char, key):
	shifted_number = (ord(char) - ord("a") - key) % 26	# SAME PROCEDURE AS UPPER CHAR, BUT WITH LOWER CASE 'A'
	return chr(shifted_number + ord("a"))

# FUNCTION TO MERGE DECRYPTED TEXT
def add_char(text, char):
	return text + char

# FUNCTION TO DECRYPT FULL TEXT
def decrypt_text(cipher, key):
	decrypted_message = ""

	# TO DECIPHER ENTIRE TEXT, WE LOOP THROUGH ALL CHARACTERS
	for char in cipher:	# WE ASSIGN EACH CHARACTER WE LOOP THROUGH TO A VARIABLE, CHAR
		if char.isupper():
			result_up = decrypt_upper_char(char, key)	# CALL DECRYPTION FUNCTION AND ASSIGN TO A VARIABLE
			decrypted_message = add_char(decrypted_message, result_up)	 # MERGE FUNCTN ADDS DECRYPTED CHAR TO DECRYPTED MESG VARIABLE
		elif char.islower():
			result_down = decrypt_lower_char(char, key)
			decrypted_message = add_char(decrypted_message, result_down)
		else:
			decrypted_message = add_char(decrypted_message, char)	# WE JUST ADD THE CHAR TO THE ALREADY EXISTING DECRYPTED MESSAGE
	return decrypted_message	# WE MUST RETURN DATA THAT WILL BE OUTPUTTED WHEN FUNCTION IS CALLED AND RAN



encrypted_text = "Khoor Zruog!"
key = 3


result = decrypt_text(encrypted_text, key)

print(result)
