from pgmpy.models import MarkovNetwork

solution    = [ [0,0,0,1,0,0,0,1,0],
                [0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,1,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,1],
                [0,0,0,0,0,0,0,0,0] ]
toporder= [
            "burningRegimen",
            "filterState",
            "wasteType",
            "co2Concentration",
            "filterEfficiency",
            "metalsInWaste",
            "dustEmission",
            "lightPenetrability",
            "metalsEmission"
        ]

def main():
    print("Start")
    G = MarkovNetwork()  
    
    G.add_nodes_from(toporder)
    
    row=0
    for r in solution: 
        col=0
        for x in r:
            if x==1:
                G.add_edge(toporder[row],toporder[col])
            col+=1
        row+=1
    
    print(G)
    mb=G.markov_blanket("metalsEmission")
    for x in mb:
        print (x)
    

if(__name__=='__main__'):
    main()