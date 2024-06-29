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
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        tmp_column = []
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                tmp_column.append(data[column].iloc[i])
        tmp_column.sort()
        value = len(tmp_column) / 2
        if value < len(tmp_column):
            if value % 1 == 0:
                median_result[column] = (tmp_column[int(value)] + tmp_column[int(value) - 1]) / 2
            else:
                median_result[column] = tmp_column[int(value)]    
    result['median'] = median_result


def first_quartile(data, result):
    first_quartile_result = {}
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        tmp_column = []
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                tmp_column.append(data[column].iloc[i])
        tmp_column.sort()
        value = len(tmp_column) / 4
        if value < len(tmp_column):
            if value % 1 == 0:
                first_quartile_result[column] = (tmp_column[int(value)] + tmp_column[int(value) - 1]) / 2
            else:
                first_quartile_result[column] = tmp_column[int(value)]
    result['first_quartile'] = first_quartile_result

def third_quartile(data, result):
    third_quartile_result = {}
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')
        tmp_column = []
        for i in range(len(data.index)):
            if not math.isnan(data[column].iloc[i]):
                tmp_column.append(data[column].iloc[i])
        tmp_column.sort()
        value = len(tmp_column) / 4
        if value < len(tmp_column):
            if value % 1 == 0:
                third_quartile_result[column] = (tmp_column[int(value)*3] + tmp_column[int(value)*3 - 1]) / 2
            else:
                third_quartile_result[column] = tmp_column[int(value)*3]
    result['third_quartile'] = third_quartile_result

result = pd.DataFrame()

count(data, result)
mean(data, result)
std(data, result)
min(data, result)
first_quartile(data, result)
median(data, result)
third_quartile(data, result)
max(data, result)

print(result.T)
print(data.describe())
