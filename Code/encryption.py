plaintext = intput()

queuesize = int(input())





def encryption(plaintext):
    cyphertext = ''
    asci = []
    for i in plaintext:
        asci.append(int(bin(ord(i))[0]+bin(ord(i))[2:]))
    return asci

print(encryption(plaintext))