def duplicate(s):

    if len(s)== 0:
        return True
    if len(s)%2 ==1:
        return(False)
    
    mid = len(s)//2

    for i in range(mid):
        
        if s[i] != s[mid+i]:
            return(False)

    return duplicate(s[1:mid])

print(duplicate("htmmtmmhtmmtmm")) # output: True
