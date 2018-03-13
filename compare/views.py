from django.shortcuts import render
from compare.forms import NewTicker
import os
import datetime as dt
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

def index(request):
    """
    form = NewTicker()

    if request.method == 'POST':
        form = NewTicker(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print("ERROR!")
    """
    return render(request,'compare/index.html')

def compare(request):
    def graphing():
        style.use('ggplot')

        start = dt.datetime(2012,1,1)
        end = dt.datetime(2016,12,31)

        df = pd.read_csv("compare/sp500_joined_closes.csv", parse_dates=True, index_col=0)

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

        ax1.plot(df.index, df['F'])
        ax1.plot(df.index, df['INTC'])
        plt.legend()

        plt.plot()
        #os.chdir('..')
        plt.savefig('static/images/foo.png', transparent=True)

    #def fundamentals(request):


    graphing()

    return render(request, "compare/compare.html")
