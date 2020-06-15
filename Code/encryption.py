def test_func(testtext):
    print(testtext)
    #to output the decrypted/encrypted text, add that next line and set it equal to whatever the respective function outputs
    #instead of 'test output'
    
    outputbox['text'] = 'test output'

import tkinter as gui

root = gui.Tk()


canvas = gui.Canvas(root, height = 600, width = 800)
canvas.pack()

frame = gui.Frame(root, bg= '#aed6f1', bd=5)
frame.place( relx = 0.5, rely = 0.1, relwidth= 0.75, relheight = 0.1, anchor='n')

EncryptButton = gui.Button(frame, text= "Encrypt Text", command=lambda: test_func(textbox.get()))
EncryptButton.place(relx = 0.7, relwidth =0.3, relheight= 0.5 )
#for both encryption and decryption buttons just replace the test func with the respective functions

DecryptButton = gui.Button(frame, text= "Decrypt Text", command=lambda: test_func(textbox.get()))
DecryptButton.place(relx = 0.7, rely =0.55 ,relwidth =0.3, relheight= 0.5 )

textbox = gui.Entry(frame)
textbox.place(relx = 0, rely = 0, relwidth= 0.65, relheight = 1)

result = gui.Frame(root,bg= '#aed6f1', bd=10)
result.place(relx=0.5, rely= 0.25, relwidth =0.75, relheight = 0.6, anchor='n')

outputbox = gui.Label(result, anchor="nw", justify='left', bd=4)
outputbox.place(relwidth=1 ,relheight= 1)

root.mainloop()


def enqueue(lst, item, front, rear, queuesize):
    # there is an issue with scope here, i change front to 0 but it reverts to -1 when repeating the function to
    # enqueue more items
    if (rear+1) % queuesize == front:
        print('Error: Queue is full')
    elif front == -1:
        front = 0
        rear = 0
        lst[rear][0]=item
    else:
        rear = (rear + 1) % queuesize # we use mod because it is circular and not linear so if size is 5 and we move the
                                        # rear pointer to 6 it should go to the 'beginning'
        lst[rear][0]=item
    # there are 3 cases here, first when the circular queue is full, second to initialise, third to normally enqueue
    return front, rear

def dequeue(lst, front, rear, queuesize):
    if front == -1:
        print("Error: Queue is empty")
    elif front == rear:
        temp = lst[front][0]
        front = -1
        rear = -1
        return temp
    else:
        temp = lst[front][0]
        front = (front + 1) % queuesize
        return temp
    return front, rear
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

plaintext = input()
queuesize = int(input())
front = -1
rear = -1
queue = []
keyasci = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if queuesize > 26:
    x = queuesize-26
x = queuesize
for i in range(x):
    letters.append('x')


for i in range(queuesize):
    queue.append(['', letters[i]])

for i in range(len(plaintext)):
    front, rear = enqueue(queue, plaintext[i], front, rear, queuesize)

keywords = [i[1] for i in queue]
for i in keywords:
    keyasci.append(bin(ord(i))[0] + bin(ord(i))[2:])


''''''


def encryption(plaintext, queue):
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

''''''
#decryption is the same just the opposite way around

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
    for i in range(len(keyasci)):
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

binary = encryption(plaintext, queue)

print(decryption(binary, keyasci))

