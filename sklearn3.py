from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X = poly.fit_transform(auto[["horsepower"]])
y = auto["mpg"]
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25)
regr = skl_lm.LinearRegression()
regr.fit(Xtrain,ytrain)
print(regr.score(Xtest, ytest))
regr.predict(poly.fit_transform([[250]]))
