import random

with open("profanity_dict.txt", 'r') as file:
    profanity_words=file.read().splitlines()

vowels="aeiou"

first_consonants=['B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Z',"Bl", "Cl", "Fl", "Gl", "Pl",
"Sl", "Br", "Cr", "Dr", "Fr", "Gr", "Pr", "Tr", "Sk", "Sm", "Sn",
"Sp", "St", "Sw", "Tw",'Sh', 'Ch','Th']

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

def gen_word():
    while True:
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
            return word

#sp a z  e r
#v  a r  i a
#n  u pt u p

if __name__=="__main__":
    for i in range(40):
        print(gen_word())