import pickle
import os

def makepickle(filename,colIndex):
    filena=open(filename).readlines()
    filena=[x.split(',') for x in filena if 'None' not in x][1:]
    
    twot=int(len(filena)*0.6)
    onef=int(len(filena)*0.2)
    TrS=filena[:twot]
    CVS=filena[twot:twot+onef]
    TeS=filena[twot+onef:twot+onef*2]
    outstr=['TrS','CVS','TeS']
    outs=[TrS,CVS,TeS]
    
    for j in range(3):
        outj=map(list,zip(*outs[j]))
        for i in range(len(outj)):
            outj[i].reverse()
        col=[]
        for i in colIndex:
            col.append(outj[i])
        col=[map(float,list(x)) for x in col]
        d,e=os.path.splitext(filename)
        outname=d+'_'+outstr[j]+'_'.join([str(x) for x in colIndex])+'.pickle'
        pickle.dump(col,open(outname,'wb'))