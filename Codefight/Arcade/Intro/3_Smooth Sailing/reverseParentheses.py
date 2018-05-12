def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == '(':
            sdx = i

        elif s[i] == ')':
            edx = i
            #print "[!]",s[:sdx] + s[sdx + 1:edx][::-1] + s[edx + 1:]
            return reverseParentheses(s[:sdx] + s[sdx + 1:edx][::-1] + s[edx + 1:])
    return s
