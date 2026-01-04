The LinReg Library is written in C++. In contains 2 functions that calculate the slope and y intercepts of a line of fit for a set of points.
Math equation for linear regression:
Y = a + bx

a = [ (Σy)(Σx²) − (Σx)(Σxy) ] / [ n(Σx²) − (Σx)² ]

b = [ n(Σxy) − (Σx)(Σy) ] / [ n(Σx²) − (Σx)² ]

Symbol Definitions
- Y is the predicted value
- x is the independent variable
- a is the y-intercept
- b is the slope of the line

- Σx  = sum of all x-values  
- Σy  = sum of all y-values  
- Σx² = sum of x-values squared  
- Σxy = sum of the product of x and y  
- n   = number of data points

The python file uses the C++ library functions to take in the X and Y values, and call the functions to make an accurate prediction. In addition, it uses the MatPlotLib library to make a coordinate 
plane, to graph the points and draw the line of best fit.
