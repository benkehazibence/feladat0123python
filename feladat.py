import os, random

#2 ország közti lakosság különbség
def kulonbseg(orsz1, orsz2):
    if(orsz1>orsz2):
        return orsz1-orsz2
    else:
        return orsz2-orsz1
    
os.system("cls")
#2 ország lakosság száma (8-20 millió között)
o1=random.randrange(8,21)
o2=random.randrange(8,21)
print("1. ország:",o1,"millió fő")
print("2. ország:",o2,"millió fő")
print("")
print("Különbség:",kulonbseg(o1,o2),"millió fő")