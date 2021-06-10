import os
import pandas as pd

df1 = pd.DataFrame( columns=list('AB'))
entries = os.listdir('fire/bike')
b0 = [0]*51
b1=[1]*22
b=b0+b1
c=0
print("here")
for i in entries:
    
    if(c<51):
        df1=df1.append({'A':i,'B':0},ignore_index=True)
    else:
        df1=df1.append({'A':i,'B':1},ignore_index=True)
    c=c+1

entries = os.listdir('fire/drum')
c=0
print("here")
for i in entries:
    if(c<74):
        df1=df1.append({'A':i,'B':0},ignore_index=True)
    else:
        df1=df1.append({'A':i,'B':1},ignore_index=True)
    c=c+1

entries = os.listdir('fire/scooter')
c=0
print("here")
for i in entries:
    if(c<20):
        df1=df1.append({'A':i,'B':0},ignore_index=True)
    else:
        df1=df1.append({'A':i,'B':1},ignore_index=True)
    c=c+1

entries = os.listdir('fire/pallet')
c=0
print("here")
for i in entries:
    if(c<70):
        df1=df1.append({'A':i,'B':0},ignore_index=True)
    else:
        df1=df1.append({'A':i,'B':1},ignore_index=True)
    c=c+1

entries = os.listdir('fire/cylinder')
c=0
print("here")
for i in entries:
    if(c<61):
        df1=df1.append({'A':i,'B':0},ignore_index=True)
    else:
        df1=df1.append({'A':i,'B':1},ignore_index=True)
    c=c+1

df1.to_csv(r'list_eval_partition.txt', header=None, index=None, sep=' ', mode='a')

