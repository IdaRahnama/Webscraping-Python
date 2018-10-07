class student:
    count=0
    def __init__(self,age,weight,height):
        self.age=age
        self.weight=weight
        self.height=height
        student.count+=1

n1=input()
age1=list()
height1=list()
weight1=list()
st=input()
st=st.split()
for i in range(int(n1)):
    age1.append(st[i])


st=input()
st=st.split()
for i in range(int(n1)):
    height1.append(st[i])

st=input()
st=st.split()
for i in range(int(n1)):
    weight1.append(st[i])
st1=list()
for i in range(int(n1)):
    st1.append(student(age1[i],weight1[i],height1[i]))

n2=input()
age2=list()
height2=list()
weight2=list()
st=input()
st=st.split()
for i in range(int(n2)):
    age2.append(st[i])


st=input()
st=st.split()
for i in range(int(n2)):
    height2.append(int(st[i]))

st=input()
st=st.split()
for i in range(int(n2)):
    weight2.append(int(st[i]))
st2=list()
for i in range(int(n2)):
    st2.append(student(age2[i],weight2[i],height2[i]))

sum1=0.
sum2=0.
sum3=0.
for i in range(int(n1)):
    sum1+=int(st1[i].age)
    sum2+=int(st1[i].weight)
    sum3+=int(st1[i].height)
print(sum1/int(n1))
print(sum3/int(n1))
print(sum2/int(n1))

av_h1=sum3/int(n1)
av_w1=sum2/int(n1)
sum1=0.
sum2=0.
sum3=0.
for i in range(int(n2)):
    sum1+=int(st2[i].age)
    sum2+=int(st2[i].weight)
    sum3+=int(st2[i].height)
print(sum1/int(n2))
print(sum3/int(n2))
print(sum2/int(n2))

av_h2=sum3/int(n2)
av_w2=sum2/int(n2)

if av_h1>av_h2:
    print('A')
elif av_h1==av_h2 and av_w1<av_w2 :
    print('A')
elif av_h1==av_h2 and av_w1>av_w2 :
    print('B')
else:
    print('B')




