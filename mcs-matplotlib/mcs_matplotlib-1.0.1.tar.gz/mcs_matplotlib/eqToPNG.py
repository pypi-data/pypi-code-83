from IPython.display import Image, display
from IPython.lib.latextools import latex_to_png
from sympy import latex

def equToPNG(equ, show=False):
    lt = latex(equ)
    data = latex_to_png(lt, wrap=True, color='white')
    if show:
        display(Image(data=data))
    
def latexToPNG(latex, show=False):
    data = latex_to_png(latex, wrap=True, color='white')
    if show:
        display(Image(data=data))
