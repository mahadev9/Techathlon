# Techathlon

Problem statement: Pothole detection using LIDAR values 

Proposed solution:

We took every value from the coloumn x in the Flight02_pointcloud and flight03_pointcloud, for a particular timestamp and added it to an array.
We created an 2D array of timestamps and its repective x values from lidar.
These values were then compared with the next x value(consecutive x value), and if the difference between thme was very high(comparing to a certian threshold), we predicted that the road was uneven at that position.

With the x value threshold, we also took the intensity values from the Flight02_pointcloud.csv and flight03_pointcloud.csv.
We then calculated the average value of all the intensities and used it as another threshold.
If the value of intensity for a particular corresponding x value was greater than the mean intensity, then it is considered as a road with more mud, or worn out road and if the corresponding intensity of a particular value of x is less than the value of mean intensity, then it is considered as flat, good road.

We count the number of potholes or what we may say- 'a bad road'.

The timestamp values are then stored in an array and then this timestamp values are compared with the values in the flght03_gps and flight02_gps, and the corresponding longitude and latitude values will be send and plotted on the map.

This approach can be improved by using the flight02_imu and flight03_imu, which contains the accelaration values of the drone.


Apart from this , we used computer vision techniques to identify the road and the part of the road which needs repair.
We used thresholding and canny edge dectection algorithm. This was done without any of the LIDAR data.




![Image description](https://github.com/mahadev9/Techathlon/blob/master/output_flight02/potholes_detect_flight02.png)
