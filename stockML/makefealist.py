def genesubset(inputlist):
    temp=[]
    for i in range(len(inputlist)):
        temp.append([inputlist[i]])
        for j in range(len(inputlist)-i-1):
            temp[i].append(inputlist[i+1+j])
    return temp
    
temp=[]
def tt(inputlist,i=0,j=1):
    if i==len(inputlist)-1:
        return temp
    temp.append([inputlist[i],inputlist[i+j]])
    if i+j==len(inputlist)-1:
        i+=1
        j=1
        return tt(inputlist,i,j)
    else :
        j+=1
        return tt(inputlist,i,j)

