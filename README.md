# a-model-of-guidence-a-graduate-student-to-choose-an-appropriate-city-to-work
Program background
As the philosopher Heraclitus said no man ever steps in the same river twice, for it's  not the same river and he's not the same man. Therefore, making a decision can  change a person’s life. Specifically, if h a graduate student chooses an appropriate city  based on the industry scale of a city to work, they may easy get success in their career.

Structure of the Project
There are three part of project includes getting data, showing data and analysis data.
1. using Beautiful Soup which is a Python library for pulling data out of HTML and 
XML files request data from website and download data. When users run 
‘download1_zip’ can get data from website. There is a ‘class Crawler’ in the 
‘download1_zip’. Now I would introduce the functions of the ‘class Crawler’.
1.1’def __init__(self,endpage)’ is an initializer, which is called whenever a new object 
of that type is created. Having observe the ‘http://stats.gd.gov.cn/zyhygyzjz/index.html’
there are total 10 pages so I give a ‘endpage’ as parameter to use in the whole class. If 
‘endpage’ is more than 10, it will raise an error.
1.2‘def post_request(self)’ get a webpage by importing the Requests module. 
Moreover, using soup.select() can get the label about industry data which is my 
project need.
1.3‘def get_zip_url(self,k,j)’ is building the url which is needed for ‘def 
get_zip_by_url(self)’. The reason why I build a dictionary is that the discipline of the 
urls seem be difficult to find. Therefore, I need to set ‘k’ and ‘j’ as the parameters to 
build the url.
1.4‘def get_zip_by_url(self)’ is based on the url to download the zip and save the zip 
in the same ‘folder’ as ‘download1_zip.py’.
Attention: why I do not download use the url of ‘def post_request(self)’ is that the 
document in that way is office word, but I want to get excel forms which is easy to 
change to csv.
2. Using GUI look at the csv data. Open the ’skin_data1.py’ and run. It will let you 
click the file path and choose the csv you want to see. Finally, click close, you can 
see the data in the python cell.
Atterntion: ‘skin_data.py’ can also present data, but I try a lot of way cannot build the 
main() to make the program looks more clear.
3. Analysis data
Open ‘finish_whole_city.py’ and you can see a class name ‘Data_analysis’. Input 
the parameter for ‘efg = Data_analysis efg = Data_analysis(2005,'12-09-01.csv').
if you do not know the city is which number. If you do not know parameter k of 
‘def get_zip_url(self,k)’ you can use ’enquire.py’ to look at the relationship
between the number and the city.
3.1’ def __onecity__(self,k)’shows you The Number of Industrial Enterprises in the 
city you choos in a year.
3.2 ‘def overall_picture(self)’show different city development trend by a line graph.
From the line graph, you can know that the city which you want to work there, the 
number of enterprises is more than before or less than before. As we known, the 
number of enterprises can decide a city economic and the number of available job.
3.3’ def city_rank(self)’ output a csv document that in the same folder as 
‘finish_whole_city.py’which show you the increasing order based on the year which 
you choose.
3.4 ‘def a_picture_city(self)’ a bar graph for one city in different ye
Conclusion
There are four part of my project download data, using gui read data, use 
matplotlib.pyplot make tables become diagrams, which is called visualization and do 
some mathematic to deal with data. Through the data analysis, a graduate student can 
be based on their ability to choose the city which they think is best for them. The most 
important thing for me to build graph is to showing the relationship of data.
Limitation and improvement
From the beginning I want to do more data analysis work for this project. The difficult 
part for me is to pass the parameter and deal with the relationship between different 
parameter. And I use a lot of time to put the function together and build a class. I have 
to learn how to use BeautifulSoup to down data and I find that the ‘url’sometimes is 
hard to just use a for loop to create, because the component of ‘url’ is not always 
simple. And some of the character problem lead to the python can not recognize the 
character of csv. If I can connect all these parts and using gui and make a program.
