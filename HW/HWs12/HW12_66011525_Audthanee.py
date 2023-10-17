#Q1----------------------------------------------------------------------------------------------------------------------------------------------

listtext = {"be":'b', "because":"cuz", "see":'c', "the":"da", "okay":"ok", "are":'r', "you":'u', "without":"w/o", "why":'y', "see you":"cu", "ate":'8', "great":"gr8", "mate":"m8", "wait":"w8", "later":"l8r", "tomorrow":"2mro", "for":'4', "before":"b4", "once":"1ce", "and":'&', "Your, You're":"ur", "As far as i know":"afaik", "As soon as possible":"ASAP", "At the moment":"atm", "Be right back":"brb", "By the way":"btw", "For your information":"FYI", "In my humble opinion":"imho", "In my opinion":"imo", "Laughing out loud":"lol", "Oh my god":"omg", "Rolling on the floor laughing":"rofl", "Talk to you later":"ttyl"}
#format = {long : short}

def textese(s):
    words = s.split()
    nword = []
    i = 0
    while i < len(words):
        phrase = ' '.join(words[i:i+3]).lower()
        if phrase in listtext:
            nword.append(listtext[phrase])
            i += 3
        elif words[i].lower() in listtext:
            nword.append(listtext[words[i].lower()])
            i += 1
        else:
            nword.append(words[i])
            i += 1
    return ' '.join(nword)


def untextese(s):
    words = s.split()
    for i in range(len(words)):
        if words[i] in listtext.values():
            k = next(key for key, value in listtext.items() if value == words[i])
            words[i] = k
    return ' '.join(words)


# Example usage
input_text = "for dictionary because we need to knowing it's okay to do"
output_text = textese(input_text)
output_text1 = untextese(output_text)

print(output_text)
print(output_text1)

#Q2----------------------------------------------------------------------------------------------------------------------------------------------

dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1', 'q':'2', 'r':'3'}

def composite(l1, l2):
    newdict = {}
    for i in l1:
        if l1.get(i) in l2:
            newdict[i] = l2.get(l1.get(i))

    return newdict


a = composite(dict1, dict2)
print(a)

#Q3----------------------------------------------------------------------------------------------------------------------------------------------

s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*i):
    if not i:
        return [()]
    res = [()]
    for current_set in i:
        temp_res = []
        for item in current_set:
            for prod in res:
                temp_res.append(prod + (item,))
        res = temp_res
    return res


print(product(s1,s2))
print()
print(product(s1,s2,s3))
print()
print(product(s1))