import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 
import seaborn as sns


def message_distribution_plot(df, t='day'):
    """Set t to day, week, month or year"""
    
    plt.figure(figsize=(15,10))
    plt.title(f'Distribution of messages by {t}')
    plt.ylabel(f'Number of messags per {t}')
    
    return df.resample(t[0].lower()).count().sort_values('user', ascending=False).loc[:,'user'].plot()


def value_counts_plot(df):
    """
    Value counts plots with t variable to set the timeline
    
    Use df = df.dayweek / df.week / etc
    """
    
    plt.figure(figsize=(15,10))
    
    #get rid of sort_index() to change the graph
    return df.value_counts().sort_index().plot(kind='bar')


def value_counts_plot_sns(df, t_column):
    """
    Value counts plots with t variable to set the timeline
    
    Using Seaborn
    """
    
    plt.figure(figsize=(15,10))
    
    return sns.countplot(
        data = df,
        x = t_column,
        #order = df.month.value_counts().index 
    )
    
    
def value_counts_plot_sns_hue(df, t_column, hue):
    """
    Value counts plots with t variable to set the timeline
    
    Using Seaborn and hues
    """
    
    plt.figure(figsize=(15,10))
    plt.title = f'Message per {t_column} & by {hue}'
    
    return sns.countplot(
        x= t_column,
        data = df,
        hue = hue
        )