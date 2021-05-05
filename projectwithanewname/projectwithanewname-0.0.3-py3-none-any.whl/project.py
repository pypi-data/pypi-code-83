"""
project.py
A short description of the project.

Handles the primary functions
"""
import simtk.openmm.app
from simtk.unit import *
from sys import stdout

def openmm_simulation():
    pdb = simtk.openmm.app.PDBFile('data/input.pdb')
    forcefield = simtk.openmm.app.ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
    system = forcefield.createSystem(pdb.topology, nonbondedMethod=simtk.openmm.app.PME,
                                     nonbondedCutoff=1 * nanometer, constraints=simtk.openmm.app.HBonds)
    integrator = simtk.openmm.LangevinIntegrator(300 * kelvin, 1 / picosecond, 0.004 * picoseconds)
    simulation = simtk.openmm.app.Simulation(pdb.topology, system, integrator)
    simulation.context.setPositions(pdb.positions)
    simulation.reporters.append(simtk.openmm.app.PDBReporter('output.pdb', 1000))
    simulation.reporters.append(simtk.openmm.app.StateDataReporter(stdout, 1000, step=True,
                                                                   potentialEnergy=True, temperature=True))
    simulation.step(10)
    return simulation.currentStep

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    #print(canvas())
    print(openmm_simulation())
