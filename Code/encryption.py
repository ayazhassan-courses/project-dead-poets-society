def enqueue(lst, item, front, rear, queuesize):
    # there is an issue with scope here, i change front to 0 but it reverts to -1 when repeating the function to
    # enqueue more items
    print(front)
    if (rear+1) % queuesize == front:
        print('Error: Queue is full')
    elif front == -1:
        front = 0
        rear = 0
        lst[rear]=item
    else:
        rear = (rear + 1) % queuesize # we use mod because it is circular and not linear so if size is 5 and we move the
                                        # rear pointer to 6 it should go to the 'beginning'
        print(rear)
        lst[rear]=item
    print(front)
    # there are 3 cases here, first when the circular queue is full, second to initialise, third to normally enqueue

def dequeue(lst, front, rear, queuesize):
    if front == -1:
        print("Error: Queue is empty")
    elif front == rear:
        temp = lst[front]
        front = -1
        rear = -1
        return temp
    else:
        temp = lst[front]
        front = (front + 1) % queuesize
        return temp
    # same as enqueue


def frontt(lst):
    return lst[front]


def rear(lst):
    return lst[rear]


def display(lst, front, rear, queuesize):
    if front == -1:
        print("Error: Queue is empty")
    elif rear >= front:
        print("Elements in the circular queue are:", end = " ")
        for i in range(front, rear + 1):
            print(lst[i], end = " ")
        print()
    else:
        print ("Elements in the circular queue are:", end = " ")
        for i in range(front, queuesize):
            print(lst[i], end = " ")
        for i in range(0, rear + 1):
            print(lst[i], end = " ")
        print()
    if ((rear + 1) % queuesize == front):
        print("Error: Queue is Full")

    # to display the elements in the queue
''''''


# queuesize = int(input())
# front = -1
# rear = -1
# queue = []
#
# for i in range(queuesize):
#     queue.append([])

# for i in range(len(plaintext)):
#     enqueue(queue, plaintext[i], front, rear, queuesize)

# print(queue)

''''''


plaintext = input()

def encryption(plaintext):
    cyphertext = ''
    asci = []
    declist = []

    # plaintext is converted letter by letter to binary
    for i in plaintext:
        asci.append(bin(ord(i))[0]+bin(ord(i))[2:])

   # this step is pending but in it we xor the binary with another 8 bit binary code we get from the circular queue

    # now theres an 8 bit number thats been xor'd, we will convert it back to decimal

    for i in asci:
        decimal = 0
        for j in range((len(i))):
            last = i[j]
            f = len(i)-1-j
            if last == '1':
                decimal = decimal + 2**f
        declist.append(decimal-80) # since we should have had xor'd it, the number would be small enough where every
                                    # ascii character would be represented in 8 bit but since we havent managed to do
                                    # that, for now i will manually reduce the value of the decimal so it is not
                                    # all '11111111'

    #declist is the decimal list now the decimals need to be put in a fibonacci series, i made this without
    # using any theorem, but it works
    print(declist)
    fibonacci = [21, 13, 8, 5, 3, 2, 1, 1]
    binary = ['0'*8 for i in range(len(declist))]

    for i in range(len(declist)):
        number = declist[i]
        sum = 0
        for j in range(len(fibonacci)):
            if fibonacci[j]<=number and (sum+fibonacci[j]) <= number:
                sum += fibonacci[j]
                binary[i]=binary[i][:j]+'1'+binary[i][j+1:]

    #while the name is binary, this is not base 2, it is fibonacci series representation

    return binary

''''''
#decryption is the same just the opposite way around

def decryption(binary):

    dec = 0
    declist = []
    fibonacci = [21, 13, 8, 5, 3, 2, 1, 1]
    for i in binary:
        idk = str(i)
        for j in range(len(idk)):
            if idk[j] == '1':
                dec += fibonacci[j]
        declist.append(dec)

    for i in declist:
        binlist.append(bin(ord(i))[0]+bin(ord(i))[2:])

    # XOR step with Keywords that has not been done yet

    xoroutput = []

    xoroutput = binlist
    final = []

    for i in xoroutput:
        decimal = 0
        for j in range((len(i))):
            last = i[j]
            f = len(i) - 1 - j
            if last == '1':
                decimal = decimal + 2 ** f
        declist.append(decimal)

    for i in decllist:
        final.append(chr(i))

    return final

print(encryption(plaintext))

# print(decryption(binary))

