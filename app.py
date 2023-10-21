import csv
from opencc import OpenCC

with open('./source_data/Schinese/CurrentLanguage/future.csv', newline='') as futureData:
  rows = csv.reader(futureData)

  for row in rows:
    print(row)

cc = OpenCC('s2twp')
text = '所有穿梭机都可以在此处停靠、补充燃料，用来进行仓库之间远距离资源运输任务，以及穹顶间居民再分配的任务。'
print(cc.convert(text))
