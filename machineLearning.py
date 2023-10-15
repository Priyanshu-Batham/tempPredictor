import numpy as np
from sklearn.linear_model import LinearRegression
from database import getData
import matplotlib.pyplot as plt

# Sample dataset
def predict():
    rawData = getData()
    nextDay = rawData[-1][0]+1

    data = np.array(rawData)

    # Split the data into input sequences and target values
    X = data[:, 0].reshape(-1,1)
    y = data[:, 1]

    # Create and train a Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict the next number in the sequence
    nextDayTemp = model.predict([[nextDay]])[0]
    nextDayTemp = round(nextDayTemp, 2)
    print(f"The predicted temperature for tomorrow, (day:{nextDay}) is: {nextDayTemp}")
    return [nextDay, nextDayTemp]
# -------------------------------------------------------------------------->>>>>>>>>>>>

def plotDataFromDataset():
  
    data = getData()

    # Separate data into x and y values
    days = [item[0] for item in data]
    temps = [item[1] for item in data]

    # Create a line plot
    plt.figure(figsize=(8, 6))
    plt.plot(days, temps, marker='o', linestyle='--', color='b')
    
    # Add labels and a title
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.title('Temperature Data Over Time')

    # Show the plot
    plt.grid(True)
    plt.show()