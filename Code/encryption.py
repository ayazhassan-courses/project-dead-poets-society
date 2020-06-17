def encryption(plaintext, keyasci):
    asci = []
    declist = []

    # plaintext is converted letter by letter to binary
    for i in plaintext:
        asci.append(bin(ord(i))[0]+bin(ord(i))[2:])

   # this step is pending but in it we xor the binary with another 8 bit binary code we get from the circular queue

    xored = []


    for i in range(len(asci)):
        a = asci[i]
        b = keyasci[i]
        y = int(a, 2) ^ int(b, 2)
        xored.append(bin(y)[2:].zfill(len(a)))


    # now theres an 8 bit number thats been xor'd, we will convert it back to decimal

    for i in xored:
        decimal = 0
        for j in range((len(i))):
            last = i[j]
            f = len(i)-1-j
            if last == '1':
                decimal = decimal + 2**f
        declist.append(decimal)



    #declist is the decimal list now the decimals need to be put in a fibonacci series, i made this without
    # using any theorem, but it works
    # print(declist)
    # print(queue)
    fibonacci = [55, 34, 21, 13, 8, 5, 3, 2, 1, 1]
    binary = ['0'*10 for i in range(len(declist))]

    for i in range(len(declist)):
        number = declist[i]
        sum = 0
        for j in range(len(fibonacci)):
            if fibonacci[j]<=number and (sum+fibonacci[j]) <= number:
                sum += fibonacci[j]
                binary[i]=binary[i][:j]+'1'+binary[i][j+1:]

    #while the name is binary, this is not base 2, it is fibonacci series representation

    return binary

