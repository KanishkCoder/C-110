import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv('data.csv')
data = df["temp"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
#std_dev = statistics.stdev(dataset)
 #   print("Mean of sample: ", mean)
 # print("Std of sample: ", std_dev)

def show_fig(mean_list):
    df = mean_list
    mean=statistics.mean(mean_list)
    print("mean_of_sampling distribution: ",mean)
    fig= ff.create_distplot([df],['Temprature'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
setup()

def standard_dev():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    std_deviation=statistics.stdev(mean_list)
    print("Std-dev of sampling dis: ",std_deviation)
standard_dev()