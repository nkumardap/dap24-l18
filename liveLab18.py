"""
Economic booms and busts have always existed, but are they getting worse? Or
better? In this exercise we'll be looking at the relative variance of US GDP 
over the last few decades. A side benefit: getting to know the groupby method 
in greater detail!
"""

"""
EXERCISE 1
Get GDP data from FRED, from 1950 to 2023. Perform any operations you might
need to in order to "clean" it.
"""

"""
EXERCISE 2
Normalize the GDP

If we merely look at raw variance, it will obviously be rising over time, as 
GDP is rising over time. First we need to "normalize" the GDP by dividing the
GDP in a particular time period with the average GDP of that decade.

Calculate the mean GDP by decade. Create an "adjusted_gdp" column that is
(GDP/mean_GDP)

Hints: - The // is the "floor division" operator in Python e.g. 1962 // 10 = 196

- The groupby method creates a DataFrame object that can be merged back into 
the original dataframe

- The groupby object creates a dataframe that has a method mean() that will return
the average value of series. So df.groupby('A')['B'].mean() will group by A and 
return the mean value of B
ref: https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.core.groupby.GroupBy.mean.html
"""

"""
EXERCISE 3
Get the relative variance by decade, then plot the relative variance over
time.

Hint: - The groupby object is a dataframe with a var() method that works 
similarly to the above

- You don't need to merge it back into the original dataframe for this graph.
"""