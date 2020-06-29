for _ in range(int(input())):
    S,N=map(int,input().split())
    ans=0
    if N>=S:
        if S%2==0 or S==1:
            ans=1
        else:
            ans=2
    else:
        if S%N==0:
            ans=int(S/N)
        else:
            ans=int(S/N)
            if (S-ans*N)%2==0 or (S-ans*N)==1 :
                ans+=1
            else:
                ans+=2
    print(ans)