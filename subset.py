import pandas

def separateUnique(data, col):
    fin = {}
    for x in data[col].unique():
        fin[x] = (data[data[col] == x])
    return fin