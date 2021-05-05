from pathlib import Path
import pandas as pd

class LaserPowerStudy:
    '''
    Class that reads a csv-file with laser power measurements in the format
    
    Frequency;Percentage;Power
    XX;YY;ZZ
    ...
    
    Where the Frequency is given in kHz and the power in mW.
    Outputs an excel file and a diagram
    '''
    
    def __init__(self, csv_filepath):
        self._data = pd.read_csv(csv_filepath, delimiter=';')
        self._data = self._data.astype('float')
        
    def process_data(self, output_path=None):
        import matplotlib.pyplot as plt
        import io
        fig, ax = plt.subplots()
        for frequency in sorted(self._data['Frequency'].unique().tolist()):
            subset = self._data.loc[self._data['Frequency'] == frequency]
            x, y = subset['Percent'].values, subset['Power'].values
            ax.plot(x, y, label=frequency, marker='o', markeredgewidth=1, 
                    markeredgecolor='k')
        ax.set_xlabel('Power (%)')
        ax.set_ylabel('Power (mW)')
        handles, labels = ax.get_legend_handles_labels()
        labels = [label + ' kHz' for label in labels]
        ax.legend(handles=handles, labels=labels, title='Repetition rate')
        ax.grid()
        if output_path:
            if not isinstance(output_path, Path):
                output_path = Path(output_path)
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=100)
            buf.seek(0)
            self._save_excel(output_path / 'laser_power.xlsx')
            import openpyxl
            wb = openpyxl.load_workbook(output_path / 'laser_power.xlsx')
            ws = wb.worksheets[0]
            img = openpyxl.drawing.image.Image(buf)
            img.anchor = 'A16'
            ws.add_image(img)
            wb.save(output_path / 'laser_power.xlsx')
            
        else:
            plt.show()
            
    def _save_excel(self, output_path):
        from copy import deepcopy
        data = deepcopy(self._data)
        data.columns = ['Frequency (kHz)', 'Percent (%)', 'Power (mW)']
        data = data.pivot(index='Percent (%)', columns='Frequency (kHz)', 
                          values='Power (mW)')
        data.columns = [f'{val} kHz' for val in data.columns.tolist()]
        data.to_excel(output_path)

    