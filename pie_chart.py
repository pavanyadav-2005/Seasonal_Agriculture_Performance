import matplotlib.pyplot as plt
x=["Chilli","Cotton","GroundNut","Maize","Pulses","Rice","Sugarcane","Wheat"]
y=[3232.34,3916.1,3167.57,4428.05,4002.37,5410.91,2535.26,4860.46]
plt.pie(y,labels=x,autopct="%1.1f%%")
plt.title("Sum of hectures by type of crop")
plt.show()