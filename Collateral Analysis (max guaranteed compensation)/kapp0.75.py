import os
import sys
txval=5000
path=5


for z in os.listdir(sys.argv[1]):
    
    
        divide=0.75
        zeta=0.0375
        
        while zeta<=0.375:
            kappa=1
            while kappa<=1:
                budget=5000000
                while budget<=700000000:
                    
                    txval=20000
                    while txval<=20000:
                        path=int(divide/zeta)
                        penalty=(2*zeta*zeta)/(2*zeta*100+100*(divide-zeta))
                        print(z)
                        k="snapshots/"+z
                        print(k)            
                        os.system("python3 graph_collateral_flowconstant.py "+str(k)+" "+str(penalty)+" "+str(divide)+" "+str(zeta)+" "+str(txval)+" "+str(path)+" "+str(budget)+" "+str(2016/path)+" "+"output-zeta0.75.csv")
                        txval=txval*2
            
                    budget=budget*5
                kappa=kappa+1
            zeta=zeta*2
