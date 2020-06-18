from encryption import encryption
from decryption import decryption

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

# the inputs
plaintext = input()
queuesize = int(input())

# this isnt really important for gui but this initialises the queue
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

# if you want the encrypted output, the variable called binary has it
# ok finally plaintextoutput is the final answer, which should be the exact same as the input called plaintext
# the rest of the work dosent matter for gui i think, it all works using the encryption and decryption function