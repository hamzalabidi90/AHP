
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import numpy as np



def val(column,values):
    new_list =[]
    x=0
    for i in range(1,len(column)+1):
        for j in range(1,len(column)+1):
            if(j == i):
                new_list.append(1)
            elif( i < j ):
                new_list.append(values[x])
                x= x+1
                
            elif ( j < i ) and (i == len(column)) :
                new_list.append(round(1/new_list[i*j-1],2))
                

            elif ( j < i ):
                new_list.append(round(1/values[i-j-1],2))

    table = pd.DataFrame(np.array(np.reshape(np.array(new_list),(-1,len(column)))),
                                        columns=np.array(column),
                                        index=np.array(column) )
    print(table)

 