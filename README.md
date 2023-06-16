# Touchsenors master package 
Library package for the touchence sensor 

hardware link: http://www.touchence.jp/en/products/cube03.html


![test drawio (31)](https://user-images.githubusercontent.com/47193436/159407992-8b329eaf-29ef-4362-852c-22d51ea92d5b.png)


sensor has 8 detection points.

# Objective:

Library created to modulate the use of the Touchence sensors using python 

inspired by this video: 
(all rights reserved to touchence)

https://www.youtube.com/watch?v=-jpk3o9CFCU&ab_channel=Touchence


# Detailed discription: 
Using this packge the user can easly get sensor feedback by calling the different functions incloded in the libraray.

this library can be used without any knowldge of the commands used by the sensors. 

the sensor uses usb serial communication.

this library contains multiple functions and methods to control and display data from the sensor: 

# Files:

1-  Sensor_data_absorber.py : 


This file contains 2 functions: 

-  Get_Sensor_values_degital(): requests and saves the data from the sensor as it is in values in the range of 0 to 255 


-  Get_Sensor_values_Real(): requests and saves the data from the sensor after it converts them to real values from 0 to 11.6 N



2-  PORT_checker.py : 

This file contains one function


- Port_finder_sensor() :  This function detects active ports used by the sensors. 



3 - Data_display_options.py :


This file  file contains 2 functions or data display options:

- Liniar_display(): Liniar display of the 8 active data points of the sensor displayed like below, 


![sensor4](https://user-images.githubusercontent.com/47193436/159410352-a009306a-4419-4a04-9a4d-673191e587ac.PNG)




-  three_D_display(): 3D visual display of the state of the active 8 points of the sensor dsisplayed like below, 



![sensor3](https://user-images.githubusercontent.com/47193436/159410316-5157fe9f-bef9-406b-b208-9077ed1cd820.PNG)


