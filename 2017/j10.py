def main():
    f = open("./2017/j10.txt", 'r')
    data = f.read().replace('\n', '')
    entry = data.split(',')
    p1(entry)
    hash = p2(data)
    print(hash)


def p1(entry):
    nb = 256
    arr = [(x % nb) for x in range(nb)]
    skipSize = 0
    currentIndex = 0

    for data in entry:
        length = int(data)

        tmpArr = list(arr)
        for i in range(length):
            arrIndex = (currentIndex + length-i-1) % nb
            arr[(currentIndex+i) % nb] = tmpArr[arrIndex]

        currentIndex = (currentIndex + length + skipSize) % nb
        skipSize = skipSize + 1

    print(arr[0]*arr[1])


def p2(entry):
    nb = 256
    arr = [(x % nb) for x in range(nb)]
    skipSize = 0
    currentIndex = 0

    l = list(entry)
    entry = [ord(c) for c in l]
    entry.append(17)
    entry.append(31)
    entry.append(73)
    entry.append(47)
    entry.append(23)

    for t in range(64):
        for data in entry:
            length = int(data)

            tmpArr = list(arr)
            for i in range(length):
                arrIndex = (currentIndex + length-i-1) % nb
                arr[(currentIndex+i) % nb] = tmpArr[arrIndex]

            currentIndex = (currentIndex + length + skipSize) % nb
            skipSize = skipSize + 1
    dense = ''
    numerciDense = []
    step = 16
    for x in range(step):
        res = 0
        a = arr[x*step:x*step+step]
        for i in a:
            res = res ^ i
        numerciDense.append(res)

    for i in numerciDense:
        s = hex(i).replace("0x", "")
        if(i < 16):
            s = f'0{s}'
        dense = dense+s
    return dense


main()
