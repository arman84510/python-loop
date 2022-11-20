list1=[2,3,4,5,56,56,56]
search=int(input("enter input to search in list"))
i=1
while i<=1:
    if search in list1:
        p=list1.index(search)
        print("position of",search ,"is",p)
        i=i+1
    else:
        print("your search is not present in list")
        i=i+1
