with open('new1.txt','r') as f:
    lines=[]
    for line in f:
        lines.append(line.strip('\n'))
    print(lines)
