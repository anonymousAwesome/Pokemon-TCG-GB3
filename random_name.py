import random

with open("profanity_dict.txt", 'r') as file:
    profanity_words=file.read().splitlines()

vowels="aeiou"

first_consonants=['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
'p', 'r', 's', 't', 'v', 'w', 'x', 'z',"bl", "cl", "fl", "gl", "pl",
"sl", "br", "cr", "dr", "fr", "gr", "pr", "tr", "sc", "sk", "sm", "sn",
"sp", "st", "sw", "tw",'sh', 'ch','th']

second_consonants=['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
'p', 'r', 's', 't', 'v', 'w', 'x', 'z',"bb","bl", "cl", "fl", "gg","gl", "pl",
"sl", "br", "cr", "dr", "fr", "gr", "pr", "pt", "tr", "sc", "sk", "sm", "sn",
"sp", "st", "sw", "tw",'sh', 'ch','th','ng', 'nt', 'rs', 'll', 'ns', 'ss',
'nd', 'nk', 'ct', 'tt', 'rt', 'ck', 'rr']

third_consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
'p', 'r', 's', 't', 'v', 'w', 'x', 'z',"bl", "cl", "fl", "gl", "pl",
"sk", "sp", "st", 'sh', 'ch','th','ng', 'nt', 'rs', 'll', 'ns', 'ss',
'nd', 'nk', 'ct', 'tt', 'rt', 'ck', 'rr']


#Note: the lists *are* different from each other.
#Don't combine them.

def word_is_safe(string):
        return not any(word in string for word in profanity_words)

for i in range(40):
    word=""
    word+=random.choice(first_consonants)
    word+=random.choice(vowels)
    word+=random.choice(second_consonants)
    word+=random.choice(vowels)
    if random.randint(0,1):
        word+=random.choice(vowels)
    if random.randint(0,1):
        word+=random.choice(third_consonants)
    if len(word)==4 and word[3]=="e":
        word+="h"
    if word_is_safe(word):
        print(word)

#sp a z  e r
#v  a r  i a
#n  u pt u p