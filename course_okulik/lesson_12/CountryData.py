import json

from trio import open_file


class CountryData:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.open_file()
        self.country = self.data['Country']
        self.avg_temp = self.data['avg_temp']


    def open_file(self):
        file_data = open(self.filename)
        data = json.load(file_data)
        print(f'Содержимое файла: {data}')
        print('=================================================')
        file_data.close()
        return data

data1 = CountryData('data1.txt')
print(data1.country)
print(data1.avg_temp)

data2 = CountryData('data2.txt')
print(data2.country)
print(data2.avg_temp)