#!/usr/bin/env python

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = uppercase.lower()

def rot13(message):
    return message.translate({ord(x): y for (x,y) in zip(lowercase + uppercase, lowercase[13:] + lowercase[:13] + uppercase[13:] + uppercase[:13])})

if __name__ == '__main__':
    message = input('Enter: ')
    print(rot13(message))
