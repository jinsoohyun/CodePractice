def chatBot(conversations, currentConversation):
    best_conversation = None
    best_match_count = 0
    current_words = set(currentConversation)

    for conversation in conversations:
        conversation_words = set(conversation)
        match_count = sum([word in conversation_words for word in current_words])

        if match_count > best_match_count:
            best_match_count = match_count
            best_conversation = conversation

    if best_conversation is None:

        return currentConversation

    last_match = max([i for i in range(len(best_conversation)) if [best_conversation[i] in currentConversation]])

    if last_match == len(best_conversation)-1:

        return currentConversation
    return currentConversation+best_conversation[last_match+1:]

'''
def is_unique(word,wlist):
    nb = 0
    for w in wlist:
        if w == word:
            nb = nb+1
    if nb == 1:
        return True
    return False

def find_max(conversations_stats):
    maxs = conversations_stats[0]
    ind_max = 0
    for x in range(1,len(conversations_stats)):
        if conversations_stats[x] > maxs:
            maxs = conversations_stats[x]
            ind_max = x
    return ind_max, maxs

def chatBot(conversations, currentConversation):
    rslt = currentConversation
    lc = len(conversations)
    conversations_stats = [0 for i in range(lc)]
    conversations_li = [0 for i in range(lc)]
    #for x in range(lc):
    for x, wlist in enumerate(conversations, start=0):   # Python indexes start at zero
        #wlist  = conversations[x]
        #wl = len(wlist)
        conversations_li[x]=0
        conversations_stats[x] = 0
        #for y in range(wl):
        for y, a_word in enumerate(wlist, start=0):
            #a_word = wlist[y]
            if a_word in currentConversation:
                if is_unique(a_word,wlist):
                    conversations_stats[x] = conversations_stats[x] + 1
                    conversations_li[x]=y

        #print('word c'+str(conversations_li[x])+' cc'+str(x)+' :'+a_word)



    # ok the one with max unique matching
    ind_max, maxs = find_max(conversations_stats)
    #seaching for the last match
    #print(maxs)
    if maxs == 0:
        return rslt
    else:
        wlist  = conversations[ind_max]
        cl=len(wlist)
        for k in range(conversations_li[ind_max]+1,cl):
            rslt.append(wlist[k])
        return rslt
    return rslt
'''
