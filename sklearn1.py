import sklearn.linear_model as skl_lm
regr = skl_lm.LinearRegression()
X = advertising[["TV", "Radio", "Newspaper"]]
y = advertising["Sales"]
regr.fit(X,y)
print(regr.score())
