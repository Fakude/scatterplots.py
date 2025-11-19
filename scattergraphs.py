import matplotlib.pyplot as plt
import numpy as np


# scatter graph show the relationships between two variables 
# helps to identify a correlation (+,-,none)
# Example: study hours vs Tests scores 

x1 = np.array([0,1,2,3,4,5,6,7,8,9])
y1 = np.array([50,53,56,58,60,70,78,75,80,85])

x2 = np.array([0,1,2,3,4,5,6,7,8,2])
y2 = np.array([50,67,60,58,55,76,74,75,89,66])

plt.scatter(x1,y1,label="Boys")
plt.scatter(x2,y2, color = "Pink",
            label="Girls")

plt.title("Test Marks Vs study Time")
plt.xlabel("Study Hours")
plt.ylabel("Test Mark")

plt.legend(loc="upper left")


plt.show()