import os
import nltk.data
import re
import operator
import csv

pattern = re.compile("CEO [A-Z][a-z]* [A-Z][a-z]*")

path = '/Users/Divir/Desktop/Geeklife/Python Projects/NLP/data/'
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def clean_name(name):
    return name.lower()

def store_ceo_names():
    # open file to write
    with open('ceo_names.txt', 'w+') as write_file:
        # iterate over every file in dir
        for filename in os.listdir(path):
            with open(path+filename, 'r+') as read_file:
                data = read_file.read()
                # split text into lines
                for line in tokenizer.tokenize(data):
                    # write to file if 'CEO' is in line
                    if 'CEO' in line: write_file.write(line+'\n')

def get_ceo_dict(company_name):
    company_name = company_name.lower()
    d = {}
    with open('ceo_names.txt', 'r+') as f:
        data = f.read()
        for line in tokenizer.tokenize(data):
            if all(word in line.lower() for word in ['ceo', company_name]):
                names = re.findall(pattern, line)
                clean_names = [clean_name(name) for name in names if clean_name(name) != company_name]
                for name in clean_names:
                    name = name[4:] # remove 'CEO'
                    d[name] = d.setdefault(name, 0) + 1
    return d


def find_ceo(company_name):
    d = get_ceo_dict(company_name)
    return max(d.iteritems(), key=operator.itemgetter(1))[0] if d else 'None'


with open('wiki_ceo_names.csv','rb') as file:
    correct = 0
    incorrect = 0
    reader = csv.reader(file)
    next(reader, None)
    for line in reader:
        company, wiki_ceo = line[0], line[1]
        my_ceo = find_ceo(company).title()
        correct = wiki_ceo == my_ceo
        print "Comany: %-30s WIKI CEO: %-30s My CEO: %-30s Correct: %s" % (company, wiki_ceo, my_ceo, correct)
        if correct: correct += 1
        else: incorrect += 1
    print "Correct: %d  Incorrect: %d" % (correct, incorrect)