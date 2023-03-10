# Wikipedia about PID: 
# https://en.wikipedia.org/wiki/PID_controller
#

import matplotlib.pyplot as plot
from moku.instruments import PIDController
pid = PIDController('000.000.00', force_connect=True)

try:
    #configures control matrix for channel 1
    pid.set_control_matrix(channel=1, input_gain1=-1, input_gain2=0)
    
    #units are db, hz, hz by default
    pid.set_by_frequency(channel=1, prop_gain=-10, int_crossover=1e2, diff_crossover=1e4)

    #set the probes to monitor output 1
    pid.set_monitor(1, 'Output1')

    # setting the timebase
    pid.set_timebase(-1e-3, 1e-3)

    #trigger point is at 0V
    pid.set_trigger(type='Edge', source='ProbeA', level=0)

    # enable output channel
    pid.enable_output(1, True, True)

    # collecting initial data frames (helpful for setting the axis's)
    data = pid.get_data()
    
    # enables interactive mode for matplot
    plot.ion()

    # enables grids on the plot
    plot.grid(visible=True)

    # setting the y axis limit
    plot.ylim((-1, 1))

    # sets the x axis time, which is the range from the very last point of time to the very first point of time
    plot.xlim([data['time'][0], data['time'][-1]])

    # initial data plot
    output_plot = plot.plot(data['time'], data['ch1'])

    # continuously updates the data on plot
    while True:
        # get new data
        data = pid.get_data()

        # updates the plot
        output_plot.set_xdata(data['time'])
        output_plot.set_ydata(data['ch1'])
        
        # delay
        plot.pause(0.001)

except Exception as e:
    print(f'Exception occurred: {e}')

finally:
    pid.relinquish_ownership()
 
