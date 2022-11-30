from tools.utils import List


def main():
    f = open("./2018/j4.txt", 'r')
    data: list[str] = f.read().replace('[', '').replace(
        ']', '').replace('Guard', '').replace('shift', '').replace('begins', '').replace('#', '').splitlines()
    data.sort()
    res = p1(data)
    print(res)
    res = p2(data)
    print(res)


def p1(data: "list[str]"):
    d: List[Guard] = List()
    previousGuard = None
    for line in data:
        asleep = "falls asleep" in line
        awake = "wakes up" in line
        input = line.split()
        hour, min = input[1].split(':')

        if(asleep):
            previousGuard.sleep(int(min))
        elif(awake):
            previousGuard.wake(int(min))
        else:
            previousGuard = d.find(lambda v: v.id == int(input[2]))
            if(previousGuard is None):
                previousGuard = Guard(int(input[2]))
                d.append(previousGuard)

    maxMin = max(d.map(lambda v: v.minuteSleeping))
    lazyGuard = d.find(lambda v: v.minuteSleeping == maxMin)

    res = -1
    resMin = 0
    for cnt in lazyGuard.minuteCount.keys():
        val = lazyGuard.minuteCount[cnt]
        if(val > res):
            res = val
            resMin = cnt
    return resMin * lazyGuard.id


def p2(data: "list[str]"):
    d: List[Guard] = List()
    previousGuard = None
    for line in data:
        asleep = "falls asleep" in line
        awake = "wakes up" in line
        input = line.split()
        hour, min = input[1].split(':')

        if(asleep):
            previousGuard.sleep(int(min))
        elif(awake):
            previousGuard.wake(int(min))
        else:
            previousGuard = d.find(lambda v: v.id == int(input[2]))
            if(previousGuard is None):
                previousGuard = Guard(int(input[2]))
                d.append(previousGuard)

    res = -1
    resMin = 0
    id = 0

    for guard in d:
        for min in guard.minuteCount.keys():
            cnt = guard.minuteCount[min]
            if(cnt > res):
                id = guard.id
                resMin = min
                res = cnt
    return resMin * id


class Guard:
    def __init__(self, id: int) -> None:
        self.id = id
        self.minuteSleeping = 0
        self.lastSleepingMinute = 0
        self.minuteCount = {}

    def sleep(self, min: int):
        self.lastSleepingMinute = min

    def wake(self, min: int):
        self.minuteSleeping = self.minuteSleeping + min - self.lastSleepingMinute - 1
        for i in range(self.lastSleepingMinute, min):
            if(i in self.minuteCount):
                self.minuteCount[i] = self.minuteCount[i]+1
            else:
                self.minuteCount[i] = 1
        self.lastSleepingMinute = 0


main()
