def no_dups(s):
    # Your code here

    words = s.split()
    word_dict = {}
    order = 0

    for word in words:
        if word not in word_dict:
            word_dict[word] = order
            order += 1

    list1 = []

    for k, v in word_dict.items():
        list1.append(k)

    listToStr = ' '.join(list1)

    print(listToStr)

    return listToStr


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
