tri_num=0
j=0
num1=1
high_num=0
while True:
    tri_num+=num1
    num1+=1
    for i in range(1,tri_num+1):
        if tri_num%i==0:
         j+=1
    if j>high_num:
        high_num=j
        
        if high_num>500:
         print(tri_num)
         break
    j=0   
    
    
