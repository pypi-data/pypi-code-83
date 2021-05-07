r"""
This module is responsible for collecting the energy barriers of succsessive gneb calculations
"""
from pathlib import Path
from python3.shell_commands import copy_element
import os
import pandas as pd
import numpy as np


class CCollectSuccsessiveBarr:
    r"""
    Class for collecting barriers of succsesive calculations within directory
    """

    def __init__(self, prefix: str, calcdir: Path = Path.cwd(), resultdir: Path = Path.cwd().parent / 'barr_succ',
                 split_or_op: str = 'op', convergency_crit: float = 1.1*10**(-8)) -> None:
        r"""
        Initializes the collection
        """
        resultdir.mkdir(exist_ok=False)
        self._calcdir = calcdir
        self._resultdir = resultdir
        self._split_or_op = split_or_op
        self._prefix = prefix
        self._convergencycrit = convergency_crit

    def __call__(self) -> None:
        r"""
        Calls the collection of barriers
        """
        if self._split_or_op == 'split':
            dict = {'J': [], 'E_im': [], 'E_mf': []}
            for folder in os.listdir(str(self._calcdir)):
                j = float(str(folder).replace(self._prefix, ''))
                E_im = None
                E_mf = None
                p_im =  self._calcdir / str(folder) / 'im'
                p_mf =  self._calcdir / str(folder) / 'mf'
                if p_im.is_dir():
                    L = []
                    for line in reversed(open(str(p_im / 'force_mep.txt')).readlines()):
                        L = line.split()
                        break
                    if float(L[1]) <= self._convergencycrit:
                        df_im = pd.read_csv(p_im / 'en_path.out', sep=r'\s+', usecols=[0,1,2], names=['R', 'E', 'dE'], index_col=False)
                        E_im = np.max(df_im['E'].to_numpy())
                    else:
                        print(f'im-calc for {self._prefix}={j} not converged. E_im will be none')
                else:
                    print(f'Mode split selected but did not find im-folder. Will skip {self._prefix}={j}.')

                if p_im.is_dir():
                    L = []
                    for line in reversed(open(str(p_im / 'force_mep.txt')).readlines()):
                        L = line.split()
                        break
                    if float(L[1]) <= self._convergencycrit:
                        df_mf = pd.read_csv(p_mf / 'en_path.out', sep=r'\s+', usecols=[0, 1, 2], names=['R', 'E', 'dE'],
                                         index_col=False)
                        if E_im is None:
                            print(f'im-calc for {self._prefix}={j} not converged. E_mf will be also none')
                        else:
                            E_mf = np.max(df_mf['E'].to_numpy())
                    else:
                        print(f'mf-calc for {self._prefix}={j} not converged. E_mf will be none')
                else:
                    print(f'Mode split selected but did not find im-folder. Will skip {self._prefix}={j}.')
                dict['J'].append(j)
                dict['E_im'].append(E_im)
                dict['E_mf'].append(E_mf)
        elif self._split_or_op == 'op':
            dict = {'J': [], 'E_op': []}
            for folder in os.listdir(str(self._calcdir)):
                j = float(str(folder).replace(self._prefix, ''))
                E_op = None
                p =  self._calcdir / str(folder)
                L = []
                for line in reversed(open(str(p / 'force_mep.txt')).readlines()):
                    L = line.split()
                    break
                if float(L[1]) <= self._convergencycrit:
                    df_im = pd.read_csv(p / 'en_path.out', sep=r'\s+', usecols=[0,1,2], names=['R', 'E', 'dE'], index_col=False)
                    E_op = np.max(df_im['E'].to_numpy())
                else:
                    print(f'op-calc for {self._prefix}={j} not converged. E_op will be none')
                dict['J'].append(j)
                dict['E_op'].append(E_op)
        else:
            raise NotImplementedError('Other type than op or split is not implemented yet.')

        pd.DataFrame(dict).to_csv(self._resultdir / 'barriers_succsessive.dat')
