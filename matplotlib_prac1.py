import matplotlib.pyplot as plt
grade=[40,40,35,60,75]
plt.pie(grade)
my_colours=['green','yellowgreen','blue','lightblue','purple']
my_labels=['L001','L002','L003','L004','L005']
explode=(0.1,0.1,0.1,0.1,0.1) #one value for each slice
plt.pie(grade, explode=explode, colors=my_colours,labels=my_labels,
shadow=True)
plt.show()
