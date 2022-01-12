def ngram(object, n):
    if type(object) == str:
        object = object.split()
        ans = []
    for i in range(len(object)-n+1):
        ans_item = []
        for k in range(n):
            ans_item.append(object[i+k])
        ans.append(ans_item)
    return(ans)


print(ngram("i am an apple", 3))
