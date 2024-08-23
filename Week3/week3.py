import numpy as np
import matplotlib.pyplot as plt

def Sl_regressor(x,y):
    x=np.array(x)
    y=np.array(y)

    x_mean=x.mean()
    y_mean=y.mean()

    numerator = ((x-x_mean)*(y-y_mean)).sum()
    denominator = ((x-x_mean)**2).sum()
    slope = numerator/denominator
    intercept = y_mean - slope * x_mean

    return slope, intercept

x=list(map(float, input("Enter the values for x (space-separated): ").split()))
y=list(map(float, input("Enter the value for y (space-separated): ").split()))

if len(x) != len(y):
    print("Error: x and y must have the same number of elements.")
else: 
    slope, intercept = Sl_regressor(x,y)

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    plt.scatter(x,y, color='blue', label='Data Points')

    reg_line = [slope *xi + intercept for xi in x]
    plt.plot(x, reg_line, color='red', label=f'Line: y = {slope: .2f}x + {intercept: .2f}')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Simple Linear Regression')
    plt.legend()

    plt.show()