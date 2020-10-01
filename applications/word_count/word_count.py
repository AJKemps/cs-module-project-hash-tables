ignore = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\",
          "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]


def remove_char(s):

    word = s

    for item in ignore:
        word = word.replace(item, "")

    return word


def word_count(s):
    # Your code here

    words = s.lower().split()
    fixed_words = []
    words_count = {}

    for word in words:
        fixed_word = remove_char(word)
        fixed_words.append(fixed_word)

    for word in fixed_words:
        if word not in words_count:
            words_count[word] = 0
        count = fixed_words.count(word)
        words_count[word] = count

    if len(fixed_words) > 0:
        if fixed_words[0] == "":
            return {}
    print(words_count)
    return words_count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))


def word_count(s):
    # $%$Start
    tr = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    s = s.translate(tr).lower()
    words = s.split()
    counts = {}
    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1
    return counts


    # $%$End
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
