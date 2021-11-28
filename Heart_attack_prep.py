import joblib
model=joblib.load('Heart_attack.pk1')
name=input("Enter Your name :")
lst=[]

d1=int(input("Enter your Age :"))
lst.append(d1)
d2=input("Enter your Gender (male/female) :")
if d2=='male':
    d2=1
elif d2=='female':
    d2=0
else:
    print("Please enter the input as mentioned !")
lst.append(d2)

d3=int(input("Enter your Cholestrol in mg/dL :"))
lst.append(d3)
d4=int(input("Enter your Greatest number of beats per minute your heart can possibly reach during all-out strenuous exercise :"))
lst.append(d4)
prep=model.predict([lst])
if prep==0:
    print(name,"you are healthy,keep it up!!")
else:
    print(name,"You may in the future subjected to heart attack,Please look after your health")
