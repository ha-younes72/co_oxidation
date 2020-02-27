#!/usr/bin/env python

from kmos.run import KMC_Model
import numpy as np
import matplotlib.pyplot as plt
import itertools

f = open("data.dat", "a")

states = 50**8

with KMC_Model(print_rates=False, banner=False) as model:
  model.parameters.T = 600
  interval = 50
  E_O_bridge = float(model.parameters.E_O_bridge["value"])
  E_O_bridge_interval = np.linspace(0.9*E_O_bridge,1.1*E_O_bridge, interval)
  E_O_cus = float(model.parameters.E_O_cus["value"])
  E_O_cus_interval = np.linspace(0.9*E_O_cus,1.1*E_O_cus, interval)
  E_CO_bridge = float(model.parameters.E_CO_bridge["value"])
  E_CO_bridge_interval = np.linspace(0.9*E_CO_bridge,1.1*E_CO_bridge, interval)
  E_CO_cus = float(model.parameters.E_CO_cus["value"])
  E_CO_cus_interval = np.linspace(0.9*E_CO_cus,1.1*E_CO_cus, interval)
  E_react_Ocus_COcus = float(model.parameters.E_react_Ocus_COcus["value"])
  E_react_Ocus_COcus_interval = np.linspace(0.9*E_react_Ocus_COcus,1.1*E_react_Ocus_COcus, interval)
  E_react_Ocus_CObridge = float(model.parameters.E_react_Ocus_CObridge["value"])
  E_react_Ocus_CObridge_interval = np.linspace(0.9*E_react_Ocus_CObridge,1.1*E_react_Ocus_CObridge, interval)
  E_react_Obridge_COcus = float(model.parameters.E_react_Obridge_COcus["value"])
  E_react_Obridge_COcus_interval = np.linspace(0.9*E_react_Obridge_COcus,1.1*E_react_Obridge_COcus, interval)
  E_react_Obridge_CObridge = float(model.parameters.E_react_Obridge_CObridge["value"])
  E_react_Obridge_CObridge_interval = np.linspace(0.9*E_react_Obridge_CObridge,1.1*E_react_Obridge_CObridge, interval)

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



  