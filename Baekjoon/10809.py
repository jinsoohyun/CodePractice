#Exercise 10809
import string
Word = raw_input('')

for i in string.lowercase:
    try:
        print Word.index(i),
    except:
        print '-1',
