#将测试数据中，仅仅需要作者在同一个会议上发过论文，或者同属于一家单位或者有着共同的关键词
import pandas as pd
test_full = pd.read_csv("C:/Users/10341/Desktop/ddjin/education/13-15/13-15-little/1/test2id.txt",header=None,sep='\t')
train = pd.read_csv("C:/Users/10341/Desktop/ddjin/education/13-15/13-15-little/1/train2id.txt",header=None,sep='\t')
valid = pd.read_csv("C:/Users/10341/Desktop/ddjin/education/13-15/13-15-little/1/valid2id.txt",header=None,sep='\t')
train_full = pd.concat([train,valid])
train_1 = train_full.drop(3,axis=1)
test_full = test_full.drop_duplicates()
test_1 = pd.concat([train_1,train_1,test_full])
print(len(test_1))
test_2 = test_1.drop_duplicates(keep=False)
test_2.to_csv("C:/Users/10341/Desktop/ddjin/education/13-15/13-15-little/1/test_2.txt",index=0,header=None,sep='\t')
coauthor = train_1[train_1[2]==4]
affi = train_1[train_1[2]==0]
result_1 = []
for i in range(len(test_2)):
    a = test_2.iloc[i][0]
    b = test_2.iloc[i][1]
    a_affi = list(affi[affi[0]==a][1])
    b_affi = list(affi[affi[0]==b][1])
    print(a_affi,b_affi)
    if a_affi and b_affi and a_affi[0] == b_affi[0]:
        result_1.append(list(test_2.iloc[i]))

result_2 = []
for i in range(len(test_2)):
    a = test_2.iloc[i][0]
    print(a)
    b = test_2.iloc[i][1]
    a_coauthor = list(coauthor[coauthor[0]==a][1])
    b_coauthor = list(coauthor[coauthor[0]==b][1])
    if a_coauthor and b_coauthor:
        for j in a_coauthor:
            if j in b_coauthor:
                result_2.append(list(test_2.iloc[i]))
                break
test_1hop = pd.DataFrame(result_1 + result_2).drop_duplicates()
test_1hop.to_csv("C:/Users/10341/Desktop/ddjin/education/13-15/13-15-little/1/test_1hop.txt",index=0,header=None,sep='\t')