total = 0
current = 0
list = []


file1 = open('advent1.txt', 'r')
Lines = file1.readlines()


for line in Lines:
    if line == "\n":
        current += 1
        total = 0
    else:
        total += int(line)
        list.append(total)
        list[current] = total
        
list.sort(reverse=True)        


print(sum(list[1:4]))