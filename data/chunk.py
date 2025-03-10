import numpy as np
file=open("data.txt","r",encoding="utf-8")
file1=open("data_dev.txt","w",encoding="utf-8")
file2=open("data_test.txt","w",encoding="utf-8")
file3=open("data_train.txt","w",encoding="utf-8")
data=[]
res=[]
def splitData(dat,seed,m,k):
    #将数据分成训练集和测试集，每次指定seed，更换K,重复M次,防止过拟合.
    test=[]
    train=[]
    #random.seed(seed),指定seed的话，每次后面的随机数产生的都是一样的顺序
    np.random.seed(seed)
    for item in dat:
        #随机数产生顺序一样,随机产生（0，m）之间的数，只有一个可以分给测试集，另外的m-1都分给训练集
        if np.random.randint(0,m)==k:
            test.append(item)
        else:
            train.append(item)
    return test,train

for line in file:
	if(len(line)<2):
		res.append(data)
		data=[]
		continue
	data.append(line)
test,train=splitData(res,5,4,2)
dev,test=splitData(test,5,3,2)
for i in dev:
	for j in i:
		file1.write(str(j))
	file1.write("\n")
for i in test:
	for j in i:
		file2.write(str(j))
	file2.write("\n")
for i in train:
	for j in i:
		file3.write(str(j))
	file3.write("\n")
print(len(dev))
print(len(test))
print(len(train))
file.close()
file1.close()
file2.close()
file3.close()