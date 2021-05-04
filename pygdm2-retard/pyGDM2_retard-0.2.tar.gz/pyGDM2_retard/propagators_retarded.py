# encoding: utf-8
#
#Copyright (C) 2017-2021, P. R. Wiecha
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
python interface to 3-layer retarded Green's Dyads fortran implementation
Fortran code by Gerard Colas des Francs
"""
import time
import warnings

import numpy as np
import numba
import multiprocessing

from pyGDM2.propagators import _G0
from pyGDM2.propagators import Gs_EE_asymptotic
from pyGDM2.propagators import _G0_HE
# from pyGDM2.propagators import greens_tensor_evaluation as greens_tensor_evaluation_G0

from pyGDM2_retard.pyGDM2_retard_for import propag11 as g11_retard_for
from pyGDM2_retard.pyGDM2_retard_for import propag21 as g21_retard_for
from pyGDM2_retard.pyGDM2_retard_for import propag13 as g13_retard_for



# =============================================================================
# 3D free space Green's tensors
# =============================================================================
@numba.njit
def G0_EE(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    """
    R1: dipole position
    R2: evaluation position
    """
    if R2[2] <= 0:
        eps_env = eps1
    elif spacing >= R2[2] > 0:
        eps_env = eps2
    elif R2[2] > spacing:
        eps_env = eps3
    
    xx, yy, zz, xy, xz, yx, yz, zx, zy = _G0(R1, R2, wavelength, eps_env)
    S0 = np.array([
        [xx, xy, xz],
        [yx, yy, yz],
        [zx, zy, zz],
        ]).astype(np.complex64)
    
    return S0


@numba.njit
def G0_HE(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    """
    R1: dipole position
    R2: evaluation position
    """
    if R2[2] <= 0:
        eps_env = eps1
    elif spacing >= R2[2] > 0:
        eps_env = eps2
    elif R2[2] > spacing:
        eps_env = eps3
    
    xx, yy, zz, xy, xz, yx, yz, zx, zy = _G0_HE(R1, R2, wavelength, eps_env)
    S0 = np.array([
        [xx, xy, xz],
        [yx, yy, yz],
        [zx, zy, zz],
        ]).astype(np.complex64)
    
    return S0


@numba.njit
def G0_EE_ff(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    """
    R1: dipole position
    R2: evaluation position
    """
    xx, yy, zz, xy, xz, yx, yz, zx, zy = Gs_EE_asymptotic(R1, R2, wavelength, eps1, eps2, eps3, spacing)
    S0_ff = np.array([
        [xx, xy, xz],
        [yx, yy, yz],
        [zx, zy, zz],
        ]).astype(np.complex64)
    
    return S0_ff



### --- fortran retarded 3D
# =============================================================================
# retarded 3-layer Green's tensor, 3D - electric-electric
# =============================================================================
def Gs123_EE_retard_for_rho_phi(rho, phi, zobs, z0, wavelength, eps1, eps2, eps3, spacing):
    Dx = rho*np.cos(phi)
    Dy = rho*np.sin(phi)
    
    R1 = np.array([0, 0, z0])
    R2 = np.array([Dx,Dy,zobs])
    
    return Gs123_EE_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing)


def Gs123_EE_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    """
    R1: dipole position
    R2: evaluation position
    """
    d_min = 0.1   # minimum 2 point distance
    ak0 = 2*np.pi / wavelength
    
    Dx = R2[0] - R1[0]
    Dy = R2[1] - R1[1]
    Z1 = R1[2]
    Z2 = R2[2]
    
    ## in original implementation, the interface is at z=0.
    ## for consistency with pyGDM, shift evaluation such that interface is at z=spacing
    ## (subtract 2x because light makes a roundtrip)
    Z1 = Z1 - spacing
    Z2 = Z2 - spacing
    
    ## avoid positions exactly at boundary
    if np.round(Z1, 2) == 0:
        Z1 += d_min
    if np.round(Z1, 2) == -spacing:
        Z1 += d_min
    if np.round(Z2, 2) == 0:
        Z2 += d_min
    if np.round(Z2, 2) == -spacing:
        Z2 += d_min
    
    # print (Z1, Z2)
    ## fortran retarded: substrate-layer-top --> 3-2-1 (pyGDM: 1-2-3)
    ## after transformation interfaces are now at: 1/2 at z=-spacing, 2/3 at z=0
    ## dipole and evaluation in top layer
    if Z1 > 0 and Z2 > 0:
        S, Q = g11_retard_for(np.real(eps3), eps2, np.real(eps1), spacing, 
                              ak0, d_min, Dx, Dy, Z2, Z1)
        S = S.reshape((3,3)).T
    
    ## dipole in top; evaluation in center layer
        
    if Z1 > 0 and -spacing < Z2 < 0:
        S, Q = g21_retard_for(np.real(eps3), eps2, np.real(eps1), spacing, 
                              ak0, d_min, Dx, Dy, Z1, Z2)   # Z1, Z2
        S = S.reshape((3,3))   # no transpose: 1->2
    
    ## dipole in top; evaluation in center layer
    if Z1 > 0 and Z2 < -spacing :
        S = g13_retard_for(np.real(eps3), eps2, np.real(eps1), spacing, 
                           ak0, d_min, Dx, Dy, Z2, Z1)
        S = S.reshape((3,3)).T
        
    if -spacing < Z1 < 0 and -spacing < Z2 < 0:
        raise Exception('Both dipole and evaluation positions in intermediate layer not supported.')
    return S


def Gtot_EE_123_33_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    """
    R1: dipole position
    R2: evaluation position
    """
    S0 = G0_EE(R1, R2, wavelength, eps1, eps2, eps3, spacing)
    s33 = Gs123_EE_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing)
    return S0 + s33



# =============================================================================
# retarded 3-layer Green's tensor, 3D - mixed magnetic-electric
# =============================================================================
def Gs123_HE_retard_for_rho_phi(rho, phi, zobs, z0, wavelength, eps1, eps2, eps3, spacing):
    Dx = rho*np.cos(phi)
    Dy = rho*np.sin(phi)
    
    R1 = np.array([0, 0, z0])
    R2 = np.array([Dx,Dy,zobs])
    
    return Gs123_HE_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing)


def Gs123_HE_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    d_min = 0.1   # minimum 2 point distance
    ak0 = 2*np.pi / wavelength
    
    Dx = R2[0] - R1[0]
    Dy = R2[1] - R1[1]
    Z1 = R1[2]
    Z2 = R2[2]
    
    ## in original implementation, the interface is at z=0.
    ## for consistency with pyGDM, shift evaluation such that interface is at z=spacing
    ## (subtract 2x because light makes a roundtrip)
    Z1 = Z1 - spacing    
    Z2 = Z2 - spacing    
    
    ## avoid positions exactly at boundary
    if np.round(Z1, 2) == 0:
        Z1 += d_min
    if np.round(Z1, 2) == -spacing:
        Z1 += d_min
    if np.round(Z2, 2) == 0:
        Z2 += d_min
    if np.round(Z2, 2) == -spacing:
        Z2 += d_min
    
    ## fortran retarded: substrate-layer-top --> 3-2-1 (pyGDM: 1-2-3)
    S11, Q11 = g11_retard_for(np.real(eps3), eps2, np.real(eps1), spacing, 
                              ak0, d_min, Dx, Dy, Z2, Z1)
    
    return Q11.reshape((3,3)).T


def Gtot_HE_123_33_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    """
    R1: dipole position
    R2: evaluation position
    """
    S0 = G0_HE(R1, R2, wavelength, eps1, eps2, eps3, spacing)
    s33 = Gs123_HE_retard_for(R1, R2, wavelength, eps1, eps2, eps3, spacing)
    return S0 + s33













# =============================================================================
# Green's tensor evaluation functions
# =============================================================================
def _get_nr_processes():
    """return available processes
    
    see: 
    https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
    """
    ## preffered method to get available processes (might fail on windows)
    try:
        import os
        return len(os.sched_getaffinity(0))
    except:
        pass
    
    ## if failed, try alternative using psutils
    try:
        import psutil
        return len(psutil.Process().cpu_affinity())
    except:
        pass
    
    ## fall back on multiprocessing value (if psutils not installed)
    import multiprocessing
    return multiprocessing.cpu_count()
    

@numba.njit
def get_rho_phi(DX, DY, _step=0.1):
    rho = np.round(np.sqrt(DX**2 + DY**2), 5)
    if (rho < _step/2):
        rho = 0
        phi = 0
    else:
        phi = np.arctan2(np.round(DY, 3), np.round(DX, 3))
    return rho, phi

    
@numba.njit(parallel=True)
def _eval_geo_positions_rho_phi(geo, compare_array):
    for i in numba.prange(len(geo)):    # explicit parallel loop
        R2 = geo[i]       # "observer"
        for j in range(len(geo)):
            R1 = geo[j]   # emitter
            
            DX = R2[0] - R1[0]
            DY = R2[1] - R1[1]
            Zsum = R2[2] + R1[2]
            
            rho, phi = get_rho_phi(DX, DY)
            compare_array[i,j] = [rho, phi, Zsum/2, Zsum/2]

@numba.njit
def _reconstruct_tensors(M, tensor, index_grp):
    for j in index_grp:
        M[j] = tensor

def _integrate_gs_EE_123_33_for(args):
    rho, phi, zobs, z0, wavelength, eps1, eps2, eps3, spacing = args
    SEE = Gs123_EE_retard_for_rho_phi(np.real(rho), np.real(phi), 
                                      np.real(zobs), np.real(z0), 
                                      np.real(wavelength), 
                                      eps1, eps2, eps3, np.real(spacing))
    # print(rho, phi, zobs,z0, SEE[0,0])
    return SEE

def _integrate_gs_HE_123_33_for(args):
    rho, phi, zobs, z0, wavelength, eps1, eps2, eps3, spacing = args
    SHE = Gs123_HE_retard_for_rho_phi(np.real(rho), np.real(phi), 
                                      np.real(zobs), np.real(z0), 
                                      np.real(wavelength), 
                                      eps1, eps2, eps3, np.real(spacing))
    return SHE




def t_sbs_Gs_33_retard(geo, wavelength, conf_dict, 
                       func_eval_identical_tensors=_eval_geo_positions_rho_phi,
                       func_integrate_gs=_integrate_gs_EE_123_33_for,
                       verbose=True):
    eps1 = conf_dict['eps1']
    eps2 = conf_dict['eps2']
    eps3 = conf_dict['eps3']
    spacing = np.float32(conf_dict['spacing'].real)
    
    
    ## --- determine unique tensors in coupling matrix
    t0 = time.time()
    compare_array = np.zeros([len(geo), len(geo), 4], dtype=np.float32)
    func_eval_identical_tensors(geo, compare_array)
    compare_array = np.reshape(compare_array, (-1,4))
    if verbose: 
        t1 = time.time()
        print('identification of identical tensors: {:.2f}s'.format(t1-t0))
    
    
    ## --- sort indices by identical tensors
    idx_sort = np.argsort(compare_array.view('f4,f4,f4,f4'), axis=0, order=['f0', 'f1', 'f2'])
    sorted_compare_array = compare_array[idx_sort]
    if verbose: 
        t2 = time.time()
        print('sorting:                             {:.2f}s'.format(t2-t1))
        
        
    ## --- indices of identical tensors in coupling matrix
    unique_arr, idx_start, count = np.unique(sorted_compare_array, axis=0, 
                                             return_counts=True, return_index=True)
    # unique_arr = compare_array
    # idx_sort = np.arange(len(unique_arr))
    ## splits the indices of identical tensors into separate arrays
    index_groups = np.split(idx_sort, idx_start[1:])
    if verbose: 
        t3 = time.time()
        print('indexing of unique tensors:          {:.2f}s'.format(t3-t2))
    
    
    ## --- construct coupling matrix
    ## calculate tensors with multiprocessing
    t0 = time.time()
    ## number of parallel processes
    if int(conf_dict['n_cpu'].real)==-1:
        N_cpu = _get_nr_processes()
    else:
        N_cpu = int(conf_dict['n_cpu'].real)
    
    args = np.ones((len(unique_arr), 5), dtype=np.complex64) * \
           np.array([wavelength, eps1, eps2, eps3, spacing], dtype=np.complex64)
    argslist = np.concatenate([np.squeeze(unique_arr), args], axis=1)
    
    with multiprocessing.Pool(N_cpu) as p:
        tensor_arr = p.map(func_integrate_gs, argslist)
    if verbose:
        t4 = time.time()
        print('calculating {: >6} retarded tensors: {:.2f}s (working on {} processes)'.format(len(unique_arr), t4-t3, N_cpu))
    
    
    ## --- fill coupling matrix
    M = np.zeros((len(geo)*len(geo), 3, 3), dtype=np.complex64)
    
    for i_G, idx_unique in enumerate(index_groups):
        _reconstruct_tensors(M, tensor_arr[i_G], idx_unique[:,0])
    M = np.reshape(M, [len(geo), len(geo), 3, 3]).swapaxes(0, 1)
    if verbose: 
        t5 = time.time()
        print('reconstruction of coupling matrix:   {:.2f}s'.format(t5-t4))
    
    return M


@numba.njit(parallel=True, cache=True)
def t_sbs_G0_EE_only(geo, wavelength, selfterms, conf_dict, M):
    eps1 = np.float32(conf_dict['eps1'].real)
    eps2 = conf_dict['eps2']
    eps3 = np.float32(conf_dict['eps3'].real)
    spacing = np.float32(conf_dict['spacing'].real)
    
    for i in numba.prange(len(geo)):    # explicit parallel loop
        R2 = geo[i]       # "observer"
        for j in range(len(geo)):
            R1 = geo[j]   # emitter
            ## --- vacuum dyad
            if i==j:
                ## self term
                G0 = selfterms[j]
            else:
                G0 = G0_EE(R1, R2, wavelength, eps1, eps2, eps3, spacing)

            M[i,j] = G0


@numba.njit(parallel=True, cache=True)
def t_sbs_G0_HE_only(geo, wavelength, selfterms, conf_dict, M):
    eps1 = np.float32(conf_dict['eps1'].real)
    eps2 = conf_dict['eps2']
    eps3 = np.float32(conf_dict['eps3'].real)
    spacing = np.float32(conf_dict['spacing'].real)
    
    for i in numba.prange(len(geo)):    # explicit parallel loop
        R2 = geo[i]       # "observer"
        for j in range(len(geo)):
            R1 = geo[j]   # emitter
            ## --- vacuum dyad
            if i==j:
                ## self term
                G0 = selfterms[j]
            else:
                G0 = G0_HE(R1, R2, wavelength, eps1, eps2, eps3, spacing)

            M[i,j] = G0



@numba.njit(parallel=True, cache=True)
def _construct_coupled_dipole_system_EE(M0, Ms, alpha, M_sbs):
    for i in numba.prange(len(M0)):    # explicit parallel loop
        for j in range(len(M0[0])):
            ## invertible matrix:  delta_ij*1 - G[i,j] * alpha[j]
            # M_sbs[3*i:3*i+3, 3*j:3*j+3] = Ms[i,j]    # testing
            M_sbs[3*i:3*i+3, 3*j:3*j+3] = -1 * np.dot(M0[i,j] + Ms[i,j], alpha[j])
            if i==j:
                M_sbs[3*i:3*i+3, 3*j:3*j+3] += np.identity(3)

@numba.njit(parallel=True, cache=True)
def _construct_coupled_dipole_system_HE(M0, Ms, alpha, M_sbs):
    for i in numba.prange(len(M0)):    # explicit parallel loop
        for j in range(len(M0[0])):
            ## invertible matrix:  - G[i,j] * alpha[j]
            M_sbs[3*i:3*i+3, 3*j:3*j+3] = -1 * np.dot(M0[i,j] + Ms[i,j], alpha[j])


# =============================================================================
# the actual coupling matrix generator functions
# =============================================================================
def t_sbs_EE_123_33_retard(geo, wavelength, selfterms, alpha, conf_dict, M):
    M0 = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    Msbs = np.zeros((len(geo)*3, len(geo)*3), dtype=np.complex64)

    t_sbs_G0_EE_only(geo, wavelength, selfterms, conf_dict, M0)
    Ms = t_sbs_Gs_33_retard(geo, wavelength, conf_dict, 
                            func_integrate_gs=_integrate_gs_EE_123_33_for, 
                            verbose=True)
    
    _construct_coupled_dipole_system_EE(M0, Ms, alpha, Msbs)
    M[...] = Msbs    # subsitute M in-place
    

def t_sbs_HE_123_33_retard(geo, wavelength, selfterms, alpha, conf_dict, M):
    M0 = np.zeros((len(geo), len(geo), 3, 3), dtype=np.complex64)
    Msbs = np.zeros((len(geo)*3, len(geo)*3), dtype=np.complex64)

    t_sbs_G0_HE_only(geo, wavelength, selfterms, conf_dict, M0)
    Ms = t_sbs_Gs_33_retard(geo, wavelength, conf_dict, 
                            func_integrate_gs=_integrate_gs_HE_123_33_for, 
                            verbose=True)
    
    _construct_coupled_dipole_system_HE(M0, Ms, alpha, Msbs)
    M[...] = Msbs    # subsitute M in-place
    





@numba.njit(parallel=True)
def greens_tensor_evaluation_G0(dp_pos, r_probe, G_func, wavelength, conf_dict, M, 
                                selfterm=np.zeros((3,3)).astype(np.complex64), 
                                dist_div_G=0.1):
    eps1 = conf_dict['eps1']
    eps2 = conf_dict['eps2']
    eps3 = conf_dict['eps3']
    spacing = np.float32(conf_dict['spacing'].real)
    
    for i in numba.prange(len(dp_pos)):   # explicit parallel loop
        _pos = dp_pos[i]
        for j in range(len(r_probe)):
            _r = r_probe[j]
            if np.sqrt((_r[0]-_pos[0])**2 + (_r[1]-_pos[1])**2 + (_r[2]-_pos[2])**2)<dist_div_G:
                _G = selfterm
                # xx, yy, zz, xy, xz, yx, yz, zx, zy = selfterm
            else:
                _G = G_func(_pos, _r, wavelength, eps1, eps2, eps3, spacing)
            ## return list of Greens tensors
            M[i,j] = _G

def greens_tensor_evaluation(dp_pos, r_probe, G_func, wavelength, conf_dict, M, 
                              selfterm=np.zeros((3,3)).astype(np.complex64), 
                              dist_div_G=0.1, verbose=1):
    t0 = time.time()
    ## ---- separate in G0 and Gs
    ## -- near-field
    if G_func == Gtot_EE_123_33_retard_for:
        G0_func = G0_EE
        func_integrate_gs = _integrate_gs_EE_123_33_for
    if G_func == Gtot_HE_123_33_retard_for:
        G0_func = G0_HE
        func_integrate_gs = _integrate_gs_HE_123_33_for
    ## -- asymptotic far-field
    if G_func == propagators.Gs_EE_asymptotic:
        G0_func = G0_EE_ff
        func_integrate_gs = _integrate_gs_EE_123_33_for
        
    
    ## ---- evaluate G0:
    _M_G0 = np.zeros((len(dp_pos), len(r_probe), 3, 3), dtype=np.complex64)
    if G_func in [Gtot_EE_123_33_retard_for, Gtot_HE_123_33_retard_for, propagators.Gs_EE_asymptotic]:
        greens_tensor_evaluation_G0(dp_pos, r_probe, G0_func, wavelength, conf_dict, _M_G0, 
                                    selfterm=selfterm, dist_div_G=dist_div_G)
    
    if verbose:
        t1 = time.time()
        print('calculating {: >6} free-space tensors: {:.2f}s'.format(len(dp_pos)*len(r_probe), t1-t0))
    
    
    if G_func != propagators.Gs_EE_asymptotic:
        eps1 = conf_dict['eps1']
        eps2 = conf_dict['eps2']
        eps3 = conf_dict['eps3']
        spacing = np.float32(conf_dict['spacing'].real)
        
        argslist = []
        for i in range(len(dp_pos)):
            _pos = dp_pos[i]
            for j in range(len(r_probe)):
                _r = r_probe[j]
                DX = _r[0] - _pos[0]
                DY = _r[1] - _pos[1]
                zobs = _r[2] 
                z0 = _pos[2]
                rho, phi = get_rho_phi(DX, DY)
                
                argslist.append([rho, phi, zobs, z0, wavelength, eps1, eps2, eps3, spacing])
        
        ## number of parallel processes
        if int(conf_dict['n_cpu'].real)==-1:
            N_cpu = _get_nr_processes()
        else:
            N_cpu = int(conf_dict['n_cpu'].real)
        
        with multiprocessing.Pool(N_cpu) as p:
            tensor_arr = p.map(func_integrate_gs, argslist)
        if verbose:
            t2 = time.time()
            print('calculating {: >6} retarded tensors: {:.2f}s (working on {} processes)'.format(len(argslist), t2-t1, N_cpu))
        
        _M_Gs = np.reshape(tensor_arr, [len(dp_pos), len(r_probe), 3, 3]).astype(np.complex64)
    else:
        _M_Gs = np.zeros((len(dp_pos), len(r_probe), 3, 3), dtype=np.complex64)
    
    M[...] = _M_G0 + _M_Gs




# =============================================================================
# 3D 1-2-3 retarded Dyads class
# =============================================================================
from pyGDM2 import propagators
class DyadsRetard123(propagators.DyadsQuasistatic123):
    __name__ = "3-layer environment: 3D Green's tensors with retardation"
    
    def __init__(self, n1=None, n2=None, n3=None, spacing=5000, 
                 radiative_correction=True, auto_shift_geo=False,
                 n_cpu=-1):
        super().__init__()
        
        ## Dyads
        self.G_EE = Gtot_EE_123_33_retard_for
        self.G_HE = Gtot_HE_123_33_retard_for
        self.G_EE_ff = propagators.Gs_EE_asymptotic
        
        ## evaluate propagator routine
        self.eval_G = greens_tensor_evaluation
        
        ## coupling matrix constructor routines
        self.tsbs_EE = t_sbs_EE_123_33_retard
        self.tsbs_HE = t_sbs_HE_123_33_retard
        
        ## environment definition
        ## set ref. index values or material class of environment layers
        from pyGDM2 import materials
        if isinstance(n1, (int, float, complex)) and not isinstance(n1, bool):
            self.n1_material = materials.dummy(n1)
        else:
            self.n1_material = n1
        
        n2 = n2 or n1     # if None, use `n1`
        if isinstance(n2, (int, float, complex)) and not isinstance(n2, bool):
            from pyGDM2 import materials
            self.n2_material = materials.dummy(n2)
        else:
            self.n2_material = n2
            
        n3 = n3 or n2     # if None, use `n2`
        if isinstance(n3, (int, float, complex)) and not isinstance(n3, bool):
            from pyGDM2 import materials
            self.n3_material = materials.dummy(n3)
        else:
            self.n3_material = n3
        
        self.spacing = spacing
        self.radiative_correction = radiative_correction
    
        self.auto_shift_geo = auto_shift_geo
        self.n_cpu = n_cpu
        
    
    def exceptionHandling(self, struct, efield):
        """Exception handling / consistency check for the set of tensors
        
        check if structure and incident field generator are compatible

        Parameters
        ----------
        struct : :class:`.structures.struct`
            instance of structure class
        efield : :class:`.fields.efield`
            instance of incident field class

        Returns
        -------
        bool : True if struct and field are compatible, False if they don't fit the tensors

        """
        if len(struct.geometry) > 0:
            z_min = struct.geometry.T[2].min()
            ## check if entire structure is above the spacing layer
            if self.n2_material.__name__ != self.n3_material.__name__:
                if z_min<=self.spacing:
                    if self.auto_shift_geo:
                        warnings.warn(
                            "Structure lies below upper interface. " +
                            "The structure is shifted to Z_min = spacing+step/2.")
                        struct.geometry[:,2] += self.spacing + struct.step/2 - z_min
                    else:
                        raise Exception(
                            "Structure lies below upper interface. " +
                            "This case is not implemented yet the retarded 1-2-3 dyad class." +
                            "Please place the structure above the top surface (z > spacing)." +
                            "You can disable this error by passing the parameter " + 
                            "`auto_shift_geo=True` to the dyads class.")
                        
        ## check: eps1 and eps3 must be real
        for wavelength in efield.wavelengths:
            self.getEnvironmentIndices(wavelength, struct.geometry)
            if np.imag(self.n1) != 0 or np.imag(self.n3) != 0:
                raise Exception("layer 1 (n1, substrate) and layer 3 (n3, top layer / environment) need to have purely real permittivity.")
        
        return True
    
    
    def getConfigDictG(self, wavelength, struct, efield):
        ## all data need to be same dtype, must be cast to correct type inside numba functions
        conf_dict = numba.typed.Dict.empty(key_type=numba.types.unicode_type,
                                           value_type=numba.types.complex64)
        
        conf_dict['eps1'] = np.complex64(self.n1_material.epsilon(wavelength))
        conf_dict['eps2'] = np.complex64(self.n2_material.epsilon(wavelength))
        conf_dict['eps3'] = np.complex64(self.n3_material.epsilon(wavelength))
        conf_dict['spacing'] = np.complex64(self.spacing)
        conf_dict['n_cpu'] = np.complex64(self.n_cpu)
        
        ## return a numba typed dictionary of "complex64" type,
        ## can be used to pass configuration to the green's functions
        return conf_dict
    
    
    def getEnvironmentIndices(self, wavelength, geo):
        """get environment permittivity for `wavelength` at each meshpoint"""
        self.n1 = self.n1_material.epsilon(wavelength)**0.5
        self.n2 = self.n2_material.epsilon(wavelength)**0.5
        self.n3 = self.n3_material.epsilon(wavelength)**0.5
        
        ## environment epsilon at every meshpoint
        eps_env = np.zeros(len(geo), dtype=self.dtypec)
        eps_env[geo.T[2] > 0] = self.n3_material.epsilon(wavelength)
        eps_env[np.logical_and(-self.spacing <= geo.T[2], geo.T[2] <= 0)] = self.n2_material.epsilon(wavelength)
        eps_env[geo.T[2] < -self.spacing] = self.n1_material.epsilon(wavelength)
        
        return eps_env
    
    


#%% TESTING
if __name__ == "__main__":
    

    from pyGDM2 import fields_py as fields
    from pyGDM2 import core_py as core
    from pyGDM2 import linear_py as linear
    from pyGDM2 import propagators
    
    from pyGDM2 import structures
    from pyGDM2 import materials
    from pyGDM2 import visu
    from pyGDM2 import tools
    
    
    
    ## limit nr of cpu-cores to use in scipy
    from threadpoolctl import threadpool_limits
    threadpool_limits(limits=8, user_api='blas')
    import numba
    numba.set_num_threads(8)
    
    gold = materials.gold()
    
    ## --------------- Setup environment --> define set of Green's tensors)
    n3 = 1.0   # top (environment)
    n2 = gold  # cladding
    n2 = 1.5  # cladding
    n1 = 2   # substrate
    spacing = 150   # thickness of 'n2' layer
    dyads = propagators.DyadsQuasistatic123(n1=n1, n2=n2, n3=n3, spacing=spacing)
    dyads_retard = DyadsRetard123(n1=n1, n2=n2, n3=n3, spacing=spacing)
    
    ## --------------- Setup structure
    mesh = 'cube'
    
    step = 25
    geometry = structures.rect_wire(step, L=10, H=3, W=3)
    # geometry = structures.sphere(step, R=2.5, mesh=mesh)
    # geometry.T[0] += -5*step      # shift x
    geometry.T[2] += spacing      # shift z 
    material = materials.dummy(4.0)
    
    ## shift into top layer
    geometry_NONRET = geometry.copy()
    struct = structures.struct_py(step, geometry, material)
    struct_NONRET = structures.struct_py(step, geometry_NONRET, material)
    
    
    ## --------------- Setup incident field
    ## incident field: plane wave, 400nm, lin. pol.
    wavelengths = np.linspace(500,1000, 3)
    wavelengths = [650]
    field_generator = fields.evanescent_planewave
    kwargs = dict(theta_inc=50, polar='p')   # dummy config
    efield = fields.efield(field_generator, wavelengths=wavelengths, kwargs=kwargs)
    
    
    
    
    
    
    ## --------------- put everything together
    sim = core.simulation(struct_NONRET, efield, dyads)
    sim_r = core.simulation(struct, efield, dyads_retard)
    
    
    visu.structure(sim, projection='XZ', tit='Ndp={}'.format(len(geometry)))
    visu.structure(sim_r, projection='XZ', tit='Ndp={}'.format(len(geometry)))
    
    
    #%% run sim
    ## --------------- run scatter simulation
    sim_r.scatter(calc_H=1, verbose=True)
    sim.scatter(calc_H=1, verbose=True)


    #%%
    visu.vectorfield_by_fieldindex(sim, 0, which_field='e')
    visu.vectorfield_by_fieldindex(sim_r, 0, which_field='e')
    visu.vectorfield_color_by_fieldindex(sim, 0, which_field='e')
    visu.vectorfield_color_by_fieldindex(sim_r, 0, which_field='e')
    
    #%%
    from pyGDM2 import linear
    r_probe = tools.generate_NF_map(-1000,1000,11, -250,250,7, Z0=75)
    
    Es, Et = linear.nearfield(sim, 0, r_probe, which_fields=['Es', 'Et'])
    visu.vectorfield_color(Et)
    # visu.vectorfield_color(Bt)
    
    Es_r, Et_r = linear.nearfield(sim_r, 0, r_probe, which_fields=['Es', 'Et'])
    visu.vectorfield_color(Et_r)
    # visu.vectorfield_color(Bt_r)
    
    
    #%%
    r_probe = tools.generate_NF_map(-500,500,10, 10,160,10, 0, projection='XZ')
    
    Es, Et = linear.nearfield(sim, 0, r_probe, which_fields=['Es', 'Et'])
    visu.vectorfield_color(Et)
    # visu.vectorfield_color(Bt)
    
    Es_r, Et_r = linear.nearfield(sim_r, 0, r_probe, which_fields=['Es', 'Et'])
    visu.vectorfield_color(Et_r)
    # visu.vectorfield_color(Bt_r)
    
    