model_name = 'CO_oxidation_Ruo2'
simulation_size = 20
random_seed = 1

def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    #from setup_model import setup_model
    #setup_model(model)
    pass

# Default history length in graph
hist_length = 30

parameters = {
    "A":{"value":"20.0616*angstrom**2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_CO_bridge":{"value":"-1.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_CO_cus":{"value":"-1.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_bridge_bridge":{"value":"0.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_bridge_cus":{"value":"1.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_cus_bridge":{"value":"1.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_COdiff_cus_cus":{"value":"1.7", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_O_bridge":{"value":"-2.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_O_cus":{"value":"-1.0", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_bridge_bridge":{"value":"0.7", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_bridge_cus":{"value":"2.3", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_cus_bridge":{"value":"1.0", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_Odiff_cus_cus":{"value":"1.6", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Obridge_CObridge":{"value":"1.5", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Obridge_COcus":{"value":"0.8", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Ocus_CObridge":{"value":"1.2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_react_Ocus_COcus":{"value":"0.9", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"450", "adjustable":True, "min":"300.0", "max":"1500.0","scale":"linear"},
    "p_COgas":{"value":"1", "adjustable":True, "min":"1e-13", "max":"100.0","scale":"log"},
    "p_O2gas":{"value":"1", "adjustable":True, "min":"1e-13", "max":"100.0","scale":"log"},
    }

rate_constants = {
    "CO_adsorption_bridge":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)", True),
    "CO_adsorption_cus":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)", True),
    "CO_desorption_bridge":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_bridge-mu_COgas)*eV)", True),
    "CO_desorption_cus":("p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_cus-mu_COgas)*eV)", True),
    "COdiff_bridge_down":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)", True),
    "COdiff_bridge_left":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)", True),
    "COdiff_bridge_right":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)", True),
    "COdiff_bridge_up":("(beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)", True),
    "COdiff_cus_down":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)", True),
    "COdiff_cus_left":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)", True),
    "COdiff_cus_right":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)", True),
    "COdiff_cus_up":("(beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)", True),
    "O2_adsorption_bridge_right":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_adsorption_bridge_up":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_adsorption_cus_right":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_adsorption_cus_up":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)", True),
    "O2_desorption_bridge_right":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_bridge+E_O_cus)-mu_O2gas)*eV)", True),
    "O2_desorption_bridge_up":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_bridge-mu_O2gas)*eV)", True),
    "O2_desorption_cus_right":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_cus+E_O_bridge)-mu_O2gas)*eV)", True),
    "O2_desorption_cus_up":("p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_cus-mu_O2gas)*eV)", True),
    "Odiff_bridge_down":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)", True),
    "Odiff_bridge_left":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)", True),
    "Odiff_bridge_right":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)", True),
    "Odiff_bridge_up":("(beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)", True),
    "Odiff_cus_down":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)", True),
    "Odiff_cus_left":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)", True),
    "Odiff_cus_right":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)", True),
    "Odiff_cus_up":("(beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)", True),
    "React_bridge_down":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)", True),
    "React_bridge_left":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)", True),
    "React_bridge_right":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)", True),
    "React_bridge_up":("(beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)", True),
    "React_cus_down":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)", True),
    "React_cus_left":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)", True),
    "React_cus_right":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)", True),
    "React_cus_up":("(beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)", True),
    }

site_names = ['ruo2_bridge', 'ruo2_cus']
representations = {
    "CO":"""Atoms('CO',[[0,0,0],[0,0,1.2]])""",
    "O":"""Atoms('O')""",
    "empty":"""""",
    }

lattice_representation = """[Atoms(symbols='O2Ru2',
          pbc=np.array([False, False, False], dtype=bool),
          cell=np.array(
      [[  6.39 ,   0.   ,   0.   ],
       [  0.   ,   3.116,   0.   ],
       [  0.   ,   0.   ,  20.   ]]),
          scaled_positions=np.array(
      [[0.6942067, 0.0, 0.6390143], [0.3058159, 0.0, 0.6390143], [0.0, 0.0, 0.6390143], [0.5000113, 0.5000789, 0.6390143]]),
),]"""

species_tags = {
    "CO":"""""",
    "O":"""""",
    "empty":"""""",
    }

tof_count = {
    "React_bridge_down":{'CO_oxidation': 1},
    "React_bridge_left":{'CO_oxidation': 1},
    "React_bridge_right":{'CO_oxidation': 1},
    "React_bridge_up":{'CO_oxidation': 1},
    "React_cus_down":{'CO_oxidation': 1},
    "React_cus_left":{'CO_oxidation': 1},
    "React_cus_right":{'CO_oxidation': 1},
    "React_cus_up":{'CO_oxidation': 1},
    }

xml = """[Meta]
author = Max J. Hoffmann
email = mjhoffmann@gmail.com
model_name = CO_oxidation_Ruo2
model_dimension = 2
debug = 0

[SpeciesList]
default_species = empty

[Species CO]
representation = Atoms('CO',[[0,0,0],[0,0,1.2]])
color = #000000
tags = 

[Species O]
representation = Atoms('O')
color = #ff0000
tags = 

[Species empty]
representation = 
color = #ffffff
tags = 

[Parameter A]
value = 20.0616*angstrom**2
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_CO_bridge]
value = -1.6
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_CO_cus]
value = -1.3
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_COdiff_bridge_bridge]
value = 0.6
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_COdiff_bridge_cus]
value = 1.6
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_COdiff_cus_bridge]
value = 1.3
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_COdiff_cus_cus]
value = 1.7
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_O_bridge]
value = -2.3
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_O_cus]
value = -1.0
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_Odiff_bridge_bridge]
value = 0.7
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_Odiff_bridge_cus]
value = 2.3
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_Odiff_cus_bridge]
value = 1.0
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_Odiff_cus_cus]
value = 1.6
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_react_Obridge_CObridge]
value = 1.5
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_react_Obridge_COcus]
value = 0.8
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_react_Ocus_CObridge]
value = 1.2
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter E_react_Ocus_COcus]
value = 0.9
adjustable = False
min = 0.0
max = 0.0
scale = linear

[Parameter T]
value = 450
adjustable = True
min = 300.0
max = 1500.0
scale = linear

[Parameter p_COgas]
value = 1
adjustable = True
min = 1e-13
max = 100.0
scale = log

[Parameter p_O2gas]
value = 1
adjustable = True
min = 1e-13
max = 100.0
scale = log

[Lattice]
cell_size = 6.39 0.0 0.0 0.0 3.116 0.0 0.0 0.0 20.0
default_layer = ruo2
substrate_layer = ruo2
representation = [Atoms(symbols='O2Ru2',
	          pbc=np.array([False, False, False], dtype=bool),
	          cell=np.array(
	      [[  6.39 ,   0.   ,   0.   ],
	       [  0.   ,   3.116,   0.   ],
	       [  0.   ,   0.   ,  20.   ]]),
	          scaled_positions=np.array(
	      [[0.6942067, 0.0, 0.6390143], [0.3058159, 0.0, 0.6390143], [0.0, 0.0, 0.6390143], [0.5000113, 0.5000789, 0.6390143]]),
	),]

[Layer ruo2]
color = #ffffff
site bridge = (0.0, 0.5, 0.69999999999999996); default_species; 
site cus = (0.5, 0.5, 0.69999999999999996); default_species; 

[Process CO_adsorption_bridge]
rate_constant = p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)
otf_rate = None
enabled = True
conditions = empty@bridge
actions = CO@bridge

[Process CO_adsorption_cus]
rate_constant = p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)
otf_rate = None
enabled = True
conditions = empty@cus
actions = CO@cus

[Process CO_desorption_bridge]
rate_constant = p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_bridge-mu_COgas)*eV)
otf_rate = None
enabled = True
conditions = CO@bridge
actions = empty@bridge

[Process CO_desorption_cus]
rate_constant = p_COgas*bar*A/2/sqrt(2*pi*umass*m_CO/beta)*exp(beta*(E_CO_cus-mu_COgas)*eV)
otf_rate = None
enabled = True
conditions = CO@cus
actions = empty@cus

[Process COdiff_bridge_down]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)
otf_rate = None
enabled = True
conditions = CO@bridge + empty@bridge.(0, -1, 0)
actions = empty@bridge + CO@bridge.(0, -1, 0)

[Process COdiff_bridge_left]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)
otf_rate = None
enabled = True
conditions = CO@bridge + empty@cus.(-1, 0, 0)
actions = empty@bridge + CO@cus.(-1, 0, 0)

[Process COdiff_bridge_right]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_cus)*eV)
otf_rate = None
enabled = True
conditions = CO@bridge + empty@cus
actions = empty@bridge + CO@cus

[Process COdiff_bridge_up]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_bridge_bridge)*eV)
otf_rate = None
enabled = True
conditions = CO@bridge + empty@bridge.(0, 1, 0)
actions = empty@bridge + CO@bridge.(0, 1, 0)

[Process COdiff_cus_down]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)
otf_rate = None
enabled = True
conditions = CO@cus + empty@cus.(0, -1, 0)
actions = empty@cus + CO@cus.(0, -1, 0)

[Process COdiff_cus_left]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)
otf_rate = None
enabled = True
conditions = CO@cus + empty@bridge
actions = empty@cus + CO@bridge

[Process COdiff_cus_right]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_cus_bridge)*eV)
otf_rate = None
enabled = True
conditions = CO@cus + empty@bridge.(1, 0, 0)
actions = empty@cus + CO@bridge.(1, 0, 0)

[Process COdiff_cus_up]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_COdiff_cus_cus)*eV)
otf_rate = None
enabled = True
conditions = CO@cus + empty@cus.(0, 1, 0)
actions = empty@cus + CO@cus.(0, 1, 0)

[Process O2_adsorption_bridge_right]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)
otf_rate = None
enabled = True
conditions = empty@bridge + empty@cus
actions = O@bridge + O@cus

[Process O2_adsorption_bridge_up]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)
otf_rate = None
enabled = True
conditions = empty@bridge + empty@bridge.(0, 1, 0)
actions = O@bridge + O@bridge.(0, 1, 0)

[Process O2_adsorption_cus_right]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)
otf_rate = None
enabled = True
conditions = empty@cus + empty@bridge.(1, 0, 0)
actions = O@cus + O@bridge.(1, 0, 0)

[Process O2_adsorption_cus_up]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)
otf_rate = None
enabled = True
conditions = empty@cus + empty@cus.(0, 1, 0)
actions = O@cus + O@cus.(0, 1, 0)

[Process O2_desorption_bridge_right]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_bridge+E_O_cus)-mu_O2gas)*eV)
otf_rate = None
enabled = True
conditions = O@bridge + O@cus
actions = empty@bridge + empty@cus

[Process O2_desorption_bridge_up]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_bridge-mu_O2gas)*eV)
otf_rate = None
enabled = True
conditions = O@bridge + O@bridge.(0, 1, 0)
actions = empty@bridge + empty@bridge.(0, 1, 0)

[Process O2_desorption_cus_right]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*((E_O_cus+E_O_bridge)-mu_O2gas)*eV)
otf_rate = None
enabled = True
conditions = O@cus + O@bridge.(1, 0, 0)
actions = empty@cus + empty@bridge.(1, 0, 0)

[Process O2_desorption_cus_up]
rate_constant = p_O2gas*bar*A/sqrt(2*pi*umass*m_O2/beta)*exp(beta*(2*E_O_cus-mu_O2gas)*eV)
otf_rate = None
enabled = True
conditions = O@cus + O@cus.(0, 1, 0)
actions = empty@cus + empty@cus.(0, 1, 0)

[Process Odiff_bridge_down]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)
otf_rate = None
enabled = True
conditions = O@bridge + empty@bridge.(0, -1, 0)
actions = empty@bridge + O@bridge.(0, -1, 0)

[Process Odiff_bridge_left]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)
otf_rate = None
enabled = True
conditions = O@bridge + empty@cus.(-1, 0, 0)
actions = empty@bridge + O@cus.(-1, 0, 0)

[Process Odiff_bridge_right]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_cus)*eV)
otf_rate = None
enabled = True
conditions = O@bridge + empty@cus
actions = empty@bridge + O@cus

[Process Odiff_bridge_up]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_bridge_bridge)*eV)
otf_rate = None
enabled = True
conditions = O@bridge + empty@bridge.(0, 1, 0)
actions = empty@bridge + O@bridge.(0, 1, 0)

[Process Odiff_cus_down]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)
otf_rate = None
enabled = True
conditions = O@cus + empty@cus.(0, -1, 0)
actions = empty@cus + O@cus.(0, -1, 0)

[Process Odiff_cus_left]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)
otf_rate = None
enabled = True
conditions = O@cus + empty@bridge
actions = empty@cus + O@bridge

[Process Odiff_cus_right]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_cus_bridge)*eV)
otf_rate = None
enabled = True
conditions = O@cus + empty@bridge.(1, 0, 0)
actions = empty@cus + O@bridge.(1, 0, 0)

[Process Odiff_cus_up]
rate_constant = (beta*h)**(-1)*exp(-beta*(E_Odiff_cus_cus)*eV)
otf_rate = None
enabled = True
conditions = O@cus + empty@cus.(0, 1, 0)
actions = empty@cus + O@cus.(0, 1, 0)

[Process React_bridge_down]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@bridge + CO@bridge.(0, -1, 0)
actions = empty@bridge + empty@bridge.(0, -1, 0)

[Process React_bridge_left]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@bridge + CO@cus.(-1, 0, 0)
actions = empty@bridge + empty@cus.(-1, 0, 0)

[Process React_bridge_right]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Obridge_COcus*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@bridge + CO@cus
actions = empty@bridge + empty@cus

[Process React_bridge_up]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Obridge_CObridge*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@bridge + CO@bridge.(0, 1, 0)
actions = empty@bridge + empty@bridge.(0, 1, 0)

[Process React_cus_down]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@cus + CO@cus.(0, -1, 0)
actions = empty@cus + empty@cus.(0, -1, 0)

[Process React_cus_left]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@cus + CO@bridge
actions = empty@cus + empty@bridge

[Process React_cus_right]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Ocus_CObridge*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@cus + CO@bridge.(1, 0, 0)
actions = empty@cus + empty@bridge.(1, 0, 0)

[Process React_cus_up]
rate_constant = (beta*h)**(-1)*exp(-beta*E_react_Ocus_COcus*eV)
otf_rate = None
enabled = True
tof_count = {'CO_oxidation': 1}
conditions = O@cus + CO@cus.(0, 1, 0)
actions = empty@cus + empty@cus.(0, 1, 0)

"""
