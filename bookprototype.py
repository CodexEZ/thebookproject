import csv
import string
def book_project(f):
    file=open(f,"r")
    d=dict()
    for line in file:
        line=line.strip()
        line=line.lower()
        line=line.translate(line.maketrans("","",string.punctuation))
        words=line.split()
        for word in words:
            if word=="a" or word=="and" or word=="an" or word=="of" or word=="in" or word=="the":
                continue
            if word in d:
                d[word]=d[word]+1
            else:
                d[word]=1
    f=[]
    w=[]
    for i in d:
        f.append(d[i])
    for key in d.keys():
        w.append(key)
    l=len(f)
    for i in range(l-1):
        for j in range(0,l-i-1):
            if f[j+1]>f[j]:
                k=f[j+1]
                f[j+1]=f[j]
                f[j]=k
                g=w[j+1]
                w[j+1]=w[j]
                w[j]=g
    for i in range(0,100):
        print(w[i],"--->",f[i])
    #Normalizing values and storing it in different list
    x_max=f[-1]
    x_min=f[0]
    normal=[]
    for x in f:
        normal.append((x-x_min)/(x_max-x_min))
    n_values.append(normal)
    book_words.append(w)
    book_words_frequency.append(f)


l=["book 1.txt","book 2.txt"]
n_values=[]
book_words=[]
book_words_frequency=[]
for i in l:
    book_project(i)
min=min(len(n_values[0]),len(n_values[1]))
rows=[]
zx1=[]
zx2=[]
zx3=[]
for i in range(min):
    for j in range(min):
        if book_words[0][j]==book_words[1][i]:
            zx1.append(book_words[0][i])
            zx2.append(n_values[0][j])
            zx3.append(n_values[1][i])
zx1=zx1[0:100]
zx2=zx2[0:100]
zx3=zx3[0:100]
csvfile=open("Bookdata1.csv",'w')
csvwriter=csv.writer(csvfile)
csvwriter.writerow(zx1)
csvwriter.writerow(zx2)
csvwriter.writerow(zx3)




