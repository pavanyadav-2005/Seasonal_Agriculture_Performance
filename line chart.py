import pandas as pd 
import matplotlib.pyplot as plt
data={
    "season":["kharif","Rabi","zaib"],
    "production":[82387.61,67498.88,23098.35],
}
df=pd.DataFrame(data)
df.plot(x="season",y="production",kind="line")
plt.title("production by seasonal")
plt.xlabel("Type of season")
plt.ylabel("sum of production")
plt.show()