file=open("C:\\Users\minjie\Desktop\data_label.txt","r",encoding="utf-8")
file1=open("data_test.txt","w",encoding="utf-8")
sentence=""
label=""
sen=[]
lab=[]
text=[]
ignored_words=['!','\"','$','%','\'','(',')','*','+',',','.','..','@','#','&','?','/']
for line in file:
	line=line.lower()
	if(line[0]=='\"'):
		for item in sen:
			if(item in dic):
				if(len(item)<2):
					continue
				file1.write(item+" "+dic[item]+"\n")
			else:
				if(len(item)<2):
					continue
				file1.write(item+" "+"O"+"\n")
		file1.write("\n")
		dic={}
		sentence=line[1:-2]
		for i in range(0,len(sentence)):
			if sentence[i] in ignored_words:
				sentence=sentence.replace(sentence[i],' ')
		sen=sentence.split(' ')
	elif(line[0]=='('):
		label=line
		lab=label.split(',')
		lab1=lab[0][1:].split(' ')
		lab2=lab[1].split(' ')
		flag=0
		for item in lab1:
			if(flag==0):
				dic[item]="B-DIS"
				flag=1
			else:
				dic[item]="I-DIS"
		flag=0
		for item in lab2:
			if(flag==0):
				dic[item]="B-MED"
				flag=1
			else:
				dic[item]="I-MED"
file.close()
file1.close()