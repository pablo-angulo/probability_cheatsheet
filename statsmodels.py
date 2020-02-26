import statsmodels.formula.api as smf
regr = smf.ols("Sales ~ TV + Radio", advertising).fit()
est.predict(advertising_future)
regr.summary()
