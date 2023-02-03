# Wikipedia about PID: 
# https://en.wikipedia.org/wiki/PID_controller
#

import time
import matplotlib.pyplot as plot

#base PI controller
def PI(kP, kI, SP):
    #MV is the measured variable
    MV = 0
    proportional = 0
    integral = 0
    while True:
        #SP is the setpoint, below is the calculation of error
        error = SP - MV
        #proportional error
        proportional = kP * error
        #integral error, essentially is a riemann sum of previous integrals
        integral = integral + kI * error
        #UT is the control variable, is the summation of P and I
        UT = proportional + integral
        #the new measured variale is taking the current measured variable and adding it with the control variable
        MV = UT + MV
        print(MV)
        time.sleep(0.5)

#PI controller with matplot for visualization :D
def plotPI(kP, kI, SP):
    MV = 0
    proportional = 0
    integral = 0
    values = []
    #creates 100 instances of data
    for i in range(100):
        error = SP - MV
        proportional = kP * error
        integral = integral + kI * error
        UT = proportional + integral
        MV = UT + MV
        values.append(MV)
    plot.plot(values)
    plot.show()

plotPI(0.1, 0.1, 10)




