import sys

def where_dot(file_circle, file_dot):

    with open(file_circle, 'r', encoding='utf-8') as f1:
        data1 = f1.readlines()  

    with open(file_dot, 'r', encoding='utf-8') as f2:
        data2 = f2.readlines()

    x0 = float(data1[0].split()[0])
    y0 = float(data1[0].split()[1])
    R = float(data1[1])

    for i in range(len(data2)):
        x = float(data2[i].split()[0])
        y = float(data2[i].split()[1])
        
        f = (x-x0)**2 + (y-y0)**2 - R**2
    
        if f == 0:
            print(0)
        elif f > 0:
            print(2)
        elif f < 0:
            print(1)

where_dot(sys.argv[1], sys.argv[2])
#print('Запись законечена')
