import numpy as np
salary = np.random.normal(15000,1000,500)	#This salary is a numpy array with gaussian (or normal) distribution
import matplotlib.pyplot as plt				#The mean is about 15000 , standard deviation is about 1000 , and number of people(or samples) is 500

plt.xlabel("Employees")
plt.ylabel("Salary")
plt.title("Employee-Salary Plot")
plt.plot(list(range(1,501)),salary , marker = 'o')
plt.show()	#Prints a line graph

###############################################################

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
