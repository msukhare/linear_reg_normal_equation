import sys
import csv
import pandas as pd
import numpy as np

def read_file():
    try:
        data = pd.read_csv(sys.argv[1])
    except:
        sys.exit("wrong name of file")
    data.insert(0, 'X0', 1)
    col = data.shape[1]
    X = data.iloc[:, 0 : col - 1]
    Y = data.iloc[:, col - 1 :]
    X = np.array(X.values, dtype=float)
    Y = np.array(Y.values, dtype=float)
    return (data, X, Y)

def open_new_file(thetas):
    try:
        c = csv.writer(open(sys.argv[2], "w"))
    except:
        sys.exit("no name for new_file, fail to creat it")
    for i in thetas:
        c.writerow(i)

def main():
    data, X, Y = read_file() 
    X_t = np.transpose(X)
    X_by_X_inv = np.linalg.inv(X_t.dot(X))
    thetas = X_by_X_inv.dot(X_t).dot(Y)
    open_new_file(thetas)

if __name__ == "__main__":
    main()
