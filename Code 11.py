
# Checking working directory
import os 
import pandas as pd 

current_directory = os.getcwd()
print(current_directory)


#change working directory
new_directory_path = r'C:\Users\Isaac\OneDrive\Desktop\USF\Fall 23\Python'
os.chdir(new_directory_path)


updated_dir = os.getcwd()
print(updated_dir)


file_path = 'Week13Assignment.txt'

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"file '{file_path}' not foung.")
except IOError:
    print("An error occurred while reading the file. ")




#Average Age of Patients 
df = pd.read_csv(file_path)

print(df)

print(df.columns)



#Average Age
average_age = df[' Age'].mean()
print(average_age)



#Number of Male and Female Patients 
male = (df[" Gender"] == ' Male').sum()
female = (df[" Gender"]== ' Female').sum()
print(f"The number of male patients is: {male}. The number of female patients is {female}.")



#Highest Blood Pressure 
max_bp = max(df[" BloodPressure"])
print(f"The highest Blood Pressure is: {max_bp}.")


#Lowest Blood Pressure 
min_bp = min(df[" BloodPressure"])
print(f"The Lowestr Blood Pressure is {min_bp}.")


#Average Body Temperature of Patients
av_temp = df[" Temperature"].mean()
print(f"The average temperature of the patients is: {av_temp} degrees Celcius.")




