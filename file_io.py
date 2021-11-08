def read_data(file):
    f = open(file, "r")

    data = {}
    data['s1'] = float(f.readline())
    data['p1'] = float(f.readline()) 
    data['s2'] = float(f.readline())
    data['p2'] = float(f.readline())
    data['s3'] = float(f.readline())
    data['p3'] = float(f.readline())
    data['lambda'] = float(f.readline())

    f.close()

    return data

def write_sequence(file, seq):
    f = open(file, "a")
    f.seek(0)

    for elem in seq:
        f.write(str(float('{:.3f}'.format(elem))) + "\n")

    f.close()

def write_data(file, content):
    f = open("results/"+file, "a")
    f.seek(0)

    for elem in content:
        f.write(str((elem)) + "\n")
    f.write("\n")
    
    f.close()