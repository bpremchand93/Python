import matplotlib.pyplot as plt
# data=[20,21,23,24,26,28,29,33,35,39,45,46,18]
data=[20,21,17,18,20,21,20,20,19,18,19,20,31,20,20,19,18]
data2=[30,28,27,28,25,24,25,22,20,18,19,22,29,22,22,20,21]
data3=[21,21,18,19,21,21,21,24,18,17,17,21,17,18,18,18,18]
# plt.plot(data,marker='o', markersize=7,
# markerfacecolor='red', markeredgecolor='blue', markeredgewidth=.5)
plt.hist(data,color="0.6",edgecolor = "0.2", rwidth=0.8)
# plt.annotate('Oldest Student', xy=(12, 31), xytext=(9,
# 28),arrowprops=dict(facecolor='magenta', shrink=0.02),)
# plt.plot(data)
plt.title("Student age in B.sc")
plt.xlabel("Student Number")
plt.ylabel("Age")
plt.grid()
plt.show()
# plt.savefig('plt1.png')
