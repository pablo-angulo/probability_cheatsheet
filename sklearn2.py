advertising_future = pd.DataFrame(
    [  [100,30,30],
       [100,40,30],
    ],
    columns=["TV", "Radio", "Newspaper"]
)
regr.predict(advertising_future)
