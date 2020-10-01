import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()


# TODO: analyze which words can follow other words
# Your code here

print(words)

markov = {}

for i in range(len(words)-1):
    if words[i] not in markov:
        markov[words[i]] = {words[i+1]}
    if words[i] in markov:
        markov[words[i]] = {*markov[words[i]], words[i+1]}

for k, v in sorted(markov.items(), key=lambda item: item[0]):
    print(f'{k}: {v}')


# TODO: construct 5 random sentences
# Your code here

def create_sentence(dict):

    count = 0
    sentence_count = 0
    s = []
    finished = False

    while not finished:
        if count == 0:
            word = random.choice(list(dict))
            print(word, count)
            print(word[0].isupper())
            print()

            if word[0] == '"' or word[0].isupper():
                s.append(word)
                count += 1
        if count > 0:
            new_word = random.choice(list(dict[s[count-1]]))
            print(new_word, count)

            if new_word[-1] == '.' or new_word[-1] == '!' or new_word[-1] == '?' or (new_word[-1] == '"' and new_word[-2] == '.') or (new_word[-1] == '"' and new_word[-2] == '!') or (new_word[-1] == '"' and new_word[-2] == '?'):
                s.append(new_word)
                sentence_count += 1
                if sentence_count == 4:
                    finished = True
                if sentence_count < 4:
                    count = 0

            else:
                s.append(new_word)
                count += 1

    if finished:
        return ' '.join(s)


print(create_sentence(markov))
