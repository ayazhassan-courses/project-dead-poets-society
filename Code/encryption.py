# def enqueue(lst, item, front, rear, queuesize):
#     print(front)
#     if (rear+1) % queuesize == front:
#         print('Error: Queue is full')
#     elif front == -1:
#         front = 0
#         rear = 0
#         lst[rear]=item
#     else:
#         rear = (rear + 1) % queuesize
#         print(rear)
#         lst[rear]=item
#     print(front)
#
#
# def dequeue(lst, front, rear, queuesize):
#     if front == -1:
#         print("Error: Queue is empty")
#     elif front == rear:
#         temp = lst[front]
#         front = -1
#         rear = -1
#         return temp
#     else:
#         temp = lst[front]
#         front = (front + 1) % queuesize
#         return temp
#
#
# def front(lst):
#     return lst[front]
#
#
# def rear(lst):
#     return lst[rear]
#
#
# def display(lst, front, rear, queuesize):
#     if front == -1:
#         print("Error: Queue is empty")
#     elif rear >= front:
#         print("Elements in the circular queue are:", end = " ")
#         for i in range(front, rear + 1):
#             print(lst[i], end = " ")
#         print()
#     else:
#         print ("Elements in the circular queue are:", end = " ")
#         for i in range(front, queuesize):
#             print(lst[i], end = " ")
#         for i in range(0, rear + 1):
#             print(lst[i], end = " ")
#         print()
#
#     if ((rear + 1) % queuesize == front):
#         print("Error: Queue is Full")
#
#
plaintext = input()
# queuesize = int(input())
# front = -1
# rear = -1
# queue = []
#
# for i in range(queuesize):
#     queue.append([])
#
# for i in range(len(plaintext)):
#     enqueue(queue, plaintext[i], front, rear, queuesize)
#
# print(display(queue, front, rear, queuesize))



def encryption(plaintext):
    cyphertext = ''
    asci = []
    declist = []
    for i in plaintext:
        asci.append(bin(ord(i))[0]+bin(ord(i))[2:])

    # idk how to add to circular queue and do that step

    # now theres an 8 bit number thats been xor'd

    for i in asci:
        decimal = 0
        for j in range((len(i))):
            last = i[j]
            f = len(i)-1-j
            if last == '1':
                decimal = decimal + 2**f
        declist.append(decimal)

    #declist is the decimal list now the decimals need to be put in a fibonacci series

    
    return declist


print(encryption(plaintext))

