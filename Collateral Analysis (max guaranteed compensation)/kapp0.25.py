import os
import sys
txval=5000
path=5


for z in os.listdir(sys.argv[1]):
    
    
        divide=0.25
        zeta=0.025
        
        while zeta<=0.025:
            kappa=1
            while kappa<=1:
                budget=5000000
                while budget<=700000000:
                    
                    txval=20000
                    penalty=0.000028
                    while penalty<=0.00034:
                        path=20
                        print(z)
                        k="snapshots/"+z
                        print(k)            
                        os.system("python3 graph_collateral_flowconstant.py "+str(k)+" "+str(penalty)+" "+str(divide)+" "+str(zeta)+" "+str(txval)+" "+str(path)+" "+str(budget)+" "+str(2016/20)+" "+"output-zeta0.25.csv")
                        penalty=penalty*11.8
            
                    budget=budget*5
                kappa=kappa+1
            zeta=zeta+0.05
