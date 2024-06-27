import sys
import pandas as pd
import math

sys.dont_write_bytecode = True

# data = pd.read_csv('datasets/dataset_test.csv')
data = pd.read_csv('datasets/dataset_train.csv')


def count(data, result):
    count_result = {}
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        count = 0
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                count += 1
        count_result[column] = count
    result['count'] = count_result

def mean(data, result):
    mean_result = {}
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        sum = 0
        div = 0
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                sum += data[column].iloc[i]
                div += 1
        if div > 0:
            mean_result[column] = sum / div
        else:
            mean_result[column] = 'NaN'
    result['mean'] = mean_result

def std(data, result):
    std_result = {}
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        sum = 0
        div = 0
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                sum += data[column].iloc[i]
                div += 1
        if div > 0:
            mean = sum / div
            sum = 0
            for i in range(len(data.index)):
                if not math.isnan(data[column].iloc[i]):
                    sum += (data[column].iloc[i] - mean) ** 2
            std_result[column] = math.sqrt(sum / div)
        else:
            std_result[column] = 'NaN'
    result['std'] = std_result

def min(data, result):
    min_result = {}
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        min = 'NaN'
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                if min == 'NaN':
                    min = data[column].iloc[i]
                elif data[column].iloc[i] < min:
                    min = data[column].iloc[i]
        min_result[column] = min
    result['min'] = min_result

def max(data, result):
    max_result = {}
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        max = 'NaN'
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                if max == 'NaN':
                    max = data[column].iloc[i]
                elif data[column].iloc[i] > max:
                    max = data[column].iloc[i]
        max_result[column] = max
    result['max'] = max_result
    
def median(data, result):
    median_result = {}
    
# def median(line):	

# def third_quartile(line):


result = pd.DataFrame()

count(data, result)
mean(data, result)
std(data, result)
min(data, result)
max(data, result)
median(data, result)

print(result.T)
print(data.describe())
