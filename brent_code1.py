import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

df = pd.DataFrame({'x1':pd.Series([1, 1.25, 2, 2.50]),
                   'x2':pd.Series([30, 35, 43, 28]),
                   'y':pd.Series([100, 78, 42, 31],
                    index=list(range(4)))})
#print(df)
X = df[['x1', 'x2']]
#print(X)
y = df['y']
#print(y)
regression = linear_model.LinearRegression()
regression.fit(X, y)
#print(regression.coef_)
#print(regression.predict([[0, 0]]))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x1'], df['x2'], df['y'], c = 'r', marker = 'o')
xx1, xx2 = np.meshgrid(range(1, 4), range(25, 45))
yy = -45.25*xx1 - 0.886*xx2 + 169.23
ax.plot_surface(xx1, xx2, yy, alpha=0.5)
plt.show()