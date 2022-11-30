from tools.utils import List


def main():
    data = ""
    with open('./2021/j6.txt', 'r') as f:
        data = f.read()

    input = data.split(',')  # data.split(',')
    days = 256
    currentDay = 0
    inputInt = []
    for i in input:
        inputInt.append(int(i))

    while currentDay < days:
        nextInput = [8 for x in range(inputInt.count(0))]
        inputInt = [x-1 if x > 0 else 6 for x in inputInt]
        inputInt += nextInput
        currentDay += 1

    print(len(inputInt))


def calc_growth(fish, days):
    day_fish = []
    for f in range(9):
        day_fish.append(fish.count(f))
    for i in range(days):
        next_day_fish = day_fish[1:] + day_fish[:1]
        next_day_fish[6] += day_fish[0]
        day_fish = next_day_fish
    return sum(day_fish)


fish = List([f for f in open("./2021/j6.txt").read().split(",")])

print(calc_growth(fish, 80))
print(calc_growth(fish, 256))
