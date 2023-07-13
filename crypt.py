from twofish import Twofish

def tfencrypt(data: str, password: str) -> bytes:
    bs = 16 #block size 16 bytes or 128 bits
    plaintext = data

    if len(plaintext) % bs: #add padding 
	    padded_plaintext = str(plaintext + '%' * (bs - len(plaintext) % bs)).encode('utf-8')
    else:
	    padded_plaintext=plaintext.encode('utf-8')

    T = Twofish(str.encode(password))
    ciphertext = b''
    for x in range(int(len(padded_plaintext) / bs)):
	    ciphertext += T.encrypt(padded_plaintext[x * bs: ( x+ 1) * bs])

    return ciphertext

def tfdecrypt(data_bin: bytes, password: str) -> bytes:
    bs = 16 #block size 16 bytes or 128 bits
    ciphertext = data_bin
    T = Twofish(str.encode(password))
    plaintext = b''

    for x in range(int(len(ciphertext) / bs)):
        plaintext += T.decrypt(ciphertext[x * bs: (x + 1) * bs])

    return str.encode(plaintext.decode('utf-8').strip('%'))

if __name__ == "__main__":
    password = ')BCZvH9LE!^!X%4ZnMcRqc^Fj%4z!VL&'
    crypted = tfencrypt("Test", password)

    print("First stage:", crypted)
    # crypted = tfencrypt(crypted.decode("utf-8"), password)
    # print("Second stage:", crypted)
    # encrypted = tfdecrypt(crypted, password)
    # print("First encrypt stage:", encrypted)
    # encrypted = tfdecrypt(crypted, password)
    # print("Second encrypt stage:", encrypted)

# with open('infile.txt', 'r') as infile, open('outfile.txt', 'wb') as outfile:
#     tfencrypt(infile, outfile, password)

# with open('outfile.txt', 'rb') as infile, open('outfile_decrypted.txt', 'wb') as outfile:
#     tfdecrypt(infile, outfile, password)
