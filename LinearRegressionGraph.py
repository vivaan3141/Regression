import ctypes
import matplotlib.pyplot as plt


lib = ctypes.CDLL(
    "/Users/vivaananika/CLionProjects/linreg.cpp/liblinreg.dylib"
)

lib.slope.argtypes = (
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
)
lib.slope.restype = ctypes.c_double

lib.yInt.argtypes = (
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
)
lib.yInt.restype = ctypes.c_double

n = int(input("How many data points? \n"))

XArray = ctypes.c_double * n
YArray = ctypes.c_double * n

x = XArray()
y = YArray()

for i in range(n):
    x[i] = float(input(f"X value {i + 1}\n"))
    y[i] = float(input(f"Y value {i + 1}\n"))

plt.scatter(x, y)
m = lib.slope(x, y, n)
b = lib.yInt(x, y, n)

print("Slope =", m)
print("Y int =", b)

xPred = float(input("X value for prediction:\n"))
print((xPred * m) + b)
yAc = float(input("*Optional* Actual Y Value (Copy predicted value in enter it to view graph if you want to skip):\n"))


plt.scatter(xPred, yAc, color='green', label="Actual value")
plt.scatter(xPred, (xPred * m) + b,color='red', label="Predicted Value")



x1=min(x)/1.5
y1=(x1*m)+b
x2=max(x)*1.5
y2=(x2*m)+b
plt.plot([x1, x2], [y1, y2])

st=""
if (m==1):
    if (b==0):
        st="REGRESSION ANALYSIS - Equation: y = x"

    else:
        st="REGRESSION ANALYSIS - Equation: y = x +"+str(b)
    
elif (m==0):
    if (b==0):
        st="REGRESSION ANALYSIS - Equation: y = 0"

    else:
        st="REGRESSION ANALYSIS - Equation: y = "+str(b)
else:
    if (b==0):
        st="REGRESSION ANALYSIS - Equation: y = x"

    else:
        st="REGRESSION ANALYSIS - Equation: y = "+str(m)+" x + "+str(b)
    

plt.xlabel('X')
plt.ylabel('Y')
plt.title(st)
plt.grid(True)
plt.legend()


plt.show()
