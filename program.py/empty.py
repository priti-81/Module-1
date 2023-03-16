n=input("enter words : ")
n1=n.split(' ')
for a in n1:
    if len(a)>2:
        print(a[0]+a[1]+a[-2]+a[-1])
    else:
        print('" "')
    
  