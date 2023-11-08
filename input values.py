a=input("enter values for a:")
b=input("enter values for b:")
c=input("enter values for c:")
values=[a,b,c]
for i in range(0,3):
    print(*values,sep="\t")
    print()
