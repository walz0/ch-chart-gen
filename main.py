# https://stackoverflow.com/questions/46759492/syllable-count-in-python
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def mark_syllables(word):
    word = word.lower()
    syllables = {}
    vowels = "aeiouy"
    # consonants that continue the syllable
    cont_consonants = "cerx"
    if word[0] in vowels:
        # count += 1
        syllables[0] = word[0]
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            # count += 1
            if index < len(word) - 1:
                if word[index+1] in cont_consonants:
                    syllables[index+1] = word[index+1]
                    continue
            syllables[index] = word[index]

    # return word if there is only 1 syllable
    if len(syllables) == 0:
        return word

    output = ""
    # place syllable markers
    prev = 0
    for i in range(len(list(syllables.keys()))):
        index = list(syllables.keys())[i]
        if i == len(list(syllables.keys())) - 1:
            output += word[prev:len(word)]
            continue
        output += word[prev:index+1] + "-"
        prev = index+1

    return output

print(mark_syllables("fisherman"))
print(mark_syllables("supercalifragilisticexpialidocious"))
print(mark_syllables("poop"))