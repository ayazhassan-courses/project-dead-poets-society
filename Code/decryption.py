def decryption(binary, keyasci):


    declist = []
    binlist = []
    xoroutput = []
    fibonacci = [55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

    for i in binary:
        idk = i
        dec = 0
        for j in range(len(idk)):
            if idk[j] == '1':
                dec += fibonacci[j]
        declist.append(dec)

    for i in declist:
        binlist.append(bin(i)[0]+bin(i)[2:])
    for i in range(len(binlist)):
        if len(binlist[i])!=len(keyasci[i]):
            while len(binlist[i])!=len(keyasci[i]):
                if len(binlist[i])>len(keyasci[i]):
                    keyasci[i]='0'+keyasci[i]
                else:
                    binlist[i]='0'+binlist[i]


    # XOR step with Keywords that has not been done yet
    for i in range(len(binlist)):
        a = keyasci[i]
        b = binlist[i]
        y = int(a, 2) ^ int(b, 2)
        xoroutput.append(bin(y)[2:].zfill(len(a)))


    temp = []
    final = []

    for i in xoroutput:
        decimal = 0
        for j in range((len(i))):
            last = i[j]
            f = len(i) - 1 - j
            if last == '1':
                decimal = decimal + 2 ** f
        temp.append(decimal)

    for i in temp:
        final.append(chr(i))

    return final
