import os
import sys

nombres=[]
f=open('bg.txt','w')
a=sys.argv[1]
def main(dir):
    lista=os.listdir(dir)[:-1]
    # i=len(lista[:-1])
    for i in lista:
        path,exten=i.split(".")
        if exten == 'jpg' or exten == 'png':
            f.write(a+i+'\n')
    f.close()
    print(nombres)

if __name__=='__main__':
    main(a)