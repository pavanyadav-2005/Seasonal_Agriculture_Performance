import matplotlib.pyplot as plt 
x=["chilli","cotton","GroundNut","Maize","Pulses","Rice","Sugarcane","Wheat"]
y=[412,508,424,551,496,690,305,614]
plt.bar(x,y)
plt.title("No.of farmers by type of crops")
plt.xlabel("Types of Crops")
plt.ylabel("No.of farmers")
plt.show()