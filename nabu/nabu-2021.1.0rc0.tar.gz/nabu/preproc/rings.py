import numpy as np
from .sinogram import SinoProcessing
from ..thirdparty.pore3d_deringer_munch import munchetal_filter

class MunchDeringer(SinoProcessing):

    def __init__(self, sigma, levels=None, wname='db15', sinos_shape=None, radios_shape=None):
        """
        Initialize a "Munch Et Al" sinogram deringer. See References for more information.

        Parameters
        -----------
        sigma: float
            Standard deviation of the damping parameter. The higher value of sigma,
            the more important the filtering effect on the rings.
        levels: int, optional
            Number of wavelets decomposition levels.
            By default (None), the maximum number of decomposition levels is used.
        wname: str, optional
            Default is "db15" (Daubechies, 15 vanishing moments)
        sinos_shape: tuple, optional
            Shape of the sinogram (or sinograms stack).
            This class requires either sinos_shape or radios_shape.
        radios_shape: tuple, optional
            Shape of the projection (or projections stack)
            This class requires either sinos_shape or radios_shape.

        References
        ----------
        B. Munch, P. Trtik, F. Marone, M. Stampanoni, Stripe and ring artifact removal with
        combined wavelet-Fourier filtering, Optics Express 17(10):8567-8591, 2009.
        """
        super().__init__(sinos_shape=sinos_shape, radios_shape=radios_shape)
        self.sigma = sigma
        self.levels = levels
        self.wname = wname
        self._check_can_use_wavelets()


    def _check_can_use_wavelets(self):
        if munchetal_filter is None:
            raise ValueError("Need pywavelets to use this class")


    def _destripe_2D(self, sino, output):
        res = munchetal_filter(sino, self.levels, self.sigma, wname=self.wname)
        output[:] = res
        return output


    def remove_rings(self, sinos, output=None):
        """
        Main function to performs rings artefacts removal on sinogram(s).
        CAUTION: this function defaults to in-place processing, meaning that
        the sinogram(s) you pass will be overwritten.

        Parameters
        ----------
        sinos: numpy.ndarray
            Sinogram or stack of sinograms.
        output: numpy.ndarray, optional
            Output array. If set to None (default), the output overwrites the input.
        """
        if output is None:
            output = sinos
        if sinos.ndim == 2:
            return self._destripe_2D(sinos, output)
        n_sinos = sinos.shape[0]
        for i in range(n_sinos):
            self._destripe_2D(sinos[i], output[i])
        return output

