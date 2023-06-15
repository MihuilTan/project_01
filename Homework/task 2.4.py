# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    a = s.replace("!", " ")
    return a

print(remove_exclamation_marks("Hi! Hello!",))
print(remove_exclamation_marks(""))
print(remove_exclamation_marks("Oh, no!!!"))
# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == '!':
        b = s[:-1]
    else:
        b = s
    return b
print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi"))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
#import st
def remove_word_with_one_em(s):
    return ' '.join(w for w in s.split() if w.count('!') != 1)
    #s=("The food! is great!!!")
    #count=strs.count("!")-1
    #strs = strs.replace('!','',count)
    #print (strs)
print(remove_word_with_one_em("Hi!"))
print(remove_word_with_one_em("Hi! Hi!"))
print(remove_word_with_one_em("Hi! Hi! Hi!"))
print(remove_word_with_one_em("Hi Hi! Hi!"))
print(remove_word_with_one_em("Hi! !Hi Hi!"))
print(remove_word_with_one_em("Hi! Hi!! Hi!"))
print(remove_word_with_one_em("Hi! !Hi! Hi!"))

