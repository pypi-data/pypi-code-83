'''
Neuron simulator export for:

Components:
    null (Type: notes)
    i_clamp (Type: pulseGenerator:  delay=0.2 (SI time) duration=0.6 (SI time) amplitude=9.9E-10 (SI current))
    testcell (Type: IF_cond_alpha:  e_rev_E=0.0 (dimensionless) e_rev_I=-70.0 (dimensionless) tau_refrac=5.0 (dimensionless) v_thresh=-50.0 (dimensionless) tau_m=20.0 (dimensionless) v_rest=-65.0 (dimensionless) v_reset=-65.0 (dimensionless) cm=1.0 (dimensionless) i_offset=0.1 (dimensionless) tau_syn_E=0.3 (dimensionless) tau_syn_I=0.5 (dimensionless) v_init=-65.0 (dimensionless) MSEC=0.001 (SI time) MVOLT=0.001 (SI voltage) NFARAD=1.0E-9 (SI capacitance))
    testcell2 (Type: IF_cond_alpha:  e_rev_E=-10.0 (dimensionless) e_rev_I=-80.0 (dimensionless) tau_refrac=5.0 (dimensionless) v_thresh=-50.0 (dimensionless) tau_m=20.0 (dimensionless) v_rest=-65.0 (dimensionless) v_reset=-65.0 (dimensionless) cm=1.0 (dimensionless) i_offset=-0.1 (dimensionless) tau_syn_E=2.0 (dimensionless) tau_syn_I=10.0 (dimensionless) v_init=-65.0 (dimensionless) MSEC=0.001 (SI time) MVOLT=0.001 (SI voltage) NFARAD=1.0E-9 (SI capacitance))
    ampaSyn (Type: alphaCondSynapse:  e_rev=-10.0 (dimensionless) tau_syn=2.0 (dimensionless) MSEC=0.001 (SI time) MVOLT=0.001 (SI voltage) NAMP=1.0E-9 (SI current))
    gabaSyn (Type: alphaCondSynapse:  e_rev=-80.0 (dimensionless) tau_syn=10.0 (dimensionless) MSEC=0.001 (SI time) MVOLT=0.001 (SI voltage) NAMP=1.0E-9 (SI current))
    Example4_PyNN (Type: network)
    SimExample4 (Type: Simulation:  length=1.0 (SI time) step=1.0E-5 (SI time))


    This NEURON file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.8.0
         org.neuroml.model   v1.8.0
         jLEMS               v0.10.5

'''

import neuron

import time
import datetime
import sys

import hashlib
h = neuron.h
h.load_file("stdlib.hoc")

h.load_file("stdgui.hoc")

h("objref p")
h("p = new PythonObject()")

class NeuronSimulation():

    def __init__(self, tstop, dt, seed=5678):

        print("\n    Starting simulation in NEURON of %sms generated from NeuroML2 model...\n"%tstop)

        self.setup_start = time.time()
        self.seed = seed
        import socket
        self.report_file = open('report.SimExample4.txt','w')
        print('Simulator version:  %s'%h.nrnversion())
        self.report_file.write('# Report of running simulation with %s\n'%h.nrnversion())
        self.report_file.write('Simulator=NEURON\n')
        self.report_file.write('SimulatorVersion=%s\n'%h.nrnversion())

        self.report_file.write('SimulationFile=%s\n'%__file__)
        self.report_file.write('PythonVersion=%s\n'%sys.version.replace('\n',' '))
        print('Python version:     %s'%sys.version.replace('\n',' '))
        self.report_file.write('NeuroMLExportVersion=1.8.0\n')
        self.report_file.write('SimulationSeed=%s\n'%self.seed)
        self.report_file.write('Hostname=%s\n'%socket.gethostname())
        self.randoms = []
        self.next_global_id = 0  # Used in Random123 classes for elements using random(), etc. 

        self.next_spiking_input_id = 0  # Used in Random123 classes for elements using random(), etc. 

        '''
        Adding simulation Component(id=SimExample4 type=Simulation) of network/component: Example4_PyNN (Type: network)
        
        '''
        # ######################   Population: pop0
        print("Population pop0 contains 2 instance(s) of component: testcell of type: IF_cond_alpha")

        h(" {n_pop0 = 2} ")
        '''
        Population pop0 contains instances of Component(id=testcell type=IF_cond_alpha)
        whose dynamics will be implemented as a mechanism (testcell) in a mod file
        '''
        h(" create pop0[2]")
        h(" objectvar m_testcell_pop0[2] ")

        for i in range(int(h.n_pop0)):
            h.pop0[i].L = 10.0
            h.pop0[i](0.5).diam = 10.0
            h.pop0[i](0.5).cm = 318.3098861837907
            h.pop0[i].push()
            h(" pop0[%i]  { m_testcell_pop0[%i] = new testcell(0.5) } "%(i,i))

            h.m_testcell_pop0[i].e_rev_E = 0.0
            h.m_testcell_pop0[i].e_rev_I = -70.0
            h.m_testcell_pop0[i].tau_refrac = 5.0
            h.m_testcell_pop0[i].v_thresh = -50.0
            h.m_testcell_pop0[i].tau_m = 20.0
            h.m_testcell_pop0[i].v_rest = -65.0
            h.m_testcell_pop0[i].v_reset = -65.0
            h.m_testcell_pop0[i].cm = 1.0
            h.m_testcell_pop0[i].i_offset = 0.1
            h.m_testcell_pop0[i].tau_syn_E = 0.3
            h.m_testcell_pop0[i].tau_syn_I = 0.5
            h.m_testcell_pop0[i].v_init = -65.0
            h.m_testcell_pop0[i].MSEC = 1.0
            h.m_testcell_pop0[i].MVOLT = 1.0
            h.m_testcell_pop0[i].NFARAD = 0.001
            h.pop_section()

            self.next_global_id+=1

        h(" pop0[0] { pt3dclear() } ")
        h(" pop0[0] { pt3dadd(966.45355, 44.07326 + (5), 7.49147, 10) } ")
        h(" pop0[0] { pt3dadd(966.45355, 44.07326 + (-5), 7.49147, 10) } ")
        h(" pop0[1] { pt3dclear() } ")
        h(" pop0[1] { pt3dadd(910.97595, 93.9269 + (5), 582.2276, 10) } ")
        h(" pop0[1] { pt3dadd(910.97595, 93.9269 + (-5), 582.2276, 10) } ")

        # ######################   Population: pop1
        print("Population pop1 contains 2 instance(s) of component: testcell2 of type: IF_cond_alpha")

        h(" {n_pop1 = 2} ")
        '''
        Population pop1 contains instances of Component(id=testcell2 type=IF_cond_alpha)
        whose dynamics will be implemented as a mechanism (testcell2) in a mod file
        '''
        h(" create pop1[2]")
        h(" objectvar m_testcell2_pop1[2] ")

        for i in range(int(h.n_pop1)):
            h.pop1[i].L = 10.0
            h.pop1[i](0.5).diam = 10.0
            h.pop1[i](0.5).cm = 318.3098861837907
            h.pop1[i].push()
            h(" pop1[%i]  { m_testcell2_pop1[%i] = new testcell2(0.5) } "%(i,i))

            h.m_testcell2_pop1[i].e_rev_E = -10.0
            h.m_testcell2_pop1[i].e_rev_I = -80.0
            h.m_testcell2_pop1[i].tau_refrac = 5.0
            h.m_testcell2_pop1[i].v_thresh = -50.0
            h.m_testcell2_pop1[i].tau_m = 20.0
            h.m_testcell2_pop1[i].v_rest = -65.0
            h.m_testcell2_pop1[i].v_reset = -65.0
            h.m_testcell2_pop1[i].cm = 1.0
            h.m_testcell2_pop1[i].i_offset = -0.1
            h.m_testcell2_pop1[i].tau_syn_E = 2.0
            h.m_testcell2_pop1[i].tau_syn_I = 10.0
            h.m_testcell2_pop1[i].v_init = -65.0
            h.m_testcell2_pop1[i].MSEC = 1.0
            h.m_testcell2_pop1[i].MVOLT = 1.0
            h.m_testcell2_pop1[i].NFARAD = 0.001
            h.pop_section()

            self.next_global_id+=1

        h(" pop1[0] { pt3dclear() } ")
        h(" pop1[0] { pt3dadd(671.5635, 8.393823 + (5), 766.48096, 10) } ")
        h(" pop1[0] { pt3dadd(671.5635, 8.393823 + (-5), 766.48096, 10) } ")
        h(" pop1[1] { pt3dclear() } ")
        h(" pop1[1] { pt3dadd(236.80977, 3.081402 + (5), 788.7727, 10) } ")
        h(" pop1[1] { pt3dadd(236.80977, 3.081402 + (-5), 788.7727, 10) } ")

        # ######################   Population: pop2
        print("Population pop2 contains 1 instance(s) of component: testcell2 of type: IF_cond_alpha")

        h(" {n_pop2 = 1} ")
        '''
        Population pop2 contains instances of Component(id=testcell2 type=IF_cond_alpha)
        whose dynamics will be implemented as a mechanism (testcell2) in a mod file
        '''
        h(" create pop2[1]")
        h(" objectvar m_testcell2_pop2[1] ")

        for i in range(int(h.n_pop2)):
            h.pop2[i].L = 10.0
            h.pop2[i](0.5).diam = 10.0
            h.pop2[i](0.5).cm = 318.3098861837907
            h.pop2[i].push()
            h(" pop2[%i]  { m_testcell2_pop2[%i] = new testcell2(0.5) } "%(i,i))

            h.m_testcell2_pop2[i].e_rev_E = -10.0
            h.m_testcell2_pop2[i].e_rev_I = -80.0
            h.m_testcell2_pop2[i].tau_refrac = 5.0
            h.m_testcell2_pop2[i].v_thresh = -50.0
            h.m_testcell2_pop2[i].tau_m = 20.0
            h.m_testcell2_pop2[i].v_rest = -65.0
            h.m_testcell2_pop2[i].v_reset = -65.0
            h.m_testcell2_pop2[i].cm = 1.0
            h.m_testcell2_pop2[i].i_offset = -0.1
            h.m_testcell2_pop2[i].tau_syn_E = 2.0
            h.m_testcell2_pop2[i].tau_syn_I = 10.0
            h.m_testcell2_pop2[i].v_init = -65.0
            h.m_testcell2_pop2[i].MSEC = 1.0
            h.m_testcell2_pop2[i].MVOLT = 1.0
            h.m_testcell2_pop2[i].NFARAD = 0.001
            h.pop_section()

            self.next_global_id+=1

        h(" pop2[0] { pt3dclear() } ")
        h(" pop2[0] { pt3dadd(346.08896, 62.328148 + (5), 615.8157, 10) } ")
        h(" pop2[0] { pt3dadd(346.08896, 62.328148 + (-5), 615.8157, 10) } ")

        # ######################   Projection: proj0
        print("Adding projection: proj0, from pop0 to pop1 with synapse ampaSyn, 4 connection(s)")

        h("objectvar syn_proj0_ampaSyn[4]")

        h("objectvar netConn_proj0_ampaSyn[4]")

        # Connection 0: cell 0, seg 0 (0.5) [0.5 on pop0[0]] -> cell 0, seg 0 (0.5) [0.5 on pop1[0]], weight: 0.02, delay 2.0
        h("pop1[0] syn_proj0_ampaSyn[0] = new ampaSyn(0.5)")
        h("pop0[0] netConn_proj0_ampaSyn[0] = new NetCon(&v(0.5), syn_proj0_ampaSyn[0], -50.0, 2.0, 0.02)")  

        # Connection 1: cell 0, seg 0 (0.5) [0.5 on pop0[0]] -> cell 1, seg 0 (0.5) [0.5 on pop1[1]], weight: 0.02, delay 2.0
        h("pop1[1] syn_proj0_ampaSyn[1] = new ampaSyn(0.5)")
        h("pop0[0] netConn_proj0_ampaSyn[1] = new NetCon(&v(0.5), syn_proj0_ampaSyn[1], -50.0, 2.0, 0.02)")  

        # Connection 2: cell 1, seg 0 (0.5) [0.5 on pop0[1]] -> cell 0, seg 0 (0.5) [0.5 on pop1[0]], weight: 0.02, delay 2.0
        h("pop1[0] syn_proj0_ampaSyn[2] = new ampaSyn(0.5)")
        h("pop0[1] netConn_proj0_ampaSyn[2] = new NetCon(&v(0.5), syn_proj0_ampaSyn[2], -50.0, 2.0, 0.02)")  

        # Connection 3: cell 1, seg 0 (0.5) [0.5 on pop0[1]] -> cell 1, seg 0 (0.5) [0.5 on pop1[1]], weight: 0.02, delay 2.0
        h("pop1[1] syn_proj0_ampaSyn[3] = new ampaSyn(0.5)")
        h("pop0[1] netConn_proj0_ampaSyn[3] = new NetCon(&v(0.5), syn_proj0_ampaSyn[3], -50.0, 2.0, 0.02)")  

        # ######################   Projection: proj1
        print("Adding projection: proj1, from pop0 to pop2 with synapse gabaSyn, 2 connection(s)")

        h("objectvar syn_proj1_gabaSyn[2]")

        h("objectvar netConn_proj1_gabaSyn[2]")

        # Connection 0: cell 0, seg 0 (0.5) [0.5 on pop0[0]] -> cell 0, seg 0 (0.5) [0.5 on pop2[0]], weight: 0.01, delay 2.0
        h("pop2[0] syn_proj1_gabaSyn[0] = new gabaSyn(0.5)")
        h("pop0[0] netConn_proj1_gabaSyn[0] = new NetCon(&v(0.5), syn_proj1_gabaSyn[0], -50.0, 2.0, 0.01)")  

        # Connection 1: cell 1, seg 0 (0.5) [0.5 on pop0[1]] -> cell 0, seg 0 (0.5) [0.5 on pop2[0]], weight: 0.01, delay 2.0
        h("pop2[0] syn_proj1_gabaSyn[1] = new gabaSyn(0.5)")
        h("pop0[1] netConn_proj1_gabaSyn[1] = new NetCon(&v(0.5), syn_proj1_gabaSyn[1], -50.0, 2.0, 0.01)")  

        print("Processing 1 input lists")

        # ######################   Input List: stim
        # Adding single input: Component(id=0 type=input)
        h("objref stim_0")
        h("pop0[0] { stim_0 = new i_clamp(0.5) } ")

        print("Finished processing 1 input lists")

        trec = h.Vector()
        trec.record(h._ref_t)

        h.tstop = tstop

        h.dt = dt

        h.steps_per_ms = 1/h.dt



        # ######################   File to save: SimExample4.pop2.v.dat (SimExample4_pop2_v_dat)
        # Column: pop2/0/testcell2/v
        h(' objectvar v_pop2_0_testcell2_v_SimExample4_pop2_v_dat ')
        h(' { v_pop2_0_testcell2_v_SimExample4_pop2_v_dat = new Vector() } ')
        h(' { v_pop2_0_testcell2_v_SimExample4_pop2_v_dat.record(&pop2[0].v(0.5)) } ')
        h.v_pop2_0_testcell2_v_SimExample4_pop2_v_dat.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: SimExample4.pop0.spikes (SimExample4_pop0_spikes)
        h(' objectvar spiketimes_SimExample4_pop0_spikes, t_spiketimes_SimExample4_pop0_spikes ')
        h(' { spiketimes_SimExample4_pop0_spikes = new Vector() } ')
        h(' { t_spiketimes_SimExample4_pop0_spikes = new Vector() } ')
        h(' objref netConnSpike_SimExample4_pop0_spikes, nil ')
        # Column: pop0/0/testcell (0) pop0[0]
        h(' pop0[0] { netConnSpike_SimExample4_pop0_spikes = new NetCon(&v(0.5), nil, -50.0, 0, 1) } ')
        h(' { netConnSpike_SimExample4_pop0_spikes.record(t_spiketimes_SimExample4_pop0_spikes, spiketimes_SimExample4_pop0_spikes, 0) } ')
        # Column: pop0/1/testcell (1) pop0[1]
        h(' pop0[1] { netConnSpike_SimExample4_pop0_spikes = new NetCon(&v(0.5), nil, -50.0, 0, 1) } ')
        h(' { netConnSpike_SimExample4_pop0_spikes.record(t_spiketimes_SimExample4_pop0_spikes, spiketimes_SimExample4_pop0_spikes, 1) } ')

        # ######################   File to save: time.dat (time)
        # Column: time
        h(' objectvar v_time ')
        h(' { v_time = new Vector() } ')
        h(' { v_time.record(&t) } ')
        h.v_time.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: SimExample4.pop1.v.dat (SimExample4_pop1_v_dat)
        # Column: pop1/0/testcell2/v
        h(' objectvar v_pop1_0_testcell2_v_SimExample4_pop1_v_dat ')
        h(' { v_pop1_0_testcell2_v_SimExample4_pop1_v_dat = new Vector() } ')
        h(' { v_pop1_0_testcell2_v_SimExample4_pop1_v_dat.record(&pop1[0].v(0.5)) } ')
        h.v_pop1_0_testcell2_v_SimExample4_pop1_v_dat.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: pop1/1/testcell2/v
        h(' objectvar v_pop1_1_testcell2_v_SimExample4_pop1_v_dat ')
        h(' { v_pop1_1_testcell2_v_SimExample4_pop1_v_dat = new Vector() } ')
        h(' { v_pop1_1_testcell2_v_SimExample4_pop1_v_dat.record(&pop1[1].v(0.5)) } ')
        h.v_pop1_1_testcell2_v_SimExample4_pop1_v_dat.resize((h.tstop * h.steps_per_ms) + 1)

        # ######################   File to save: SimExample4.pop0.v.dat (SimExample4_pop0_v_dat)
        # Column: pop0/0/testcell/v
        h(' objectvar v_pop0_0_testcell_v_SimExample4_pop0_v_dat ')
        h(' { v_pop0_0_testcell_v_SimExample4_pop0_v_dat = new Vector() } ')
        h(' { v_pop0_0_testcell_v_SimExample4_pop0_v_dat.record(&pop0[0].v(0.5)) } ')
        h.v_pop0_0_testcell_v_SimExample4_pop0_v_dat.resize((h.tstop * h.steps_per_ms) + 1)
        # Column: pop0/1/testcell/v
        h(' objectvar v_pop0_1_testcell_v_SimExample4_pop0_v_dat ')
        h(' { v_pop0_1_testcell_v_SimExample4_pop0_v_dat = new Vector() } ')
        h(' { v_pop0_1_testcell_v_SimExample4_pop0_v_dat.record(&pop0[1].v(0.5)) } ')
        h.v_pop0_1_testcell_v_SimExample4_pop0_v_dat.resize((h.tstop * h.steps_per_ms) + 1)

        self.initialized = False

        self.sim_end = -1 # will be overwritten

        setup_end = time.time()
        self.setup_time = setup_end - self.setup_start
        print("Setting up the network to simulate took %f seconds"%(self.setup_time))

    def run(self):

        self.initialized = True
        sim_start = time.time()
        print("Running a simulation of %sms (dt = %sms; seed=%s)" % (h.tstop, h.dt, self.seed))

        try:
            h.run()
        except Exception as e:
            print("Exception running NEURON: %s" % (e))
            quit()


        self.sim_end = time.time()
        self.sim_time = self.sim_end - sim_start
        print("Finished NEURON simulation in %f seconds (%f mins)..."%(self.sim_time, self.sim_time/60.0))

        try:
            self.save_results()
        except Exception as e:
            print("Exception saving results of NEURON simulation: %s" % (e))
            quit()


    def advance(self):

        if not self.initialized:
            h.finitialize()
            self.initialized = True

        h.fadvance()


    ###############################################################################
    # Hash function to use in generation of random value
    # This is copied from NetPyNE: https://github.com/Neurosim-lab/netpyne/blob/master/netpyne/simFuncs.py
    ###############################################################################
    def _id32 (self,obj): 
        return int(hashlib.md5(obj.encode('utf-8')).hexdigest()[0:8],16)  # convert 8 first chars of md5 hash in base 16 to int


    ###############################################################################
    # Initialize the stim randomizer
    # This is copied from NetPyNE: https://github.com/Neurosim-lab/netpyne/blob/master/netpyne/simFuncs.py
    ###############################################################################
    def _init_stim_randomizer(self,rand, stimType, gid, seed): 
        #print("INIT STIM  %s; %s; %s; %s"%(rand, stimType, gid, seed))
        rand.Random123(self._id32(stimType), gid, seed)


    def save_results(self):

        print("Saving results at t=%s..."%h.t)

        if self.sim_end < 0: self.sim_end = time.time()


        # ######################   File to save: time.dat (time)
        py_v_time = [ t/1000 for t in h.v_time.to_python() ]  # Convert to Python list for speed...

        f_time_f2 = open('time.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_time_f2.write('%f'% py_v_time[i])  # Save in SI units...
        f_time_f2.close()
        print("Saved data to: time.dat")

        # ######################   File to save: SimExample4.pop2.v.dat (SimExample4_pop2_v_dat)
        py_v_pop2_0_testcell2_v_SimExample4_pop2_v_dat = [ float(x  / 1000.0) for x in h.v_pop2_0_testcell2_v_SimExample4_pop2_v_dat.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_SimExample4_pop2_v_dat_f2 = open('SimExample4.pop2.v.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_SimExample4_pop2_v_dat_f2.write('%e\t%e\t\n' % (py_v_time[i], py_v_pop2_0_testcell2_v_SimExample4_pop2_v_dat[i], ))
        f_SimExample4_pop2_v_dat_f2.close()
        print("Saved data to: SimExample4.pop2.v.dat")

        # ######################   File to save: SimExample4.pop0.spikes (SimExample4_pop0_spikes)

        f_SimExample4_pop0_spikes_f2 = open('SimExample4.pop0.spikes', 'w')
        h(' objref netConnSpike_SimExample4_pop0_spikes ')
        spike_ids = h.spiketimes_SimExample4_pop0_spikes.to_python()  
        spike_times = h.t_spiketimes_SimExample4_pop0_spikes.to_python()
        for i, id in enumerate(spike_ids):
            # Saving in format: ID_TIME
            f_SimExample4_pop0_spikes_f2.write("%i\t%s\n"%(id,spike_times[i]/1000.0))
        f_SimExample4_pop0_spikes_f2.close()
        print("Saved data to: SimExample4.pop0.spikes")

        # ######################   File to save: SimExample4.pop1.v.dat (SimExample4_pop1_v_dat)
        py_v_pop1_0_testcell2_v_SimExample4_pop1_v_dat = [ float(x  / 1000.0) for x in h.v_pop1_0_testcell2_v_SimExample4_pop1_v_dat.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_pop1_1_testcell2_v_SimExample4_pop1_v_dat = [ float(x  / 1000.0) for x in h.v_pop1_1_testcell2_v_SimExample4_pop1_v_dat.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_SimExample4_pop1_v_dat_f2 = open('SimExample4.pop1.v.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_SimExample4_pop1_v_dat_f2.write('%e\t%e\t%e\t\n' % (py_v_time[i], py_v_pop1_0_testcell2_v_SimExample4_pop1_v_dat[i], py_v_pop1_1_testcell2_v_SimExample4_pop1_v_dat[i], ))
        f_SimExample4_pop1_v_dat_f2.close()
        print("Saved data to: SimExample4.pop1.v.dat")

        # ######################   File to save: SimExample4.pop0.v.dat (SimExample4_pop0_v_dat)
        py_v_pop0_0_testcell_v_SimExample4_pop0_v_dat = [ float(x  / 1000.0) for x in h.v_pop0_0_testcell_v_SimExample4_pop0_v_dat.to_python() ]  # Convert to Python list for speed, variable has dim: voltage
        py_v_pop0_1_testcell_v_SimExample4_pop0_v_dat = [ float(x  / 1000.0) for x in h.v_pop0_1_testcell_v_SimExample4_pop0_v_dat.to_python() ]  # Convert to Python list for speed, variable has dim: voltage

        f_SimExample4_pop0_v_dat_f2 = open('SimExample4.pop0.v.dat', 'w')
        num_points = len(py_v_time)  # Simulation may have been stopped before tstop...

        for i in range(num_points):
            f_SimExample4_pop0_v_dat_f2.write('%e\t%e\t%e\t\n' % (py_v_time[i], py_v_pop0_0_testcell_v_SimExample4_pop0_v_dat[i], py_v_pop0_1_testcell_v_SimExample4_pop0_v_dat[i], ))
        f_SimExample4_pop0_v_dat_f2.close()
        print("Saved data to: SimExample4.pop0.v.dat")

        save_end = time.time()
        save_time = save_end - self.sim_end
        print("Finished saving results in %f seconds"%(save_time))

        self.report_file.write('StartTime=%s\n'%datetime.datetime.fromtimestamp(self.setup_start).strftime('%Y-%m-%d %H:%M:%S'))
        self.report_file.write('SetupTime=%s\n'%self.setup_time)
        self.report_file.write('RealSimulationTime=%s\n'%self.sim_time)
        self.report_file.write('SimulationSaveTime=%s\n'%save_time)
        self.report_file.close()

        print("Saving report of simulation to %s"%('report.SimExample4.txt'))

        print("Done")

        quit()


if __name__ == '__main__':

    ns = NeuronSimulation(tstop=1000.0, dt=0.01, seed=5678)

    ns.run()

