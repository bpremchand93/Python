import pandas as pd

class demo1:
    def create_series_demo(self):
        acm_event=pd.Series(["Hours of code","Revision Class",5,12],index=['w','x','y','z'])
        acm_event['y'] = "Class Trip"
        print("Is w in Events? {}\n".format("w" in acm_event))
        # acm_event = pd.Series(p_book)
        # acm_event='test'
        # print(acm_event)

d=demo1()
d.create_series_demo()
