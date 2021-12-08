
Horizontal =  0
Depth =  0
split = list
Aim = 0

test = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']

#with open ("AOC2.txt") as f:
#    AOClist = f.readlines()

#for x in AOClist:
#    #if 'forward' in x:
#    #    print(x.rfind(' '))
#    if 'forward' in x:
#        split = x.split(' ') 
#        Horizontal += int(split[1])
#    if 'down' in x: 
#        split = x.split(' ') 
#        Depth += int(split[1])
#    if 'up' in x:
#        split = x.split(' ') 
#        Depth -= int(split[1])
#    print('Horizontal is:',Horizontal)
#    print('Depth is:',Depth)

#split = test[0].split(' ')  
#print(split[1])
    
with open ("AOC2.txt") as f:
    AOClist = f.readlines()

for x in AOClist:
    #if 'forward' in x:
    #    print(x.rfind(' '))
    if 'forward' in x:
        split = x.split(' ') 
        Horizontal += int(split[1])
        Depth += Aim * int(split[1])
    if 'down' in x: 
        split = x.split(' ') 
        Aim += int(split[1])
    if 'up' in x:
        split = x.split(' ') 
        Aim -= int(split[1])
    print('Horizontal is:',Horizontal)
    print('Depth is:',Depth)
    