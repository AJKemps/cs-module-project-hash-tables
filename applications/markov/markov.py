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
