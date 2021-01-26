# *LombScargle Periodogram of 51 Pegasi B*

Using the Scipy package in Python, the Lombscargle Periodogram for *51 Peggasi B* can be obtained.  
Velocity and corresponding sample times are available as *velocity.txt* and *time.txt* respectively.    
*scipy.signal.lombscargle(x ,y ,w)* takes three array-like arguments which are x, y and angular frequency for the output periodogram.  
The Period of *51 Pegasi b* as per google is 4.2 days, which corresponds to an angular frequency of ~1.48 radians/day.  
Therefore, the third argument should enclose the value = 1.48  

## *Angular_frequency =  numpy.linspace(0.1, 10, 10000)*  
0.1 to avoid ZeroDivisionError and 2 will suffice but 10 to provide a more cleaner look for the periodogram, and 10000 sampling points evenly in between 0.1 and 10.  
It is important that your *Angular_frequency* dataset should cover the true value of the star.  
# # Edit: In addition to the scipy version, I have uploaded the code for the same using the astropy module.
