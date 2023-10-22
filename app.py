import csv
from opencc import OpenCC
import numpy

with open('./source_data/Schinese/CurrentLanguage/future.csv', newline='') as futureData:
  rows = csv.reader(futureData)

  for row in rows:
    print(row)

cc = OpenCC('s2twp')
text = '所有穿梭机都可以在此处停靠、补充燃料，用来进行仓库之间远距离资源运输任务，以及穹顶间居民再分配的任务。'
print(cc.convert(text))

ironmen = numpy.array([46, 8, 11, 11, 4, 56]) # 將 list 透過 numpy 的 array 方法進行轉換
print(ironmen) # 看看 ironmen 的外觀
print(type(ironmen)) # 看看 ironmen 的資料結構
articles = ironmen * 30
print(articles)