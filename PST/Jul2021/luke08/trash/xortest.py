#!/usr/bin/env python3

def main():
    key = "Frimerke"
    trianglePath = './triangle.png'
    encryptFile(trianglePath, key)


def encryptFile(path, key):
    file = open(path, 'rb')
    fileContents = file.read()
    file.close()

    fileContents = bytearray(fileContents)

    for index, value in enumerate(fileContents):
        fileContents[index] = value ^ key

    encryptedFile = open('encrypted.png', 'wb')
    encryptedFile.write(fileContents)
    encryptedFile.close()


if __name__ == '__main__':
    main()

