'''describe different citiesdevelopement'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data_analysis:
    """draw the trend of whole year for all city in Guangdong province
    the row are city names representively(no more than 20) 
    while the coulumn is the year representively(no more than 9)
    """
    
    def __init__(self,year,csv_filename,num=20):
        """from year=2000 to year = 2018 you choose.
        {'2000':0,'2005':1,'2010':2,'2012':3,'2013':4,
        '2014':5,'2015':6,'2016':7,'2017':8,'2018':9}"""
        self.year = str(year)
        self.csv_filename = csv_filename
        abc = pd.read_table(csv_filename, sep=',', header = 0)
        data = abc.stack()
        self.data_raw = abc
        self.data = data
        self.num = num
            
    def __onecity__(self,k):
        """1:open the 'enquire.py' to enquire the number correspond to the city and give k.
         2: return The Number of Industrial Enterprises"""
        year_num = {'2000':0,'2005':1,'2010':2,'2012':3,'2013':4,'2014':5,'2015':6,'2016':7,'2017':8,'2018':9}
        year = self.year
        row = year_num[str(year)] + 1  
        column = k 
        city = self.data[k][0]
        self.city = city
        self.k= k
        template = "The Number of Industrial Enterprises in {0} in {1} year is {2}."
        return template.format(city, year, self.data[column][row])
    
    def overall_picture(self):
        """each city line in a same image"""
        j = int(self.num) + 1
        for i in range(j):
            nums = self.data[i]
            print(nums)
            num_a = nums[1:]
            num_a.plot(kind = 'line',title = 'The Number of Industrial Enterprises in different city')

    def city_rank(self):
        """sort value which is based Number of Industrial Enterprises (unit) on different year in
        Ascending order and output a csv document on the floder with this file."""
        self.data_raw = self.data_raw.sort_values(self.year)
        self.data_raw.to_csv('output_ranke({0}).csv'.format(self.year),encoding='gb2312')
    
    def a_picture_city(self):
        """a bar graph for one city in different year"""
        result1 = []
        year = ['2000','2005','2010','2013','2014','2015','2016','2017','2018']
        for i in range(1,10):
            get_data = int(self.data[self.k][i])
            result1.append(get_data)
        df = pd.DataFrame({'The Number of Industrial Enterprises': result1}, index=year)
        ax = df.plot.bar(rot=0)
        ax.set_title('{}'.format(self.data[self.k][0]))
            
              
efg = Data_analysis(2005,'12-09-01.csv')###example
print(efg.__onecity__(4))####' Foshan'
efg.overall_picture()
efg.a_picture_city()
efg.city_rank()


        


        
        