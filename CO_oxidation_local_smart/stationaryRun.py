#!/usr/bin/env python

from kmos.run import KMC_Model
import numpy as np
import matplotlib.pyplot as plt

with KMC_Model(print_rates=False, banner=False) as model:
  model.parameters.T = 600
  print(model.get_std_header())
  total_steps = 10
  time = np.zeros(total_steps)
  CO_Oxidation = np.zeros(total_steps)
  for iteration in xrange(1, total_steps):
    out = model.get_std_sampled_data(1, 1e6, output='dict')
    print(out['CO_oxidation'], out['simulated_time'])
    CO_Oxidation[iteration] = out['CO_oxidation']
    time[iteration] = out['simulated_time']
  plt.plot(time, CO_Oxidation, '*')
  plt.xlabel('time')
  plt.ylabel('tof')
  plt.show()
