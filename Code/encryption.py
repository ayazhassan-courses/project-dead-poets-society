def enqueue(lst, item):
    lst.append(item)


def dequeue(lst):
    return lst.pop(0)


def front(lst):
    return lst[0]


def rear(lst):
    return lst[-1]


def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


plaintext = input()

queuesize = int(input())



def encryption(plaintext):
    cyphertext = ''
    asci = []
    for i in plaintext:
        asci.append(int(bin(ord(i))[0]+bin(ord(i))[2:]))
    return asci

print(encryption(plaintext))