import csv
from opencc import OpenCC
import numpy

cc = OpenCC('s2twp') # 簡體中文 -> 繁體中文 (台灣, 包含慣用詞轉換)
# './source_data/Schinese/CurrentLanguage/future.csv'
def translate_game_file(source_path, target_path):
  # future
  data_array = []
  with open(source_path, newline='') as futureData:
    rows = csv.DictReader(futureData)

    for row in rows:
      # print(cc.convert(row['Translation']))
      data_array.append(row)


  for data in data_array:
    data['Translation'] = cc.convert(data['Translation'])


  with open(target_path, 'w', newline='') as csvfile:

    fieldnames = ['ID', 'Text', 'Translation', 'Old Text', 'Old Translation', 'Status', 'Gender', 'Critical Warnings', 'Non-critical Warnings', 'Platform Warnings', 'Location', 'Context', 'Section', 'Actor', 'Voice Actor', 'Revision', 'Old Revision', 'Edit Distance']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()

    for newData in data_array:
      writer.writerow(newData)


translate_game_file('./source_data/Schinese/CurrentLanguage/future.csv', './dist/Hantchinese/CurrentLanguage/future.csv')
translate_game_file('./source_data/Schinese/CurrentLanguage/Game.csv', './dist/Hantchinese/CurrentLanguage/Game.csv')
translate_game_file('./source_data/Schinese/CurrentLanguage/picard.csv', './dist/Hantchinese/CurrentLanguage/picard.csv')
translate_game_file('./source_data/Schinese/CurrentLanguage/prunariu.csv', './dist/Hantchinese/CurrentLanguage/prunariu.csv')
translate_game_file('./source_data/Schinese/CurrentLanguage/zubrin.csv', './dist/Hantchinese/CurrentLanguage/zubrin.csv')
