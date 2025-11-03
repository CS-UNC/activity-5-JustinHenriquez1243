"""
words_file = open('CROSSWD.txt','r')

for k in dir(words_file):
    if'__' not in k:
        print(k)
        """
def more_than_20(f):
    filee = open(f)
    list = []
    count = 0
    for i in filee:
        word = i.strip()
        if len(word) > 20:
            list.append(word)
    return list

def has_no_e(word):
    if "e" in word:
        return False
    else:
        return True
    
def uses_only(word,letters):
    for x in word:
        if x not in letters:
            return False
    return True

# print(more_than_20('CROSSWD.txt'))
def all_uses_only(file, letters):
    opened_file = open(file)
    list = []
    for i in opened_file:
        word = i.strip()
        if uses_only(word,letters):
            list.append(word)
    return list