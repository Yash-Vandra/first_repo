list3=['a','e','o','u','i']
for i in range(int(input())):
    a='sad'
    sre3=list(input("enter string "))
    for j in range(len(sre3)-2):
        print(sre3[j])
        if sre3[j] in list3 and sre3[j+1] in list3 and sre3[j+2] in list3:
            a = 'happy'
    print(a)