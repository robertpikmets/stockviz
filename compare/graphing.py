import os
import datetime as dt
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2012,1,1)
end = dt.datetime(2016,12,31)

df1 = pd.read_csv("sp500_joined_closes.csv", parse_dates=True, index_col=0)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

ax1.plot(df1.index, df1['AAPL'])
ax1.plot(df1.index, df1['MSFT'])

plt.plot()
os.chdir('..')
plt.savefig('static/images/foo.png')
plt.show()
