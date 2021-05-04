# encoding: utf-8
#
#Copyright (C) 2017-2020, P. R. Wiecha
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
python implementations of the Green's Dyads, accelerated using `numba`
"""
from __future__ import print_function
from __future__ import absolute_import

import copy
import math
import warnings
import cmath

import numpy as np
import numba

from pyGDM2 import propagators
try:
    from pyGDM_retard_for import g11_retard
except ImportError:
    from .pyGDM_retard_for import g11_retard

## --- free space propagators, fcts of (R1, R2, wavelength, eps1, eps2, eps3, spacing)
G0_EE = propagators.G0_EE_123
G0_HE = propagators.G_HE_123






### --- retarded 3D
# =============================================================================
# retarded 3-layer Green's tensor, 3D
# =============================================================================
def Gs123_retard(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    ## definition: s11,q11 = g11_retard(eps1,eps2,eps3,d,ak0,a,xd,yd,z,z0)
    
    d_min = 3.0   # minimum 2 point distance
    ak0 = 2*np.pi / wavelength
    
    Dx = R2[0] - R1[0]
    Dy = R2[1] - R1[1]
    Z0 = R1[2]
    Z1 = R2[2]
    
    #### fortran retarded: substrate-layer-top: 3-2-1(probably wrong!)
    ## fortran retarded: substrate-layer-top: 1-2-3
    S11, Q11 = g11_retard(eps1, eps2, eps3, spacing, ak0, d_min, Dx, Dy, Z1, Z0)
    
    xx, yy, zz = S11[0], S11[4], S11[8]
    xy, xz, yx = S11[1], S11[2], S11[3]
    yz, zx, zy = S11[5], S11[6], S11[7]
    
    return xx, yy, zz, xy, xz, yx, yz, zx, zy


#@numba.njit(cache=True)
def Gtot_retard(R1, R2, wavelength, eps1, eps2, eps3, spacing):
    xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_EE.py_func(R1, R2, wavelength, eps1, eps2, eps3, spacing)
    if eps1 != eps3 or eps2 != eps3:
        xxs,yys,zzs,xys,xzs,yxs,yzs,zxs,zys = Gs123_retard(R1, R2, wavelength, 
                                                          eps1, eps2, eps3, spacing)
        xx, yy, zz, xy, xz, yx, yz, zx, zy = xx+xxs, yy+yys, zz+zzs, \
                                             xy+xys, xz+xzs, yx+yxs, \
                                             yz+yzs, zx+zxs, zy+zys
        
    
    return xx, yy, zz, \
           xy, xz, yx, \
           yz, zx, zy




## --- multi-dipole / multi-probe propagator evaluation
@numba.njit(parallel=True)
def greens_tensor_evaluation_retard(dp_pos, r_probe, G_func, wavelength, conf_dict, M, 
                                    selfterm=np.zeros((3,3)).astype(np.complex64), 
                                    dist_div_G=0.5):
    eps1 = conf_dict['eps1']
    eps2 = conf_dict['eps2']
    eps3 = conf_dict['eps3']
    spacing = np.float32(conf_dict['spacing'].real)
    
    for i in numba.prange(len(dp_pos)):   # explicit parallel loop
        _pos = dp_pos[i]
        for j in range(len(r_probe)):
            _r = r_probe[j]
            if np.sqrt((_r[0]-_pos[0])**2 + (_r[1]-_pos[1])**2 + (_r[2]-_pos[2])**2)<dist_div_G:
                xx, xy, xz = selfterm[0]
                yx, yy, yz = selfterm[1]
                zx, zy, zz = selfterm[2]
                # xx, yy, zz, xy, xz, yx, yz, zx, zy = selfterm
            else:
                xx, yy, zz, xy, xz, yx, yz, zx, zy = G_func(_pos, _r, wavelength, 
                                                            eps1, eps2, eps3, spacing)
            ## return list of Greens tensors
            M[i,j,0,0], M[i,j,1,1], M[i,j,2,2] = xx, yy, zz
            M[i,j,1,0], M[i,j,2,0], M[i,j,0,1] = yx, zx, xy
            M[i,j,2,1], M[i,j,0,2], M[i,j,1,2] = zy, xz, yz


# @numba.njit(parallel=True, cache=True)
def t_sbs_EE_123_retard(geo, wavelength, selfterms, alpha, conf_dict, M):
    eps1 = conf_dict['eps1']
    eps2 = conf_dict['eps2']
    eps3 = conf_dict['eps3']
    spacing = np.float32(conf_dict['spacing'].real)
    
    for i in numba.prange(len(geo)):    # explicit parallel loop
        R2 = geo[i]       # "observer"
        print(i,len(geo))
        for j in range(len(geo)):
            R1 = geo[j]   # emitter
            aj = alpha[j]
            st = selfterms[j]
            ## --- vacuum dyad
            if i==j:
                ## self term
                xx, yy, zz = st[0,0], st[1,1], st[2,2]
                xy, xz, yx = st[0,1], st[0,2], st[1,0]
                yz, zx, zy = st[1,2], st[2,0], st[2,1]
            else:
                xx, yy, zz, xy, xz, yx, yz, zx, zy = G0_EE(R1, R2, wavelength, 
                                                                eps1, eps2, eps3, spacing)
            
            ## --- 1-2-3 surface dyad (non retarded NF approximation)
            if eps1!=eps2 or eps2!=eps3:
                xxs,yys,zzs,xys,xzs,yxs,yzs,zxs,zys = Gs123_retard(
                                  R1, R2, wavelength, eps1, eps2, eps3, spacing)
                ## combined dyad
                xx, yy, zz, xy, xz, yx, yz, zx, zy = xx+xxs, yy+yys, zz+zzs, \
                                                      xy+xys, xz+xzs, yx+yxs, \
                                                      yz+yzs, zx+zxs, zy+zys
            
            ## return invertible matrix:  delta_ij*1 - G[i,j] * alpha[j]
            M[3*i+0, 3*j+0] = -1*(xx*aj[0,0] + xy*aj[1,0] + xz*aj[2,0])
            M[3*i+1, 3*j+1] = -1*(yx*aj[0,1] + yy*aj[1,1] + yz*aj[2,1])
            M[3*i+2, 3*j+2] = -1*(zx*aj[0,2] + zy*aj[1,2] + zz*aj[2,2])
            M[3*i+0, 3*j+1] = -1*(xx*aj[0,1] + xy*aj[1,1] + xz*aj[2,1])
            M[3*i+0, 3*j+2] = -1*(xx*aj[0,2] + xy*aj[1,2] + xz*aj[2,2])
            M[3*i+1, 3*j+0] = -1*(yx*aj[0,0] + yy*aj[1,0] + yz*aj[2,0])
            M[3*i+1, 3*j+2] = -1*(yx*aj[0,2] + yy*aj[1,2] + yz*aj[2,2])
            M[3*i+2, 3*j+0] = -1*(zx*aj[0,0] + zy*aj[1,0] + zz*aj[2,0])
            M[3*i+2, 3*j+1] = -1*(zx*aj[0,1] + zy*aj[1,1] + zz*aj[2,1])
            if i==j:
                M[3*i+0, 3*j+0] += 1
                M[3*i+1, 3*j+1] += 1
                M[3*i+2, 3*j+2] += 1


# @numba.njit(parallel=True, cache=True)
# def t_sbs_HE_123_quasistatic(geo, wavelength, eps1, eps2, eps3, spacing, selfterms, alpha, M):
def t_sbs_HE_123_retard(geo, wavelength, selfterms, alpha, conf_dict, M):
    ##!!! TODO: correct retarded HE
    eps2 = conf_dict['eps2']
    
    for i in numba.prange(len(geo)):    # explicit parallel loop
        R2 = geo[i]        # "observer"
        for j in range(len(geo)):
            R1 = geo[j]    # emitter
            aj = alpha[j]
            st = selfterms[j]
            ## --- vacuum dyad
            if i==j:
                ## self term
                xx, yy, zz = st[0,0], st[1,1], st[2,2]
                xy, xz, yx = st[0,1], st[0,2], st[1,0]
                yz, zx, zy = st[1,2], st[2,0], st[2,1]
            else:
                ## we need G^HE: H-field due to e-dipole
                xx, yy, zz, xy, xz, yx, yz, zx, zy = propagators._G0_HE(R1, R2, wavelength, eps2)
            
            ## return: G[i,j] * alpha[j]
            ## --- magnetic-electric part
            M[3*i+0, 3*j+0] = -1*(xx*aj[0,0] + xy*aj[1,0] + xz*aj[2,0])
            M[3*i+1, 3*j+1] = -1*(yx*aj[0,1] + yy*aj[1,1] + yz*aj[2,1])
            M[3*i+2, 3*j+2] = -1*(zx*aj[0,2] + zy*aj[1,2] + zz*aj[2,2])
            M[3*i+0, 3*j+1] = -1*(xx*aj[0,1] + xy*aj[1,1] + xz*aj[2,1])
            M[3*i+0, 3*j+2] = -1*(xx*aj[0,2] + xy*aj[1,2] + xz*aj[2,2])
            M[3*i+1, 3*j+0] = -1*(yx*aj[0,0] + yy*aj[1,0] + yz*aj[2,0])
            M[3*i+1, 3*j+2] = -1*(yx*aj[0,2] + yy*aj[1,2] + yz*aj[2,2])
            M[3*i+2, 3*j+0] = -1*(zx*aj[0,0] + zy*aj[1,0] + zz*aj[2,0])
            M[3*i+2, 3*j+1] = -1*(zx*aj[0,1] + zy*aj[1,1] + zz*aj[2,1])








### --- dyad class 3D 123 retarded
class DyadsRetarded123(propagators.DyadsBaseClass):
    __name__ = "retarded 3D '1-2-3' Green's tensors"
    
    def __init__(self, n1=None, n2=None, n3=None, spacing=5000, 
                 radiative_correction=True):
        super().__init__()
        
        ## Dyads
        self.G_EE = Gtot_retard
        self.G_HE = G0_HE
        self.G_EE_ff = propagators.Gs_EE_asymptotic
        
        ## evaluate propagator routine
        self.eval_G = propagators.greens_tensor_evaluation
        
        ## coupling matrix constructor routines
        self.tsbs_EE = t_sbs_EE_123_retard
        self.tsbs_HE = t_sbs_HE_123_retard
        
        ## environment definition
        ## set ref. index values or material class of environment layers
        from pyGDM2 import materials
        if isinstance(n1, (int, float, complex)) and not isinstance(n1, bool):
            self.n1_material = materials.dummy(n1)
        else:
            self.n1_material = n1
            
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
    
    def __repr__(self):
        """description about simulation environment defined by set of dyads
        """
        out_str =  ' ------ environment -------'
        out_str += '\n ' + self.__name__
        out_str += '\n '
        out_str += '\n' + '   n3 = {}  <-- top'.format(self.n3_material.__name__)
        out_str += '\n' + '   n2 = {}  <-- structure zone (height "spacing" = {}nm)'.format(
                        self.n2_material.__name__, self.spacing)
        out_str += '\n' + '   n1 = {}  <-- substrate'.format(self.n1_material.__name__)
        return out_str
    
    
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
        z_min = struct.geometry.T[2].min()
        z_max = struct.geometry.T[2].max()
        ## if interface 1/2 exists, check if entire structure is below or above
        if self.n1_material.__name__ != self.n2_material.__name__:
            if z_min<0 and z_max>0:
                warnings.warn("Structure in-between substrate and middle-layer. " +
                              "This is not supported and will most likely falsify the simulation.")
        
        ## if interface 2/3 exists, check if entire structure is below or above
        if self.n2_material.__name__ != self.n3_material.__name__:
            if z_min<self.spacing and z_max>self.spacing:
                warnings.warn("Structure in-between middle and top cladding layer. " +
                              "This is not supported and will most likely falsify the simulation.")
        
        return True
    
    
    def getConfigDictG(self, wavelength, struct, efield):
        ## all data need to be same dtype, must be cast to correct type inside numba functions
        conf_dict = numba.typed.Dict.empty(key_type=numba.types.unicode_type,
                                           value_type=numba.types.complex64)
        
        conf_dict['eps1'] = np.complex64(self.n1_material.epsilon(wavelength))
        conf_dict['eps2'] = np.complex64(self.n2_material.epsilon(wavelength))
        conf_dict['eps3'] = np.complex64(self.n3_material.epsilon(wavelength))
        conf_dict['spacing'] = np.complex64(self.spacing)
        
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
        eps_env[geo.T[2].min() > self.spacing] = self.n3_material.epsilon(wavelength)
        eps_env[0 <= geo.T[2].min() <= self.spacing] = self.n2_material.epsilon(wavelength)
        eps_env[geo.T[2].min() < 0] = self.n1_material.epsilon(wavelength)
        
        return eps_env
        
        
    def getSelfTermEE(self, wavelength, struct):
        eps_env = self.getEnvironmentIndices(wavelength, struct.geometry)
        struct.setWavelength(wavelength)
        
        k0 = 2.0*np.pi / float(wavelength)
        
        if struct.normalization == 0:
            cnorm = np.zeros(len(eps_env))
        else:
            norm_nonrad = -4.0 * np.pi * struct.normalization / (3.0 * struct.step**3 * eps_env)
            
            if self.radiative_correction:
                norm_rad = 1j * 2.0 * struct.normalization * (k0**3)/3.0 * np.ones(len(norm_nonrad))
                cnorm = norm_nonrad + norm_rad
            else:
                cnorm = norm_nonrad
        
        self_term_tensors_EE = np.zeros([len(norm_nonrad), 3, 3], dtype=self.dtypec)
        self_term_tensors_EE[:,0,0] = cnorm
        self_term_tensors_EE[:,1,1] = cnorm
        self_term_tensors_EE[:,2,2] = cnorm
        
        return self_term_tensors_EE
        
    
    def getSelfTermHE(self, wavelength, struct):
        eps_env = self.getEnvironmentIndices(wavelength, struct.geometry)
        struct.setWavelength(wavelength)
        
        self_term_tensors_HE = np.zeros([len(eps_env), 3, 3], dtype=self.dtypec)
        
        return self_term_tensors_HE
        
        
    def getPolarizabilityTensor(self, wavelength, struct):
        eps_env = self.getEnvironmentIndices(wavelength, struct.geometry)
        struct.setWavelength(wavelength)
        normalization = struct.normalization
        eps = struct.epsilon_tensor 
        
        vcell_norm = struct.step**3 / float(normalization)
        
        eps_env_tensor = np.zeros(eps.shape, dtype=self.dtypec)
        eps_env_tensor[:,0,0] = eps_env
        eps_env_tensor[:,1,1] = eps_env
        eps_env_tensor[:,2,2] = eps_env
        
        ## --- isotropic polarizability
        alphatensor = np.asfortranarray((eps - eps_env_tensor) * 
                                      vcell_norm / (4.0 * np.pi), dtype=self.dtypec)
        
        return alphatensor






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
    n3 = 1.0  # top
    n2 = gold.epsilon(500)**0.5   # env.
    n1 = 1.5  # substrate
    spacing = 50   # thickness of 'n2' layer
    dyads = propagators.DyadsQuasistatic123(n1=n1, n2=n2, n3=n3, spacing=spacing)
    dyads_retard = DyadsRetarded123(n1=n1, n2=n2, n3=n3, spacing=spacing)
    
    ## --------------- Setup structure
    mesh = 'cube'
    
    step = 20
    geometry = structures.rect_wire(step, L=5, H=1, W=5)
    # geometry = structures.sphere(step, R=2.5, mesh=mesh)
    geometry.T[0] += -5*step      # shift x
    material = materials.dummy(2.0)
    
    ## shift into top layer
    geometry_NONRET = geometry.copy()
    geometry_NONRET.T[2] += spacing
    struct = structures.struct_py(step, geometry, material)
    struct_NONRET = structures.struct_py(step, geometry_NONRET, material)
    
    
    ## --------------- Setup incident field
    ## incident field: plane wave, 400nm, lin. pol.
    wavelengths = np.linspace(500,1000, 10)
    wavelengths = [500]
    field_generator = fields.evanescent_planewave
    kwargs = dict(theta_inc=45, polar='p')   # dummy config
    efield = fields.efield(field_generator, wavelengths=wavelengths, kwargs=kwargs)
    
    
    
    
    
    
    ## --------------- put everything together
    sim = core.simulation(struct_NONRET, efield, dyads)
    sim_r = core.simulation(struct, efield, dyads_retard)
    
    
    visu.structure(sim, projection='XZ', tit='Ndp={}'.format(len(geometry)))
    visu.structure(sim_r, projection='XZ', tit='Ndp={}'.format(len(geometry)))
    
    
    #%% run sim
    ## --------------- run scatter simulation
    sim_r.scatter(calc_H=0, verbose=True)
    sim.scatter(calc_H=0, verbose=True)


    #%%
    visu.vectorfield_by_fieldindex(sim, 0)
    visu.vectorfield_by_fieldindex(sim_r, 0)
    
    
    
    #%%
    # S = core.get_SBS_EE(sim_r, wavelengths[0])
    # #%%
    # S2 = S.reshape(len(S)//3, 3, -1, 3).swapaxes(1,2).reshape(-1, 3, 3).reshape(len(S)//3,len(S)//3, 3, 3)
    
    # tensornorm = np.linalg.norm(S2, axis=(2,3), ord='fro')
    # N_indiv = len(np.unique(tensornorm))
    # N_tensors = np.product(tensornorm.shape)
    # print("{}/{} = {:.3f}%".format(N_indiv, N_tensors, 100*(N_indiv/N_tensors)))
    