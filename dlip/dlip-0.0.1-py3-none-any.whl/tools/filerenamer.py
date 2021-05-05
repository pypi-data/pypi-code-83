import os
from ..utils import str_to_num

class FileRenamer:
    
    def __init__(self, path, extension='.vk4'):
        self.path = path
        self.extension = extension
        self.files = self.find_files()
        self.new_files = []
    
    def find_files(self):
        files = [file for file in os.listdir(self.path) if file.endswith(self.extension)]
        numbers = [int(os.path.splitext(file)[0].split('_')[-1]) for file in files]
        sorted_files = [file for number, file in sorted(zip(numbers, files))]
        return sorted_files
    
    def rename_files(self, basename, nrows, row_name, row_0, row_step, ncols, 
                     col_name, col_0, col_step, nrep=1, nrep_start=1):
        self.new_files = []
        if nrows * ncols * nrep != len(self.files):
            raise ValueError('Amount of rows and columns does not correspond to amount of files')
        for i in range(ncols):
            cval = col_0 + col_step * i
            for j in range(nrows):
                for k in range(nrep):
                    rval = row_0 + row_step * j
                    reps = k + 1
                    filenumber = (i * nrows + j) * nrep + k
                    new_filename = f'{basename}_{col_name}{cval}_{row_name}{rval}_REP{reps + nrep_start - 1}{self.extension}'
                    self.new_files.append(new_filename)
                    current_filepath = os.path.join(self.path, self.files[filenumber])
                    new_filepath = os.path.join(self.path, new_filename)
                    os.rename(current_filepath, new_filepath)
                    print(f'{self.files[filenumber]}\t->\t{new_filename}')
                
    def easy_rename(self):
        args = []
        queries = (
            'Sample ID:',
            'Pulse duration (ns, ps):',
            'Wavelength (ir, vis, uv):',
            'Repetition Rate (kHz):',
            'Period:',
            'Hatch distance:',
            'Number of rows:', 
            'Row name (eg. f, n, ...):',
            'First value of row:',
            'Step between rows:',
            'Number of columns:',
            'Column name (eg. f, n, ...)',
            'First value of column:',
            'Step between columns:',
            'Measurement repetitions (default 1):',
            'Measurement repetitions start (default 1):'
        )
        
        for query in queries:
            args.append(str_to_num(input(query + '\t').upper()))
        basename = '{}_{}_{}_R{}_P{}_HD{}'.format(*args[:6])
        nrep, nrep_start = args[-2:]
        args = (basename, *args[6:-2])
        self.rename_files(*args, nrep=nrep, nrep_start=nrep_start)
    
    def restore(self):
        if self.new_files:
            for current_file, original_file in zip(self.new_files, self.files):
                current_filepath = os.path.join(self.path, current_file)
                new_filepath = os.path.join(self.path, original_file)
                os.rename(current_filepath, new_filepath)
                print(f'{current_file}\t->\t{original_file}')
            self.new_files = []
        else:
            raise FileNotFoundError('Files are in their original state')
        
    