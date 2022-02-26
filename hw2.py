# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE
def encrypt(text, key):
    """
    encrypt the text according to a key, this function can only encrypt letters

    :param text: text that needs to be encrypted
    :param key: how many numbers to add to the ascii value of a letter in the text (key must be positive)
    :return: encrypted text according to the key
    """

    if key >= 26:  # if the key is bigger or equals 26 -> replace the key with the remainder of the division by 26
        key %= 26

    """ 
    if the key is 0 then is doesn't change the text.
    no need to check if there is at least one letter -> function handles cases when the char is not a letter
        """

    if key == 0 or len(text) == 0:  # if the length is 0 then there is no text to encrypt
        return text

    temp_text = list(text)  # convert the string to a list
    new_list = []  # new list -> modified according to the key
    new_text = ''  # string version of the new text
    i = -1  # index in temp_text

    for letter in temp_text:
        i = i + 1
        if 65 <= ord(letter) <= 90:  # if the letter given is a capital letter
            if (ord(letter) + key) > 90:  # if the modified letter is out of range -> ascii from 65 to 90
                new_letter = chr(ord(letter) + key - 26)  # there are 26 letters in the alphabet -> ascii value - 26
            else:
                new_letter = chr(ord(letter) + key)
            new_list.append(new_letter)

        elif 97 <= ord(letter) <= 122:  # if the letter given is not a capital letter
            if (ord(letter) + key) > 122:  # if the modified letter is out of range -> ascii from 97 to 122
                new_letter = chr(ord(letter) + key - 26)
            else:
                new_letter = chr(ord(letter) + key)
            new_list.append(new_letter)

        else:
            new_list.append(letter)  # if the given letter is not a letter -> no modifications required

    return new_text.join(new_list)


# ************************ QUESTION 2 **************************
### WRITE CODE HERE
def decrypt(text, key):
    """
    decrypt the text with a key, the function can only decrypt letters

    :param text: the text to decrypt
    :param key: how many numbers to take from the ascii value of the letter (key is not negative)
    :return: the decrypted text according to the key
    """

    if key >= 26:  # if the key is bigger or equals 26 -> replace the key with the remainder of the division by 26
        key %= 26
    """
    if the key is 0 then is doesn't change the text
    no need to check if there is at least one letter -> function handles cases when the char is not a letter
    """

    if key == 0 or len(text) == 0:  # if the length is 0 then there is no text to encrypt
        return text

    temp_text = list(text)  # convert the string to a list
    new_list = []  # new list -> modified according to the key
    new_text = ''  # string version of the new text
    i = -1  # index in temp_text

    for letter in temp_text:
        i = i + 1
        if 65 <= ord(letter) <= 90:  # if the letter given is a capital letter
            if (ord(letter) - key) < 65:  # if the modified letter is out of range -> ascii from 65 to 90
                new_letter = chr(ord(letter) - key + 26)  # there are 26 letters in the alphabet -> ascii value + 26
            else:
                new_letter = chr(ord(letter) - key)
            new_list.append(new_letter)

        elif 97 <= ord(letter) <= 122:  # if the letter given is not a capital letter
            if (ord(letter) - key) < 97:  # if the modified letter is out of range -> ascii from 97 to 122
                new_letter = chr(ord(letter) - key + 26)
            else:
                new_letter = chr(ord(letter) - key)
            new_list.append(new_letter)

        else:
            new_list.append(letter)  # if the given letter is not a letter -> no modifications required

    return new_text.join(new_list)


# ************************ QUESTION 3 **************************
### WRITE CODE HERE
def naive_break(text):
    """
    decrypts the text according to all the possible keys (1-26)
    there are 26 letters in the alphabet therefore there are 26 keys possible
    key 26 = key 0 -> no change to the text

    :param text: the text needed to decrypt
    :return: list that contains all 26 options of decryption
    """

    dec_opt = []  # list of options of the decrypted code. there are 26 options

    if len(text) == 0:  # if there is no text
        return ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    for i in range(26):  # i is the current key used to decrypt the text (0-25) 0 is like 26. with help from decrypt()
        dec_opt.append(decrypt(text, i))

    return dec_opt


# ************************ QUESTION 4.1 **************************
### WRITE CODE HERE
def find_common_letter(text):
    """
    counts the number of times a letter is in the text. capital and lower case letters are counted as one letter.

    :param text: in this text we search for the common letter. the text has at least one english letter
    :return: the common letter in the text in lower case
    """

    temp_text = list(text.lower())  # convert the text into a list that all the letters are lower case
    count_letter = [0 for _ in range(26)]  # keeps count of number of times a letter appears in text (index 0=a.. 25=z)

    for character in temp_text:  # counts how many times a character is in the text
        if 97 <= ord(character) <= 122:  # checks if the char is a letter
            count_letter[ord(character) % 97] += 1  # modulo by 97 to get the correct index

    return chr(count_letter.index(max(count_letter)) + 97)  # finds max num in list, then the char the index represents


# ************************ QUESTION 4.2 **************************
### WRITE CODE HERE
def frequency_break(text, common_letter):
    """
    decrypts the code using the most common letter in the original text.
    by comparing it to the most common letter in the encrypted text.

    the key is the number of jumps between the common letter in the original text and the common letter in the
    encrypted text.

    :param text: the encrypted text, has a least one english letter
    :param common_letter: most common letter in the original text
    :return: returns the decrypted text
    """

    key = ord(find_common_letter(text)) - ord(common_letter)

    if key < 0:  # the calculation of the key may return a negative number
        key += 26

    return decrypt(text, key)
