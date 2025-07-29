def rev(a,a_s,n):
    temp=0
    while (temp<a_s):
        st=temp
        end=min(temp+n-1,a_s-1)
        while (st<end):
            a[st],a[end]=a[end],a[st]
            st+=1
            end-=1
        temp+=n
a=[2,3,4,5,3,2,4,45,6,32,3,5,6,2,4,2,4,333,22]
n=2
a_s=len(a)
rev(a,a_s,n)
for i in range(0,a_s):
    print(a[i],end="")
