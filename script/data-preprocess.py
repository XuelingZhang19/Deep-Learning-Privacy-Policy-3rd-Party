from bs4 import BeautifulSoup
import csv
import os
import pandas as pd
import re
import string
from string import punctuation

#=================================================================================================generate binary lable for each html
# htmlpath = '/home/xueling/deepLearning/OPP-115/sanitized_policies/'
# csvpath = '/home/xueling/deepLearning/OPP-115/consolidation/threshold-0.5-overlap-similarity/'
outpath = '/home/xueling/deepLearning/out/'
# files = os.listdir(htmlpath)
# fileName = []
#
#
# # htmfile = '/home/xueling/deepLearning/OPP-115/sanitized_policies/1017_sci-news.com.html'
# for file in files:
#     if not os.path.isdir(file) and (os.path.getsize(htmlpath + '/' + file) > 0):
#         fileName.append(file)
#
# for item in fileName:
#
#     html = open(htmlpath + item, 'r')
#     content = html.read()
#     soup = BeautifulSoup(content)
#     list_segment = soup.text.split('|||')
# # print len(list_segment)
#     #================================================================================read csv
#     set_index = set()
#     indexs = []
#     segment_lable = [0] * len(list_segment)
#     csvfileName = item[:-4] +'csv'
#     csv_file = csv.reader(open(csvpath+csvfileName))
#     column_4 = []
#     column_5 = []
#     for row in csv_file:
#         column_4.append(row[4])
#         column_5.append(row[5])
#
#     set_index = [i for i, x in enumerate(column_5) if x == 'Third Party Sharing/Collection']
#     print csvfileName + str(set_index)
#
#     for item in set_index:
#         indexs.append(item)
#     # print indexs
#
#     for i in range(0, len(indexs)):
#         segment_lable[int(column_4[int(indexs[i])])]= 1
#
#     segment_lable = zip(list_segment, segment_lable)
#
#     csv.writer(open(outpath + csvfileName, 'w')).writerows(segment_lable)


#==============================================================================================================consolidate the data into one csv
# csv_writer = open('/home/xueling/deepLearning/dataset.csv', 'w')
# files = os.listdir(outpath)
# for file in files:
#     csv_data = pd.read_csv(outpath+file, header=None)
#     print(csv_data.shape)
#     csv_data.to_csv(csv_writer, mode='a', index=False, header=False)

#=====================================================================================remove the punctuation
lines = open('/home/xueling/deepLearning/dataset_0.csv').readlines()

# csv_data = pd.read_csv('/home/xueling/deepLearning/dataset.csv', header=None)
# csv_writer = open('/home/xueling/deepLearning/dataset_trimed.csv', 'w')
print len(lines)
file_writer = open('/home/xueling/deepLearning/dataset_trimed.csv', 'w+')
for line in lines:
    # line = line[:-3]
    table = string.maketrans(punctuation, ' '*len(punctuation))
    line = line.translate(table)
    line = unicode(line, "utf-8")
    line = line.replace(u'\xa0', u' ')
    line = re.sub('\s+', ' ', line).strip()
    line = line.replace(u'\u201c', "\"")
    line = line.replace(u'\u201d', "\"")
    print line
    file_writer.writelines(line+'\n')

   # sentences = nltk.sent_tokenize(fullText)

        # for sentence in sentences:
        #     sentence = remove_Numbered_Lists(sentence)
        # preprocesses.append(sentence)
file_writer.close()