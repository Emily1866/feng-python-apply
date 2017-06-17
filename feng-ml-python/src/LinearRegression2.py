from sklearn.linear_model import LinearRegression

X = [[1, 1, 1], [1, 1, 2], [1, 2, 1]]
y = [[9], [13], [12]]

model = LinearRegression()
model.fit(X, y)

x2 = [[1, 4, 5]]
y2 = model.predict(x2)
print(y2)
