from scipy.io import loadmat, savemat
from os import path, system


class RunOctave:

    __version__ = '1.0.3'

    def __init__(self, octave_path):
        self.octave_path = octave_path.replace(' ','" "')
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # Comma-separated letters
        self.CSL = ','.join(self.alphabet)

        # Getting PATH of temp files
        self.lib_path = path.split(path.abspath(__file__))[0]
        # print(self.lib_path)
        self.tempdata_path = path.join(self.lib_path, 'tempdata.mat').replace('\\','/')
        self.tempscript_path = path.join(self.lib_path, 'tempscript.m').replace('\\','/')


    def output_formatter(self, nargout, data):
        ret = []
        for key in self.alphabet[:nargout]:
            value = data[key]
            if value.shape == (1, 1):
                ret.append(value[0][0])
            else:
                ret.append(value)

        if nargout == 1:
            return ret[0]
        else:
            return ret


    def mat_file(self, nargout, syntax):
        # Auxiliary function
        with open(self.tempscript_path, 'w') as MAT_file:
            print('load("' + self.tempdata_path + '")', file=MAT_file)
            print(syntax, file=MAT_file)
            print('save("-mat-binary","' + self.tempdata_path + '")', file=MAT_file)

        # Executes the auxiliary function
        system(self.octave_path + ' ' + self.tempscript_path)

        # Read the communication channel
        data = loadmat(self.tempdata_path)

        return self.output_formatter(nargout, data)


    def run(self, target, args=None, nargout=0):
        if isinstance(args, tuple):
            nargin = len(args)
            varargin  = self.CSL[:nargin*2-1]
            syntax = target + '(' + varargin + ');'

            # Write in the communication channel
            savemat(self.tempdata_path, dict(zip(self.alphabet[:nargin], args)))
        else:
            if any(c in target for c in "[]=(,) '+-*/:"):
                syntax = target
            else:
                syntax = target + '();'

            # Write in the communication channel
            savemat(self.tempdata_path, {'None': []})

        if nargout > 0:
            varargout = self.CSL[:nargout*2-1]
            syntax = '[' + varargout + '] = ' + syntax

        return self.mat_file(nargout, syntax)
