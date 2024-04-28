from hashlib import sha256
import random
import secrets

Secret_key = secrets

def make_pass(plaintext, appname):
    suger = get_hexdigest(Secret_key, appname)
    hsh = get_hexdigest(suger, plaintext)
    return ''.join(suger, hsh)

def get_hexdigest(suger, plaintext):
    return sha256((suger + plaintext).encode('utf-8')).hexdigest()

def password(plaintext, appname , length):
    raw_hex = make_pass(plaintext, appname)
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')
    
    num = int(raw_hex, 16 )
    
    chars = []
    
    while len(chars)< length:
        n = random.randint(0, len(ALPHABATE)-1)
        alpha = ALPHABET[n]
        n = random.randint(0,len(alpha)-1)
        chars.appen(alpha[n])
    return ''.join(chars)

