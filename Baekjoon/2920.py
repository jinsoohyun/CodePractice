#Exercise 2920
Data = raw_input("").replace(' ','').strip()
dic = {'12345678':'ascending','87654321':'descending'}
try:
    if dic[Data]:
        print dic[Data]
except:
    print "mixed"

#ascending, descending, mixed
#1 2 3 4 5 6 7 8
