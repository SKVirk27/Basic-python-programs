#Assignment3

#Program1->Takes in string from user input and prints if the string is a palindrome or not.

def Palindrome(x):
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(x))
    # Checking if both string are
    # equal or not
    if (x == rev):
        print("Palindrome!!!!!")
    else:
        print("not a palindrome")

# main function1
String=input("Please enter the Palindrome sequence:")
String=String.upper()
print(Palindrome(String))

#Program2-> Takes in a number from user input and prints if the number is a prime number or not.
def Prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                print("It is not a prime number")
                break
        else:
            print("It is a prime number")

    else:
        print("It is not a prime number")
#main function
Number=int(input("Please enter the number:"))
print(Prime(Number))

#Program3-> created a 3X3 matrix of random numbers using NumPy ,
# prints the max value from the above matrix and
# Normalizes the matrix.

import numpy as np
def Normalization(data):
    data_norm = (data - data.min()) / (data.max() - data.min())
    return data_norm
#main function
matrix = np.random.randint(20, size=(3, 3))
print("****The 3*3 matrix****\n",matrix)
print("The maximum value of matrix is\n",matrix.max())
print("Normalized matrix",Normalization(matrix))

#Program4 ->Reads the 'file1.txt' and ‘file2.txt’ in two pandas dataframes,
# and merges both the file and
# also calculates mean for each gene row and sample column.
#generates figure with two box plot(showing distribution of each sample.)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Read the file1.txt and file2.txt
dataframe1=pd.read_csv("file1.txt", delimiter='\t')
dataframe2=pd.read_csv("file2.txt",delimiter='\t')

#Merging two dataframes
New_dataframe=pd.merge(dataframe1,dataframe2,on='Gene_name')
print(New_dataframe)
#Mean of each row and column(sample1, sample2)
New_dataframe.loc['Mean']=New_dataframe.mean(numeric_only=True)
New_dataframe['Mean']=New_dataframe.mean(numeric_only=True, axis=1)
print(New_dataframe)
#Saving merging file as sample_file.csv)
New_dataframe.to_csv('sample_file.csv')
#drop  Mean column
df=New_dataframe.drop('Mean',axis=1)
#Box plot of Sample1 and Sample2
Boxplot=df.plot.box(showfliers=False)
plt.show()











