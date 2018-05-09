#check the datetime range
class DatetimeRange:
    def __init__(self, dt1, dt2):
        self.dt1 = dt1
        self.dt2 = dt2

    def __contains__(self, dt):
        if dt >= self.dt1 and dt <= self.dt2:
            return True
        else:
            return False


def roadmap(tasks, queries):
    process, start_date, end_date, people = [[],[],[],[]]
    result = []
    for task in tasks:
        process.append(task[0])
        start_date.append(task[1])
        end_date.append(task[2])
        people.append(task[3:])

    #find index
    for query in queries:
        tmp = []
        tmp_dict = {}
        matching_people, mathcing_date = query

        for i in people:
            #people check
            if matching_people in i:
                #find matching people process & date time check
                dt1, dt2, dt = start_date[people.index(i)], end_date[people.index(i)], mathcing_date
                if dt in DatetimeRange(dt1, dt2):
                    tmp_dict[process[people.index(i)]] = end_date[people.index(i)]

        #tmp sort with datetime
        for key, value in sorted(tmp_dict.iteritems(), key=lambda (k,v): (v,k)):
            tmp.append(key)

        result.append(tmp)
    return result

'''
tasks = [
["ITXJC","2017-09-05","2017-09-06","Reuben","Corey","Daxton"],
 ["KLFDO","2017-05-25","2017-09-06","Corey","Jenson","Kai"],
 ["ALFDO","2017-05-25","2017-09-06","Corey","Kai"],
 ["BLFDO","2017-05-25","2017-09-06","Corey","Jenson"]
]

queries = [
 ["Corey","2017-09-06"]
]
'''
roadmap(tasks, queries)
