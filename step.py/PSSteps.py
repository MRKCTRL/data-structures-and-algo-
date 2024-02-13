charCount('my name is Jabu')
    # {m:2
    # y:1,
    # n:1,
    # a:2,
    # e:2,
    # i:1,
    # s:2,
    # l:1,
    # j:1,
    # h:1,
    # d:1}







def CharCount(strn):
    # delcare an object to return at the end 
    result=dict()
    # loop over the string 
    for i in strn.lower():
    # do something 
        # if the char is in out object add one to the value 
        if isinstance(i, str) and not (i.isspace()):
            if i in result:
                result[i]+=1
        # if the char is letter and is it not in our object add that char to our object with the value of one 
            else:
                result[i]=1
      # return something
    return result    
      # pass