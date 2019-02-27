import pandas as pd
import numpy as np
import os
# airport_csv = pd.read_csv(os.path.normpath('C://Users//PremChand//Desktop//airports.csv'))
airports_csv = pd.read_csv(os.path.normpath(r'C:\Users\PremChand\Desktop\airports.csv'))
# print(airports_csv.count())

class airports:
    def DFrame_Init_Data(self):
        #  column_name = ['id', 'ident', 'type', 'name', 'latitude_deg', 'longitude_deg',
        # 'elevation_ft', 'continent',
        #  'iso_country', 'iso_region', 'municipality', 'scheduled_service',
        # 'gps_code', 'iata_code',
        #  'local_code', 'home_link', 'wikipedia_link', 'keyword']
         #column_names can be passed in using names=column_name or they can be inferred
         # airports_csv = pd.read_csv(os.path.normpath('airports.csv'),delimiter=',',
         #                            header=None,skip_blank_lines=True)
         print(airports_csv[['id','name', 'latitude_deg', 'longitude_deg']].head(6))
         print()
    # print(airports_csv.count()) #show a count of values
    # print(airports_csv.info()) #show a count of values
    # print(airports_csv.head(10)) #show a sample of the first 4 rows
    # print(airports_csv.keys()) #show the headers/keys
air=airports()
air.DFrame_Init_Data()
