import json
name=input("enter your name:")
deg=0
lis=[]
with open ("r.json","r") as d:
    r=json.loads(d.read())
for i in al :
    ans=input("enter the answer:")
    lis.append(ans)
    if ans==r[i]:
        print("yes")
        mark=mark+1
    else :
        print("no")
x={name,lis}
print(x)
print("the mark is : ",mark)
