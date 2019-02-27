import pandas as pd
import numpy as np
import os
# airport_csv = pd.read_csv(os.path.normpath('C://Users//PremChand//Desktop//airports.csv'))
airports_csv = pd.read_csv(os.path.normpath(r'C:\Users\PremChand\Desktop\airports.csv'))
# print(airports_csv.count())

class air:
    def DFrame_select_rows(self):
        global airports_csv
        print("\nRow Data\n")
         #Type 1
        sml_tbl= airports_csv[['name','latitude_deg','longitude_deg']]
        print(sml_tbl[(sml_tbl.latitude_deg < 59)])
         # Type 2
        nu1 =airports_csv[3:6]#new DataFrame with rows 3 to 5 only (from 3 to less
                                # than 6)
        print("\nnu DataFrame\n{}".format(nu1))
        nu2= airports_csv[['name']][3:6]#as before but display only name column
        print("\nnu2 DataFrame\n{}".format(nu2))

a=air()
a.DFrame_select_rows()
