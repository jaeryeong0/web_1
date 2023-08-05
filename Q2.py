N, M = map(int, input().split())

def Printf(format, string):
    if len(string)==0: return

    global M
    format = "L"
    if format == "L":
        while len(string) > 0:

            res = ""
            temp = ""
            i = 0
            while len(res)-1 <= M and i < len(string):
                res = temp
                temp += string[i] + "-"
                i += 1
            
            res = res[:-1]
            temp = temp[:-1]

            if len(temp) <= M:
                res = temp+ "-"*(M-len(temp))
                i += 1
            else:
                res = res+ "-"*(M-len(res))
            print(res)
            # print(string)
            # print(i-1)
            string = string[i-1:]
    # if format == "R":

    
    # if format == "C":


Input = []
Lines = []
for i in range(N):
    temp = list(map(str, input().split()))
    Input += temp
    Lines.append(temp)

StrLines = []
for i, line in enumerate(Lines):
    if line[0][0]!="<":
        StrLines.append(line)

Enters = []





cnt = 0
strings = []
tags = [("L",0)]
for i, x in enumerate(Input):
    if x[0]=="<":
        if x[1]=="/":
            tags.append(("L",i-cnt))
        else:
            tags.append((x[1],i-cnt))
        cnt += 1
        print(1)
    else:
        strings.append(x)

print(Enters)

# print(tags)

for i in range(len(tags)):

    start1 = tags[i][1]

    try:
        end1 = tags[i+1][1]
    except: end1 = None

    # print(start, end)
    
    j = 0
    while j < len(Enters):
        start = Enters[j]
        try:
            end = Enters[j+1]
        except: end = None
        
        
        if start < start1 or end > end1:
            break
        
        print(start1, start, end1, end)
        j += 1
        Printf(tags[i][0], strings[start:end])
    # print("----------------------------------------------------------------")

'''
7 11
<CENTER>
Hello world
</CENTER>
Hello world
<RIGHT>
Hello world
</RIGHT>
'''
