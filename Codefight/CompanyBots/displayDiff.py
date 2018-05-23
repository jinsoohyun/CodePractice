def displayDiff(oldVersion, newVersion):
    oldStr = ''
    newStr = ''
    for i in range(len(oldVersion)):
        if oldVersion[i] != newVersion[i]:
            oldStr += oldVersion[i]
            newStr += newVersion[i]

        else:
            if len(oldStr) > 0:
                print oldStr
                print newStr
                oldStr = ''
                newStr = ''




oldVersion = "same_prefix_1233_same_suffix"
newVersion = "same_prefix23123_same_suffix"
#            "same_prefix(_1)23[12]3_same_suffix"

oldVersion = "same_prefix_1233_same_suffix"
newVersion = "same_prefix231233_same_suffix"
#            "same_prefix(_)[23]1233_same_suffix""
displayDiff(oldVersion, newVersion)

