import numpy as np
import csv
from pprint import pprint
import random

test_data = {
    1: (2, 8),
    2: (3, 1),
    3: (4, 2),
    4: (5, 3),
    5: (2, 1)
}

def read_data(file_name):
    data  = {}
    with open(file_name, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            job, time, weight = row
            data[int(job)] = (int(time), int(weight))
    return data

def get_weighted_completion_time(job_order, data):
    times, weights = zip(*[ data[job] for job in job_order ])
    weighted_completion_time = np.dot(np.cumsum(times), weights)
    return weighted_completion_time

def main():
    # job orders
    job_order_1 = '15	17	5	13	18	9	14	6	1	3	21	10	12	8	2	16	7	4	11	20	19'.split()
    job_order_1 = [int(x) for x in job_order_1]
    job_order_2 = [random.randint(1, 21) for x in range(21)]

    data = read_data('single_machine_data.csv')
    sorted_list = sorted([(k, v) for k, v in data.iteritems()], key=lambda x: x[1][0]*x[1][1], reverse=False)
    keys = [x for x, y in sorted_list]
    print sorted_list
    print keys

    wct = get_weighted_completion_time(keys, data)
    print wct, job_order_2




if __name__ == '__main__':
    main()
