import tkinter as gui
from encryption import encryption
from decryption import decryption
global plaintext
global queuesize
global button 
plaintext = ''
queuesize = 0

def enqueue(lst, item, front, rear, queuesize):

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
        lst[front][0]=''
        front = -1
        rear = -1

    else:
        lst[front][0] = ''
        front = (front + 1) % queuesize

    return front, rear
    # same as enqueue


''''''
# ok this is all thats important for u i think @shayan

def take_input(input):  # this is whats called when the buttons are pressed, it takes the inputs and stores them in those variable
    button = str(input)
    plaintext = textbox.get()
    queuesize = int(keybox.get())
    if queuesize<len(plaintext):
        while queuesize<len(plaintext):
            print('The size of the queue has to be bigger than the input')
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
    # if the queue is longer than 26, it will just have x as the keyword

    for i in range(queuesize):
        queue.append(['', letters[i]])

    # the initialisation is done, now its using the input to enqueue in the queue

    for i in range(len(plaintext)):
        front, rear = enqueue(queue, plaintext[i], front, rear, queuesize)
    # using the queue for encryption
    keywords = [i[1] for i in queue]
    for i in keywords:
        keyasci.append(bin(ord(i))[0] + bin(ord(i))[2:])


    ''''''
    binary = encryption(plaintext, keyasci)

    word = decryption(binary, keyasci)

    plaintextoutput = ''
    for i in word:
        plaintextoutput+=i


    for i in range(len(plaintext)):
        front, rear = dequeue(queue, front, rear, queuesize)
    output = ""

    if button == 'e':  # this is to just decide if we wanna output the encrypted text or the decrypted text
        output = binary
    elif button == 'd':
        output = plaintextoutput

    outputbox['text'] = output

    # the problem is binary and plaintextoutput both get defined at the end so thats the error we have to fix

button = ''

root = gui.Tk()

canvas = gui.Canvas(root, height=600, width=800)
canvas.pack()

frame = gui.Frame(root, bg='#aed6f1', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

EncryptButton = gui.Button(frame, text="Encrypt Text", command=lambda: take_input('e'))
EncryptButton.place(relx=0.7, relwidth=0.3, relheight=0.5)

DecryptButton = gui.Button(frame, text="Decrypt Text", command=lambda: take_input('d'))
DecryptButton.place(relx=0.7, rely=0.55, relwidth=0.3, relheight=0.5)

textbox = gui.Entry(frame)
textbox.place(relx=0, rely=0, relwidth=0.65, relheight=1)

keyframe = gui.Frame(root, bg='#aed6f1', bd=4)
keyframe.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.075, anchor='n')

keybox = gui.Entry(keyframe)
keybox.place(relx=0, rely=0, relwidth=0.65, relheight=1)

result = gui.Frame(root, bg='#aed6f1', bd=10)
result.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

outputbox = gui.Label(result, anchor="nw", justify='left', bd=4)
outputbox.place(relwidth=1, relheight=1)


# the inputs
# plaintext = input()
# queuesize = int(input())

# this isnt really important for gui but this initialises the queue

root.mainloop()





# if you want the encrypted output, the variable called binary has it
# ok finally plaintextoutput is the final answer, which should be the exact same as the input called plaintext
# the rest of the work dosent matter for gui i think, it all works using the encryption and decryption function