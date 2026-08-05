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
			decrypted_message = add_char(decrypted_message, result_up)	 # MERGE FUNCTION ADDS DECRYPTED CHAR TO DECRYPTED MESG VARIABLE
		elif char.islower():
			result_down = decrypt_lower_char(char, key)
			decrypted_message = add_char(decrypted_message, result_down)
		else:
			decrypted_message = add_char(decrypted_message, char)	# WE JUST ADD THE CHAR TO THE ALREADY EXISTING DECRYPTED MESSAGE
	return decrypted_message	# WE MUST RETURN DATA THAT WILL BE OUTPUTTED WHEN FUNCTION IS CALLED AND RAN


# FUNCTION FOR SCORING SYSTEM
def score_text(text):
	common = "ETAOINSHRD"	# DEFINE COMMON AND RARE LETTERS TO BE EVALUATED
	rare = "JKQXZ"

	score = 0	# SCORE BOARD INITIATED TO 0

	for char in text:	# LOOP THROUGH EACH CHARACTER IN TEXT TO BE DECIPHERED
		char_upper = char.upper()	# CONVERT TO UPPERCASE FOR COMPARISON

		if char_upper in common:
			score += 2	# ADD 2 IF COMMON
		elif char_upper in rare:
			score -= 1	# SUBTRACT 1 IF RARE

	return score

# MAIN FUNCTION TO GUESS AND CRACK
def crack_caesar(ciphertext):
	best_key = 0
	best_score = -999	# OR FLOAT(-INF) WHICH REPRESENTS NEGATIVE INFINITY, SO WE CAN HAVE A PROPER BASELINE TO COMPARE SUBSEQUENT TEST KEYS
	best_message = ""	# TO STORE THE LEADING BEST DECRYPTED MESSAGE AS THE LOOP PROGRESSES

	for test_key in range(1, 26):	# WE RANGE FROM 1 TO 25 AS TEST KEYS
		test_message = decrypt_text(ciphertext, test_key)
		test_score = score_text(test_message)
		if test_score > best_score:	# WE RUN A CONDITION TO UPDATE THE FUNCTION VARIABLES AS THE LOOP RUNS
			best_score = test_score
			best_message = test_message
			best_key = test_key
	return best_key, best_message



# encrypted_message = "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald." (used for testing)

print('='*12, "CAESAR CIPHER CRACKER (DOUBLE DEZZ)", '='*12)

encrypted_message = input("Paste encrypted text: ")

key, result = crack_caesar(encrypted_message)	# GRABS BEST_KEY AND BEST_MESSAGE RESPECTIVELY

print(f"\nDECRYPTION SUCCESSFUL!\n\nDETECTED KEY ==> Backward shift by {key}\nDECRYPTED MESSAGE ==> {result}")
