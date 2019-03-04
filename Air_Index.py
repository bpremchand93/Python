# Python program to find the good air quality site to live for astma patient.
import pandas as pd # Data processing library
import os # Deals with file path and directory
import time # time library
import matplotlib.pyplot as plt # plotting library
import seaborn as sns # visualization tool

# To measure the program execution timing start time has taken
t0 = time.time()

# Changing the current working directory
Mydir = os.chdir(r"C:\Users\PremChand\Desktop\lab")

# Reading CSV file using pandas dataframe
file1 = pd.read_csv("LaqnData_OxfordRd_d.csv")
file2 = pd.read_csv("LaqnData_Putney_d.csv")

# .csv file has been stored in the dataframes.
df1 = pd.DataFrame(file1)
df2 = pd.DataFrame(file2)

# Appending two dataframe(df1 & df2) and stored it in the new dataframe(df3)for further analysis.
df3 = df1.append(df2)

#Replacing the negative values from the reading column to 0, because negative values may occured due to air quality device error.
df3[df3["Value"]<0.0]=0.0

#To find the outlier in air index readings below function has created to plot the data in box plot using seaborn.
#Box plot and Stripplot has been plotted to show the air quality reading details.
class reading_boxplot:
    def outlier_find(self):
        pal = sns.color_palette("Paired")
        sns.boxplot(y=list(df3["Value"]),data=df3,palette=pal, fliersize=0)
        ax=sns.stripplot(y=list(df3["Value"]), data=df3, jitter=True, dodge=True, linewidth=0.5,palette=pal)
        ax.set_title("To find the outlier in the air index value")
        ax.set_xlabel("Sites")
        ax.set_ylabel("Air Index Reading")
        plt.show()

df_reading_value = reading_boxplot()
df_reading_value.outlier_find()

# As per boxplot, outlier has been identified and processed only the readings between 0 to 150 unit values for further processing.
df3 = df3[(df3["Value"] > 0) & (df3["Value"] <= 150)]

# Replacing unit values as below.
df3["Units"] = df3["Units"].replace(["ug m-3","ug/m3"], "ug m-3")
df3["Units"] = df3["Units"].replace(["mg m- 3", "mg  m-3"], "mg m-3")
df3["Units"] = df3["Units"].replace(["ug m -3 as NO 2", "ug m-3 as NO 2"], "ug m-3 as NO2")

#Below function will do data cleaning operations. When the datatype is object then changing those columns to uppercase apart from unit column.
#If the dataframe contains datetime value, then left stripping "0" for date and month,
#then reformat datetime column to US datetime format (i.e: month, date, year and time) to avoid mixed data formats.
class df_formatting():
    def df_cleaning(self,ex_df_column):
            for d in df3.columns:
                if(df3[d].dtype.kind == "O") &  (d != ex_df_column):
                    if(df3[d].str.contains(r"\d{2}/\d{2}/\d{4} \d{2}:\d{2}").all()):
                        dd=df3[d].str.split("/").str[0].str.lstrip("0")
                        mm=df3[d].str.split("/").str[1].str.lstrip("0")
                        yy_time=df3[d].str.split("/").str[2]
                        df3[d] = mm+"/"+dd+"/"+yy_time
                        df3[d] = pd.to_datetime(df3[d])
                    else:
                        df3[d]=df3[d].apply(lambda x: x.upper())
                #else dont"t do anything just continue
                else:
                    continue

# Calling the dataframe column formatting function
df_class = df_formatting()
df_class.df_cleaning("Units")


# As given in the requirement, John Dohorty is working hours from 09:00 AM to 17:00PM, and his commuting time is 10 min, doing his
# workout timing after his work is 1 hours. I assume he will be working everyday(i.e weekdays, weekends & public holiday).
# While considering the above factors air quality values has processed only between
# 00:00AM to 09:00AM and 17:00PM to 00:00AM for further processing.
index = pd.DatetimeIndex(df3["ReadingDateTime"])
df3 = df3.iloc[(index.indexer_between_time("17:00", "09:00"))]
df3 = df3.reset_index(drop=True)

# Dataframe has stored in the output csv file.
df3.to_csv("Airindex_output_file.csv", sep=",", encoding="utf-8", index=False)

# Grouped the species and site column; hence outlier has detected median has used to plot the barplot.
ax = df3.groupby(["Species", "Site"]).Value.median().unstack().plot(kind="bar")

# Below function created to add the cummulative unit value to each bars.
def stackedbar_autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, rect.get_y() + rect.get_height() / 2, "{:.1f}".format(height),
            ha="center", va="center")

# Calling the autolabel function
stackedbar_autolabel(ax.patches)

# matplotlib.patch.Patch properties
props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
textstr = (r"WA9 Site is suitable for Astma Patients as per the median value of species")

# Text box has been placed in the upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment="top", bbox=props)

# Added the plotting margin, title, axis names
plt.subplots_adjust(bottom=0.2, top=0.8)
plt.title("Air Index for WA6 & WA9 Sites from Jan 2018 to Dec 2018")
plt.ylabel("Air Index Values")
plt.show()

# Calculating end time
t1 = time.time()

# Calculating end time - start time to measure the python code total execution time
total = ((t1 - t0) / 60)
print("Job execution timing {0} Minutes".format(str(round(total, 3))))

# Conclusion:
# As given in the requirement, following data cleaning has been done in the datasets.
# 1. Replaced the units in the species unit column.
# 2. Identified the negative reading values and replaced with 0, because those values may obtained during device error condition.
# 3. Upper case has changed to all the columns in the dataframe except species unit column.
# 4. Outlier has identified in the air index values and excluded those values, to not affects the mean value.
# 5. Modified the datatime column from object to datatime datatype, then datatime column values changed to mm/dd/yy hh:ss (US date format)
#
# Once data cleaning and outlier has identified, plot has made only for the air index value between 00:00 AM to 09:00 AM and 17:00PM to 00:00AM.
# Based on the generated bar graph, it is clear that WA9 site is suitable for John Doherty(Astma patient).
# Note: I assumed John Doherty will be working everyday(i.e Working days, weekends & public holidays)
