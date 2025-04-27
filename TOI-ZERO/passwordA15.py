firstname = input()
lastname = input()
age= input()
if len(firstname) > 5 and len(lastname) > 5:
    print(firstname[:2]+lastname[-1]+age[-1])
else:
    print(firstname[0]+age+lastname[-1])