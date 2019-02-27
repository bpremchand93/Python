import pandas as pd
import numpy as np

class demo1:
    def create_series_demo(self):
         acm_Events = pd.Series(["HourOfCode", "Revision Class", 5, 12], index=['w','x','y','z'])
        #print(acm_Events)
         acm_Events['y'] = "Class Trip"
         print("Is w in Events? {}\n".format("w" in acm_Events))
         print(acm_Events)
        # print()

    def dictionary_converter(self):
         p_book = {"R Lennon": 6355, "T Dowling": 6304} # dictionary of phone numbers
         phone_book = pd.Series(p_book) # convert dictionary to Series
         print(phone_book)

    def Series_Demo3(self):
         acm_Events = pd.Series(["HourOfCode", "Revision Class", 5, 12], index=['w','x','y','z'])
         student_grades = pd.Series([77,65,59,38],index=["Joe","Mary",'Mick',"Jane"])
         print(student_grades / 4) #avg
         # print(" \n{}\n".format(np.square(student_grades)))

         student_grades2 = pd.Series([71, 70, 60, 45], index=["Harry", "Mary", "Mick", "Jane"])
         nu_Series=acm_Events[2:3] #slicing
         # print(nu_Series)
         print(student_grades2)
         #see what happens if you change Harry to Jane

         s_g3 = student_grades + student_grades2 #grades can be added but this is not reliable
         print("\n {} \n".format(s_g3))
         print("\n {} \n".format(s_g3.isnull()))

d = demo1()
# d.create_series_demo()
# d.dictionary_converter()
d.Series_Demo3()
