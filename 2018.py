
M1= input()
M2= input()
M3= input()
M4= input()
M5= input()
M6= input()

winI=0
winS=0
winM=0
winP=0
loseI=0
loseS=0
loseM=0
loseP=0
diffI=0
diffS=0
diffM=0
diffP=0
PointI=0
PointS=0
PointM=0
PointP=0
drawI=0
drawS=0
drawP=0
drawM=0

if int(M1[0])> int(M1[2]):
    winI+=1
    loseS+=1
elif int(M1[0])==int(M1[2]):
    drawI+=1
    drawS+=1
else:
    winS+=1
    loseI+=1


if int(M2[0])> int(M2[2]):
    winI+=1
    loseP+=1
elif int(M2[0])==int(M2[2]):
    drawP+=1
    drawI+=1
else :
    winP+=1
    loseI+=1

if int(M3[0])> int(M3[2]):
    winI+=1
    loseM+=1
elif int(M3[0])==int(M3[2]):
    drawM+=1
    drawI+=1
else :
    winM+=1
    loseI+=1

if int(M4[0])> int(M4[2]):
    winS+=1
    loseP+=1
elif int(M4[0])==int(M4[2]):
    drawP+=1
    drawS+=1
else :
    winP+=1
    loseS+=1

if int(M5[0])> int(M5[2]):
    winS+=1
    loseM+=1
elif int(M5[0])==int(M5[2]):
    drawS+=1
    drawM+=1
else :
    winM+=1
    loseS+=1

if int(M6[0])> int(M6[2]):
    winP+=1
    loseM+=1
elif int(M6[0])==int(M6[2]):
    drawP+=1
    drawM+=1
else :
    winM+=1
    loseP+=1

PointI= winI*3+drawI
PointM=winM*3+drawM
PointS=winS*3+drawS
PointP=winP*3+drawP

diffI=int(M1[0])-int(M1[2])+int(M2[0])-int(M2[2])+int(M3[0])-int(M3[2])
diffS=int(M1[2])-int(M1[0])+int(M4[0])-int(M4[2])+int(M5[0])-int(M5[2])
diffP=int(M2[2])-int(M2[0])+int(M4[2])-int(M4[0])+int(M6[0])-int(M6[2])
diffM=int(M3[2])-int(M3[0])+int(M5[2])-int(M5[0])+int(M6[2])-int(M6[0])

print('Spain wins:{0} ,loses:{1} ,draws:{2} ,goal difference:{3} ,points:{4}'.format(winS,loseS,drawS,diffS,PointS))
print('Iran wins:{0} ,loses:{1} ,draws:{2} ,goal difference:{3} ,points:{4}'.format(winI,loseI,drawI,diffI,PointI))
print('Portugal wins:{0} ,loses:{1} ,draws:{2} ,goal difference:{3} ,points:{4}'.format(winP,loseP,drawP,diffP,PointP))
print('Morocco wins:{0} ,loses:{1} ,draws:{2} ,goal difference:{3} ,points:{4}'.format(winM,loseM,drawM,diffM,PointM))



