for _ in range(int(input())):
    N=int(input())
    A=0.000000
    B=0.000000
    for i in range(N):
        g,a,b=map(int,input().split())
        A +=  g*(b/(a+b))
        B += g*(a/(a+b))
    print('%.6f'%A,end=" ")
    print ('%.6f'%B)

