#!/usr/bin/env python

from kmos.run import KMC_Model
import numpy as np
import matplotlib.pyplot as plt
import itertools
import random

f = open("data_random_simularion5.dat", "a")

with KMC_Model(print_rates=False, banner=False) as model:
  model.parameters.T = 600
  delta_e = 0.1

  E_O_bridge = float(model.parameters.E_O_bridge["value"])
  E_O_cus = float(model.parameters.E_O_cus["value"])
  E_CO_bridge = float(model.parameters.E_CO_bridge["value"])
  E_CO_cus = float(model.parameters.E_CO_cus["value"])
  E_react_Ocus_COcus = float(model.parameters.E_react_Ocus_COcus["value"])
  E_react_Ocus_CObridge = float(model.parameters.E_react_Ocus_CObridge["value"])
  E_react_Obridge_COcus = float(model.parameters.E_react_Obridge_COcus["value"])
  E_react_Obridge_CObridge = float(model.parameters.E_react_Obridge_CObridge["value"])
  
  for iteration in xrange(1,1000000):
    model.parameters.E_O_bridge = random.uniform(E_O_bridge-delta_e, E_O_bridge+ delta_e)
    model.parameters.E_O_cus = random.uniform(E_O_cus-delta_e,E_O_cus+delta_e)
    model.parameters.E_CO_bridge = random.uniform(E_CO_bridge-delta_e,E_CO_bridge+delta_e)
    model.parameters.E_CO_cus = random.uniform(E_CO_cus-delta_e,E_CO_cus+delta_e)
    model.parameters.E_react_Ocus_COcus = random.uniform(E_react_Ocus_COcus-delta_e,E_react_Ocus_COcus+delta_e)
    model.parameters.E_react_Ocus_CObridge = random.uniform(E_react_Ocus_CObridge-delta_e,E_react_Ocus_CObridge+delta_e)
    model.parameters.E_react_Obridge_COcus = random.uniform(E_react_Obridge_COcus-delta_e,E_react_Obridge_COcus+delta_e)
    model.parameters.E_react_Obridge_CObridge = random.uniform(E_react_Obridge_CObridge-delta_e,E_react_Obridge_CObridge+delta_e)
    
    out = model.get_std_sampled_data(1, 5e6, output='dict')
    out = model.get_std_sampled_data(1, 5e6, output='dict')
    tof = out['CO_oxidation']
    f.write("%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\r\n" % (float(model.parameters.E_O_bridge["value"]), float(model.parameters.E_O_cus["value"]), float(model.parameters.E_CO_bridge["value"]), float(model.parameters.E_CO_cus["value"]), float(model.parameters.E_react_Ocus_COcus["value"]), float(model.parameters.E_react_Ocus_CObridge["value"]), float(model.parameters.E_react_Obridge_COcus["value"]), float(model.parameters.E_react_Obridge_CObridge["value"]), tof))

    print("---%f" % (iteration))
f.close()

'''  
  lis = itertools.product(E_O_bridge_interval, E_O_cus_interval, E_CO_bridge_interval, E_CO_cus_interval, E_react_Ocus_COcus_interval, E_react_Ocus_CObridge_interval, E_react_Obridge_COcus_interval, E_react_Obridge_CObridge_interval)
  counter = 0.0
  for it in lis:
    model.parameters.E_O_bridge = it[0]
    model.parameters.E_O_cus = it[1]
    model.parameters.E_CO_bridge = it[2]
    model.parameters.E_CO_cus = it[3]
    model.parameters.E_react_Ocus_COcus = it[4]
    model.parameters.E_react_Ocus_CObridge = it[5]
    model.parameters.E_react_Obridge_COcus = it[6]
    model.parameters.E_react_Obridge_CObridge = it[7]

    out = model.get_std_sampled_data(1, 5e6, output='dict')
    out = model.get_std_sampled_data(1, 5e6, output='dict')
    tof = out['CO_oxidation']
    f.write("%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\r\n" % (float(model.parameters.E_O_bridge["value"]), float(model.parameters.E_O_cus["value"]), float(model.parameters.E_CO_bridge["value"]), float(model.parameters.E_CO_cus["value"]), float(model.parameters.E_react_Ocus_COcus["value"]), float(model.parameters.E_react_Ocus_CObridge["value"]), float(model.parameters.E_react_Obridge_COcus["value"]), float(model.parameters.E_react_Obridge_CObridge["value"]), tof))
    counter = counter + 1.0
    print("---%f" % (counter/states))
f.close()
'''
