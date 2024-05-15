
""" 
Many different approaches I saw, lots of new methods in Python. Want to come back to this and re-read/ re-implement these solutions from scratch
#######################################
def caesarCipher(s, k):
    result = ''
    for char in s:
        if char.isalpha():
            # Determine the offset based on the case of the character
            offset = ord('a') if char.islower() else ord('A')
            # Apply the Caesar cipher transformation
            result += chr((ord(char) - offset + k) % 26 + offset)
        else:
            # If the character is not a letter, keep it unchanged
            result += char
    return result
#######################################
def cipher(shift, text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    def newchar(char):
        index = alphabet.find(char) + shift
        return alphabet[index % 26]
    return ''.join(map(newchar, text.lower()))

    #######################################
    def caesarCipher(s, k):
    lowercase_trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'[k:] + 'abcdefghijklmnopqrstuvwxyz'[:k])
    uppercase_trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[k:] + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:k])
    return s.translate(lowercase_trans).translate(uppercase_trans)

s = "Hello, World!"
k = 3
encrypted = caesarCipher(s, k)
print("Original:", s)
print("Encrypted:", encrypted)
 """