import pandas as pd
import numpy as np
from scipy.sparse import csc_matrix
train2id = pd.read_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/train2id.txt",header=None,sep='\t')
valid2id = pd.read_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/valid2id.txt",header=None,sep='\t')
train2id_drop = []  #删除那些自身到自身的边
print(train2id)
for i in range(len(train2id)):
    a = train2id.iloc[i,0]
    b = train2id.iloc[i,1]
    if a==b:
        train2id_drop.append(i)
train2id = train2id.drop(labels=train2id_drop,axis=0)
train2id.to_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/train2id.txt",header=None,sep='\t',index=0)

valid2id_drop = []  #删除那些自身到自身的边
for i in range(len(valid2id)):
    a = valid2id.iloc[i,0]
    b = valid2id.iloc[i,1]
    if a==b:
        valid2id_drop.append(i)
valid2id = valid2id.drop(labels=valid2id_drop,axis=0)
valid2id.to_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/valid2id.txt",header=None,sep='\t',index=0)

train2id = pd.concat([train2id,valid2id])

train_4 = train2id[train2id[2]==4][[0,1]]
train_4_copy = train_4[[1,0]]
train_4_copy.columns = [0,1]
train_4_total = pd.concat([train_4,train_4_copy]).drop_duplicates()

train_4_total.to_csv("C:/Users/10341/OneDrive/实验/economics/train_4.txt",header=None,sep='\t',index=0)


test_1hop = pd.read_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/test_1hop.txt",header=None,sep='\t')
test_2 = pd.read_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/test_2.txt",header=None,sep='\t')

test_1hop = test_1hop.drop_duplicates()
test_2 = test_2.drop_duplicates()
test_1hop.to_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/test_1hop.txt",header=None,sep='\t',index=0)
test_2.to_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/test_2.txt",header=None,sep='\t',index=0)

test_1hop = test_1hop.drop([2],axis=1)
test_2 = test_2.drop([2],axis=1)

test_1hop.to_csv("C:/Users/10341/OneDrive/实验/economics/test_1hop.txt",header=None,sep='\t',index=0)
test_2.to_csv("C:/Users/10341/OneDrive/实验/economics/test_2.txt",header=None,sep='\t',index=0)
test_1hop_copy = test_1hop[[1,0]]
test_1hop_copy.columns = [0,1]
test_1hop_ = pd.concat([test_1hop,test_1hop_copy]).drop_duplicates()
test_1hop_.to_csv("C:/Users/10341/OneDrive/实验/economics/test_1hop_.txt",header=None,sep='\t',index=0)
test_2_copy = test_2[[1,0]]
test_2_copy.columns = [0,1]
test_2_ = pd.concat([test_2,test_2_copy]).drop_duplicates()
test_2_.to_csv("C:/Users/10341/OneDrive/实验/economics/test_2_.txt",header=None,sep='\t',index=0)

test_1hop_[2] = 4
test_2_[2] = 4

test_1hop_.to_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/test_1hop_.txt",header=None,sep='\t',index=0)
test_2_.to_csv("C:/Users/10341/OneDrive/实验/ddjin/economics/13-15/13-15-little/1/test_2_.txt",header=None,sep='\t',index=0)

train = pd.read_csv("C:/Users/10341/OneDrive/实验/economics/train_4.txt",header=None,sep='\t')

row = []
col = []
data = []
for i in range(len(train)):
    a = train.iloc[i,0]
    b = train.iloc[i,1]
    row.append(a)
    col.append(b)
    data.append(1.0)

print(len(set(list(train[0]) + list(train[1]))))
print(max(list(train[0]) + list(train[1])))

train_csc = csc_matrix((data, (row, col)), shape=(917, 917))
import scipy.io as scio
dataNew = 'C:/Users/10341/OneDrive/实验/economics/man_train_4.mat'
scio.savemat(dataNew, {'net':train_csc})

test_1hop = pd.read_csv("C:/Users/10341/OneDrive/实验/economics/test_1hop.txt",header=None,sep='\t')
row = []
col = []
data = []
for i in range(len(test_1hop)):
    a = test_1hop.iloc[i,0]
    b = test_1hop.iloc[i,1]
    row.append(a)
    col.append(b)
    data.append(1.0)
test_1hop_csc = csc_matrix((data, (row, col)), shape=(917,917))
import scipy.io as scio
dataNew = 'C:/Users/10341/OneDrive/实验/economics/man_test_1hop_4.mat'
scio.savemat(dataNew, {'net':test_1hop_csc})

test_1hop_ = pd.read_csv("C:/Users/10341/OneDrive/实验/economics/test_1hop_.txt",header=None,sep='\t')
row = []
col = []
data = []
for i in range(len(test_1hop_)):
    a = test_1hop_.iloc[i,0]
    b = test_1hop_.iloc[i,1]
    row.append(a)
    col.append(b)
    data.append(1.0)
test_1hop__csc = csc_matrix((data, (row, col)), shape=(917,917))
import scipy.io as scio
dataNew = 'C:/Users/10341/OneDrive/实验/economics/man_test_1hop__4.mat'
scio.savemat(dataNew, {'net':test_1hop__csc})

test_2 = pd.read_csv("C:/Users/10341/OneDrive/实验/economics/test_2.txt",header=None,sep='\t')
row = []
col = []
data = []
for i in range(len(test_2)):
    a = test_2.iloc[i,0]
    b = test_2.iloc[i,1]
    row.append(a)
    col.append(b)
    data.append(1.0)
test_2_csc = csc_matrix((data, (row, col)), shape=(917,917))
import scipy.io as scio
dataNew = 'C:/Users/10341/OneDrive/实验/economics/man_test_2_4.mat'
scio.savemat(dataNew, {'net':test_2_csc})

test_2_ = pd.read_csv("C:/Users/10341/OneDrive/实验/economics/test_2_.txt",header=None,sep='\t')
row = []
col = []
data = []
for i in range(len(test_2_)):
    a = test_2_.iloc[i,0]
    b = test_2_.iloc[i,1]
    row.append(a)
    col.append(b)
    data.append(1.0)
test_2_csc = csc_matrix((data, (row, col)), shape=(917,917))
import scipy.io as scio
dataNew = 'C:/Users/10341/OneDrive/实验/economics/man_test_2__4.mat'
scio.savemat(dataNew, {'net':test_2_csc})