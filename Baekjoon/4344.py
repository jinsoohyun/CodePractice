testCase = input('')
CaseList = []

for i in range(testCase):
    CaseList.append(raw_input(''))

def get_AVG(ArrayList, aver):
    result = []
    for i in ArrayList:
        if float(i) > float(aver):
            result.append(i)
    return '%.3f'%((float(len(result))/len(ArrayList))*100)



for k in CaseList:
    k = k.split(' ')
    n = int(k[0])
    HeightList = map(int, k[1::])
    average = '%.3f'%(float(sum(HeightList))/len(HeightList))
    print get_AVG(HeightList, average)+"%"
