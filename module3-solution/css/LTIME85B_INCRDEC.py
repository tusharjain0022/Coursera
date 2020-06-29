def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    ans=1
    a=[]
    b=[]
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    for key, value in freq.items(): 
        if value>2:
            ans=0
        elif value==1:
            a.append(key)
        else:
            a.append(key)
            b.append(key)
    a.sort()
    b.sort(reverse=True)
    if len(a)!=0 and len(b)!=0 and a[-1]==b[0]:
        ans=0
    if ans==0:
        print("NO")
    else:
        print("YES")
        for i in a:
            print(i,end=' ')
        for i in b:
            print(i,end=' ')
        print('')
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    ans=1
    CountFrequency(A)