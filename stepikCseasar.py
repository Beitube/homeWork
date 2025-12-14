def caesar_cipher(text, shift):
    if not text.isalpha():
        return text
    
    is_upper = text.isupper()
    char = text.lower()

    shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    
    return shifted.upper() if is_upper else shifted

def encrypt_string(s):
    words = s.split(' ')
    encrypted_words = []
    
    for word in words:
        word_length = sum(1 for c in word if c.isalpha())
        
        if word_length == 0:
            encrypted_words.append(word)
            continue
        
        encrypted_word = ''.join(caesar_cipher(c, word_length) for c in word)
        encrypted_words.append(encrypted_word)
    
    return ' '.join(encrypted_words)

text = input()

result = encrypt_string(text)
print(result)
