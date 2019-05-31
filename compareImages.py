
from PIL import Image
import glob


def dhash(image, hashSize = 8):

    image = image.convert('L').resize(
            (hashSize + 1, hashSize),
          Image.ANTIALIAS,
        )

    difference = []
    for row in xrange(hashSize):
         for col in xrange(hashSize):
              pixelLeft = image.getpixel((col, row))
              pixelRight = image.getpixel((col + 1, row))
              difference.append(pixelLeft > pixelRight)

    decimalValue = 0
    hexString = []
    for index, value in enumerate(difference):
        if value:
            decimalValue += 2 ** (index % 8)
        if (index % 8) == 7:
             hexString.append(hex(decimalValue)[2:].rjust(2, '0'))
             decimalValue = 0
    return ''.join(hexString)


def hamdist(str1, str2):
    return len(list(filter(lambda x: ord(x[0]) ^ ord(x[1]), zip(str1, str2))))

def main():
    folderPath = "dev_dataset" #path to file
    dictionaryHash = {}
    for filepath in glob.iglob(folderPath+'/*.jpg'):
        orig = Image.open(filepath)
        d = {filepath: dhash(orig)}
        dictionaryHash.update(d)

    lst = list()

    for i, k in dictionaryHash.items():
        for j, m in dictionaryHash.items():

            if ((hamdist(k, m) < 12) and i!=j):
                 lst.append((i,j))

    data = {tuple(sorted(item)) for item in lst}
    for i in data:
        print(i)

if __name__ == '__main__':
    main()
