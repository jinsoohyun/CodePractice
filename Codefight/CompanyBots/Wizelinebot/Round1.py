def CreateNode(Id):
    return { 'id': Id, 'count': 0, 'childs': {} }

def dfs(node, deep, r):
    childsOrder = sorted([(node['childs'][d]['id'], d) for d in node['childs']])
    #print childsOrder
    for c in childsOrder:
        L = '--' * deep
        L += c[1] + ' (' + str(node['childs'][c[1]]['count']) + ')'
        r.append(L)
        dfs(node['childs'][c[1]], deep + 1, r)

def countAPI(calls):
    T = CreateNode(0)
    for call in calls:
        if call[0] == '/':
            call = call[1: ]
        u = call.split('/')
        print u
        node = T
        for x in u:
            if node['childs'].get(x) == None:
                node['childs'][x] = CreateNode(len(node['childs']))
            node = node['childs'][x]
            node['count'] += 1
    r = []
    dfs(T, 1, r)
    return r
