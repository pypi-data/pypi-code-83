"""
Unit and regression test for the project package.
"""

# Import package, test suite, and other packages as needed
import project
import pytest
import sys
import simtk.openmm

def test_project_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "project" in sys.modules

def test_openmm_imported():
    """Checks that OpenMM has been imported correctly """
    assert "simtk.openmm" in sys.modules

def test_openmm_simulation():
    """Checks that an OpenMM runs correctly """
    print(project.project.openmm_simulation.__code__
    assert project.project.openmm_simulation() == 10