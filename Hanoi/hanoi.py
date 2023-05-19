from popfunc import *

def hanoi(a,s2=[],s3=[],k=1,p=[101,102,103],n=0,part=1):
    

    def kk(k):
        k+=1
        if k>3:
            k=1
        return k
    def pp(a,p,k):
        if len(a)>0:
            if a[-1]==p[-1]:
                k=kk(k)
                # print(k)
        return k
   

    def ass(a,s2,k,n,k2):
        if len(a)>0:
            if len(s2)==0 or s2[-1]<a[-1]:
                print(a[-1], k, k2)
                p.append(a[-1])
                p.pop(0)
                s2.append(a[-1])
                a.pop(-1)
                print(dt)
                n+=1
            else:
                k=kk(k)
             
        else:
            k=kk(k)
           
        return k,n

    dt={1:a,3:s2,2:s3}
    
    if len(a)>0 and part==1:
        # print(k,p)
        k=pp(dt[k],p,k)
        
        k1=k
        kn=ass(dt[k],dt[kk(k)],k,n,kk(k))
        k=kn[0]
        n=kn[1]
        
        if k1!=k:
            return hanoi(a,s2,s3,k,p,n)
        kn=ass(dt[k],dt[kk(kk(k))],k,n, kk(kk(k)))
        k=kn[0]
        n=kn[1]
        if k1!=k:
            return hanoi(a,s2,s3,k,p,n)
        
        k=kk(k)
        return hanoi(a,s2,s3,k,p,n)

    else:
        if len(a)==0 and (len(s2)==0 or len(s3)==0):
            return print('ГОТОВО!!! Количество шагов:', n)
        part=2
        # print(k,p)
        k=pp(dt[k],p,k)
        
        k1=k
        kn=ass(dt[k],dt[kk(k)],k,n,kk(k))
        k=kn[0]
        n=kn[1]

        if k1!=k:
            return hanoi(a,s2,s3,k,p,n)
        kn=ass(dt[k],dt[kk(kk(k))],k,n,kk(kk(k)))
        k=kn[0]
        n=kn[1]
        if k1!=k:
            return hanoi(a,s2,s3,k,p,n)
        
        k=kk(k)
        return hanoi(a,s2,s3,k,p,n)
  

a=ii()
al=[]
while a!=0:
    al.append(a)
    a-=1
al.reverse()
hanoi(al)
