def ass_coll(assids:int):
    stack=[]
    for assid in assids:
        while stack and assid<0<stack[-1]:
            if stack[-1]<-assid:
                stack.pop()
            elif stack[-1]==assid:
                stack.pop()
                break
            else:
                break
        else:
            stack.append(assid)
    return stack

print(ass_coll([5,10,-5]))
print(ass_coll([5,10,5]))