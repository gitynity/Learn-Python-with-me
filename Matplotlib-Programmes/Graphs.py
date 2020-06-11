import numpy as np
import matplotlib.pyplot as plt				
from matplotlib import style # for style of graph


style.use("ggplot")  #ggplot = grid background in our graph
plt.grid(color = 'c' , linestyle = "-.")  #color of grid lines = "cyan" and linesstyle = dotted lines in grid

days = [1,2,3,4,5,6,7,8,9,10]
temperature = np.random.normal(30,5,10)

plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Daywise Temperature Plot")
plt.plot(days,temperature , color = 'g' , marker = 'o' , linestyle = '--' , linewidth = 3 , markersize = 10)
# OR 
#plt.plot(days,temperature, "o--" , linewidth = 3 , markersize = 10  ) # o-- = " o , dashed" in shortform. No color is explicitly defined by us , so bydefault blue color is selected by matplotlib

plt.show()	#Prints a line graph

#Now lets plot two line graphs in one graph

IndianTemp = np.random.normal(35,10,10)
MPtemp = np.random.normal(30,5,10)

style.use("ggplot")  #ggplot = grid background in our graph
plt.grid(color = 'c' , linestyle = "-.")  #color of grid lines = "cyan" and linesstyle = dotted lines in grid

plt.plot(days,temperature, "o--" , linewidth = 3 , markersize = 10 , label = "MadhyaPradesh"  ) # Instead of giving the label name of graph in plt.legend , we can mention it here also as label = "Temp line" 
plt.plot(days,IndianTemp,"go-",label = "India")

plt.title("Daily Summer Temperatures Madhya Pradesh" , fontsize = 15)
plt.xlabel("Days" , fontsize = 15)
plt.ylabel("Temperature" , fontsize = 15)
plt.legend(loc = 4)  

plt.xticks(list(range(0,10))) # or plt.xticks(np.arange(0,10)) will also do the same : xticks are used to set the values of x axis
plt.yticks(np.arange(0,41,10)) # yticks are used to set the values of y axis

plt.show()

###############################################################

#Lets plot a Histogram

Py_students = np.random.randint(15,50,(100))	#Generate 100 random  values between 15 to 50
ML_students = np.random.randint(18,45,(100))	#Generate 100 random  values between 18 to 45

bins = [15,20,25,30,35,40,45]	#In a histogram, the total range of data set (i.e from minimum value to maximum value) is divided into 8 to 15 equal parts. These equal parts are known as bins or class intervals. Each and every observation (or value) in the data set is placed in the appropriate bin

plt.hist(Py_students , bins , label = "Python")
plt.legend(loc=2)
plt.xlabel("Student's Age")
plt.ylabel("Number of Students")
plt.title("Python Students Age wise Histogram")
plt.show()	#Prints a histogram of python students age wise


################################################################

#Now lets plot two histograms together

plt.hist([Py_students,ML_students] , bins , color = ["b","g"] , label = ["Python" , "ML"])  #passing the graph data in form of lists 
plt.legend(loc=2)	#Position of label
plt.title("Machine Learning & Pyhton students age wise histogram")
plt.xlabel("Student's Age")
plt.ylabel("Number of Students")

plt.show()	#Prints a histogram

###############################################################
