
import sys
import csv
import argparse
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_percentage_error

from sklearn.naive_bayes import GaussianNB
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression

def readFile(fileName,features):
    csv.field_size_limit(sys.maxsize)
    with open(fileName) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        
        X = []
        y = []
        labels=[]

        line_count = 0
        for row in csvReader:
            if line_count == 0:
                labels+=[row]
                line_count += 1
            else:
                #for i in features:
                    #print(row[i])
                X += [ [float(row[i]) for i in features] ]
                y += [float(row[-1])]
                line_count += 1

    return X,y,labels

def switch(string):
    return{
        "gnb":GaussianNB(),
        "krr":KernelRidge(alpha=0.5),
        "lasso":Lasso(alpha=0.1),
        "lr":LogisticRegression()
        }[string]



def main():
    parser = argparse.ArgumentParser(description='Tool for train and test a model selecting n features from the total',
                                   prog='python3 -m model')
    
    parser.add_argument('dataset', type=str, help='dataset path')
    parser.add_argument('model', type=str, help='gaussian naive bayes [gnb], ')

    parser.add_argument("-a","--test_size", help="test size", metavar="NUM",default=0.9)
    parser.add_argument("-r","--random_state", help="random state", metavar="NUM")
    parser.add_argument("-m","--model", help="name of the dataset/problem", metavar="STR",default="PROBLEM")
    parser.add_argument("-f","--features", help="indexes of the selected features", metavar="ARRAY", nargs='+', default=[])

    args = parser.parse_args()

    args.features=[int(x) for x in args.features]

    X,y,labels=readFile(args.dataset,args.features)

    if(args.random_state!=None):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(args.test_size), random_state=int(args.random_state))
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(args.test_size))
    

    #print(X_test)

    model=switch(args.model)

    y_pred = model.fit(X_train, y_train).predict(X_test)

    print("Accuracy score:{}".format(accuracy_score(y_test, y_pred)))
    #print("Mean absolute pergentage erro:{}".format(mean_absolute_percentage_error(y_test, y_pred)))
   

if(__name__=='__main__'):
    main()