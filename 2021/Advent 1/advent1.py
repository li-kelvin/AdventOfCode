

file1 = open('advent1.txt', 'r')
Lines = file1.readlines()

cnt = 0
for i in range(len(Lines) - 1):
    if Lines[i] < Lines[i+1]:
        cnt += 1
        
print(f'Ans: {cnt}') # 7



    
    
    
    
