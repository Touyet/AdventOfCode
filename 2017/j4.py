from tools.utils import List


def main():
    f = open("./2017/j4.txt", 'r')
    data: list[str] = f.read().splitlines()

    res = p2(data)

    print(res)


def p2(lines: "list[str]"):
    valid = 0
    for line in lines:
        words: List[str] = List(line.split())
        isValid = True
        for word in words:
            if(len(words.filter(lambda v: v == word)) > 1):
                isValid = False
                break
            anagram = words.find(
                lambda v: v != word and isAnagram(v, word))
            if(anagram is not None):
                isValid = False
                break
        if(isValid is True):
            valid = valid+1
    return valid


def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)


main()
