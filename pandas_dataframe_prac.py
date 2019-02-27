import pandas as pd #use pandas for series and data frames
import numpy as np # use numpy for square function
class pd_demo_2:
    def DFrame_Init_Data(self):
        bd_class = {'semester_year': ['2019_1', '2019_2', '2019_1', '2019_2'],
                     'student': ['001234', '001234', '001122', '001122'],
                     'BI/ML': [55, 66, 65, 67], 'BDA/DSP': [36, 70, 68, 71], 'DA/PRJ': [60, 70, 70, 72]}
        stu_grades = pd.DataFrame(bd_class, columns=['semester_year', 'student', 'BI/ML', 'BDA/DSP', 'DA/PRJ'])
        print(stu_grades)
pd2 = pd_demo_2() #instantiate class
pd2.DFrame_Init_Data()
