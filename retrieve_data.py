import urllib, pandas, os

def getData(file, pickle=None, url=None, sep="\t", filt=None):
    if pickle:
        if os.path.exists(pickle):
            print("Initiate Unpickling Procedure!!")
            return pandas.read_pickle(pickle)
    if not os.path.exists(file):
        if not url:
            return None
        urllib.request.urlretrieve(url, file)
    print("Reading Data")
    df = pandas.read_csv(file, sep=sep, encoding="ISO-8859-1")
    if filt:
        df = df[filt]
    if pickle:
        print("Creating pickle at " + file)
        df.to_pickle(pickle)
    return df