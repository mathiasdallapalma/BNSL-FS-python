import sys
import numpy as np
import csv
from sklearn.preprocessing import LabelEncoder
import argparse
from collections import Counter

def readFile(fileName):
    with open(fileName) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        
        examples = []

        line_count = 0
        for row in csvReader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                examples += [[ float(x) for x in row[:-1]]+row[-1:]]
                line_count += 1

    return examples
    
def saveResults(args, matrix,varCardinality):
    file2 = open(args.output, 'w')
    lenM=len(matrix[0])
    sol=np.zeros(lenM*(lenM-1),dtype=int)

    file2.write("{} {}\n".format(lenM," ".join(map(str, varCardinality))))
    file2.write("{}\n".format(args.name))
    file2.write("{}\n".format(" ".join(map(str, sol))))


    np.savetxt(file2, matrix, fmt="%.0f")
    file2.close()

def discretize(x,bins):
#vedi standard scaler

    row=0
    for v in x[:-1]:    
        norm = [(float(i)-min(v))/(max(v)-min(v)+0.0001) for i in v]
        x[row]=np.digitize(norm,bins)
        row+=1

    label_encoder = LabelEncoder()
    for v in x[-1:]:
        x[row]=label_encoder.fit_transform(v)
    
    return x

    
    

def main():
    parser = argparse.ArgumentParser(description='Tool for discretize dataset',
                                   prog='python3 -m discretize')
    
    parser.add_argument('dataset', type=str, help='dataset path')
    
    parser.add_argument("-l","--label",
                    help="the column in witch starts the alpha-numeric values.", metavar="NUM")
    parser.add_argument("-o","--output", help="name of the output file", metavar="FILE",default="out.txt")
    parser.add_argument("-b","--bins", help="number of discrete classes", metavar="NUM",default=2)
    parser.add_argument("-n","--name", help="name of the dataset/problem", metavar="STR",default="PROBLEM")

    args = parser.parse_args()

    i=0
    bins=[]
    while(i<1):
        adder=1/int(args.bins)
        i+=adder
        bins+=[i]

    examples=readFile(args.dataset)
    transposed=[*zip(*examples)]

    transposedDisc=discretize(transposed,bins[:-1])
    varCardinality=[]
    i=0
    for r in transposedDisc:
        varCardinality+=[len(set(r))]

    exampleDisc=[*zip(*transposedDisc)]
    
    saveResults(args,exampleDisc,varCardinality)
   

if(__name__=='__main__'):
    main()