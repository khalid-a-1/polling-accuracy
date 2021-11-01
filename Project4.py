#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amna Khalid
October 24, 2018
Project4.py
This project investigates how polling size affects the accuracy of
polling results.
"""
import random
import numpy as np
import matplotlib.pyplot as plt


def poll (percentage,pollSize):
    '''
    This function tells us how much of the population agrees or 
    says 'yes' to the statement being polled.
    PARAMETERS:
        percentage - % of people that agree 'yes'
        pollSize - number of people being polled
    RETURN VALUE:
        Percentage of people that said yes in the poll
    '''
    s = 0
    for step in range(1, pollSize):
        r =  random.random()
        if r <= percentage:
            s = s + 1
        
    return (s / pollSize) * 100


def max_(numss):
    '''
    This function lists the maximun values in the list of poll 
    results.
    PARAMETERS:
       numss - list of pollResults
    RETURN VALUE:
        y - max value
    '''      
    y = numss[0]
    for i in range(len(numss)):
        if numss[i] >= y:
            y = numss[i]
            
    return y
    

def min_(nums):
    '''
    This function lists the minimun values in the list of poll 
    results.
    PARAMETERS:
       nums - list of pollResults
    RETURN VALUE:
        x - min value
    '''   
    x = nums[0]     
    for i in range(len(nums)):
        if nums[i] <= x:
            x = nums[i]
    
    return x

def pollExtremes (percentage,pollSize,trials):
    '''
    This function shows the variation in the maximum and minimun 
    values in the lists. 
    PARAMETERS:
        percentage - % of people that agree 'yes'
        pollSize - number of people being polled
        trials - number of times the poll is repeated
    RETURN VALUE:
        maxPollSize - maximum value in the list of pollResults
        minPollSize - minimun value in the list of pollResults
        
    '''
    
    pollResults = []               
    for trial in range(trials):
        sample = poll (percentage,pollSize)
        pollResults.append(sample)
        
    maxPollSize = max_(pollResults)
    minPollSize = min_(pollResults) 
            
    return  maxPollSize, minPollSize

def plotResults (percentage,minPollSize,maxPollSize,step,trials):
    '''
    This function uses previous functions to investigate how increasing
    poll sizes affect the variation of the poll results and plots a 
    graph of those values.
    PARAMETERS:
        percentage - % of people that agree 'yes'
        minPollSize - minimum value in the appended list of pollResults(above)
        maxPollSize - maximun value in the appended list of pollResults
        step - increments from minPollSize to maxPollSize
        trials - number of times the poll is repeated
    RETURN VALUE:
        (high-low) /  2 - margin of error for the largest poll
    '''
    #Lists needed to plot the graph 
    xLow = []
    xHigh = []
    xList = []
    for pollSize in range(minPollSize, maxPollSize, step):
        low, high = pollExtremes (percentage,pollSize,trials)
        xLow.append(low)
        xHigh.append(high)
        xList.append(pollSize)
    
    #ploting the graph 
    plt.plot(xList, xLow ,c = "navy")
    plt.plot(xList, xHigh, c = "magenta")
    plt.title("Effect of Polling Size on Accuracy")
    plt.xlabel("Poll Size")
    plt.ylabel("Percentage of Yes" )
    plt.legend(["Maximun Yes","Minimun Yes"])
    
    plt.show()
        
    return (high-low) / 2     


def main ():
    '''
    This function calls above functions. 
    '''
    plotResults (0.30,10,1000,10,100)
    
main ()