
for _ in range(int(input())):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    ans=0
    for i in A:
        ans=ans|i

    ans=list(bin(ans).replace("0b", "") )
    count=0
    
    strr=""
    for i in ans:
        if count<K:
           strr+=str(i)
         
           if i=='1':
              count+=1
             
        else:
            strr+='0'
    print(int(strr,2))
        
  
    