""" Wrapper for sme_synth.so C library """
import os
from os.path import dirname, join
import logging

import numpy as np

from .cwrapper import get_lib_name, IDL_DLL

logger = logging.getLogger(__name__)


class SME_DLL:
    """ Object Oriented interface for the SME C library """

    def __init__(self, libfile=None, datadir=None):
        #:LineList: Linelist passed to the library
        self.linelist = None
        #:int: Number of mu points passed to the library
        self.nmu = None
        #:Abund: Elemental abundances passed to the library
        self.abund = None
        #:float: First wavelength of the current segment in Angstrom
        self.wfirst = None
        #:float: Last wavelength of the current segment in Angstrom
        self.wlast = None
        #:float: Van der Waals broadening parameter set in the library
        self.vw_scale = None
        #:bool: Whether the library uses H2 broadening or not
        self.h2broad = False
        #:float: Effective temperature set in the model
        self.teff = None
        #:float: Surface gravity set in the model
        self.grav = None
        #:float: Turbulence velocity in the model in km/s
        self.vturb = None
        #:Atmo: Atmosphere structure in the model
        self.atmo = None
        #:dict: NLTE subgrids for nlte coefficient interpolation
        self._nlte_grids = {}
        self.ion = None

        self.lib = IDL_DLL(libfile)
        self.SetLibraryPath(datadir)

        self.check_data_files_exist()

    @property
    def libfile(self):
        """str: Location of the library file"""
        return self.lib.libfile

    @property
    def file(self):
        """str: Location of the library file"""
        # Deprecated
        return self.libfile

    @property
    def datadir(self):
        """str: Expected directory of the data files"""
        return self.GetLibraryPath()

    @property
    def ndepth(self):
        """int: Number of depth layers in the atmosphere model"""
        assert self.atmo is not None, f"No model atmosphere has been set"
        motype = self.atmo.depth
        return len(self.atmo[motype])

    @property
    def nlines(self):
        """int: number of lines in the linelist"""
        assert self.linelist is not None, f"No line list has been set"
        return len(self.linelist)

    def check_data_files_exist(self):
        """
        Checks if required data files for the SME library exist.
        If they dont exist, SME will just segfault, without any hint.

        Raises
        ------
        FileNotFoundError
            If any of the files don't exist
        """
        names = self.GetDataFiles()
        directory = self.GetLibraryPath()
        for name in names:
            n = os.path.join(directory, name)
            if not os.path.exists(n):
                raise FileNotFoundError(
                    f"Could not find required data file {name} in library directory {directory}"
                )

    def SMELibraryVersion(self):
        """
        Return SME library version

        Returns
        -------
        version : str
            SME library version
        """
        version = self.lib.call("SMELibraryVersion", raise_error=False)
        return version

    def SetLibraryPath(self, datadir=None):
        """ Set the path to the library """
        if datadir is None:
            datadir = join(dirname(__file__), "share", "libsme")
        datadir = str(datadir)
        # Against all conventions, SME lib expects a "/" at the end of the path
        if not datadir.endswith(os.sep):
            datadir = datadir + os.sep
        self.lib.SetLibraryPath(datadir, type="string")

    def GetLibraryPath(self):
        """ Get the data file directory """
        return self.lib.GetLibraryPath(raise_error=False)

    def GetDataFiles(self):
        """ Get the required data files """
        files = self.lib.GetDataFiles(raise_error=False)
        if files != "Using obsolete SME Library":
            return files.split(";")
        else:
            logging.warning(
                "Using obsolete SME Library. Cannot determine necessay data files"
            )
            return []

    def InputWaveRange(self, wfirst, wlast):
        """
        Read in Wavelength range

        Will raise an exception if wfirst is larger than wlast

        Parameters
        ----------
        wfirst : float
            first wavelength of the segment
        wlast : float
            last wavelength of the segment
        """
        assert (
            wfirst < wlast
        ), "Input Wavelength range is wrong, first wavelength is larger than last"
        self.lib.InputWaveRange(wfirst, wlast, type="double")

        self.wfirst = wfirst
        self.wlast = wlast

    def SetVWscale(self, gamma6):
        """
        Set van der Waals scaling factor

        Parameters
        ----------
        gamma6 : float
            van der Waals scaling factor
        """
        logger.debug("Setting Van der Waals scale in smelib")
        self.lib.SetVWscale(gamma6, type="double")
        self.vw_scale = gamma6

    def SetH2broad(self, h2_flag=True):
        """ Set flag for H2 molecule """
        logger.debug("Setting H2 broadening in smelib")

        if h2_flag:
            self.lib.SetH2broad()
            self.h2broad = True
        else:
            self.ClearH2broad()

    def ClearH2broad(self):
        """ Clear flag for H2 molecule """
        self.lib.ClearH2broad()
        self.h2broad = False

    def InputLineList(self, linelist):
        """
        Read in line list

        Parameters
        ---------
        atomic : array of size (nlines, 8)
            atomic linelist data for each line
            fields are: atom_number, ionization, wlcent, excit, gflog, gamrad, gamqst, gamvw
        species : array(string) of size (nlines,)
            names of the elements (with Ionization level)
        """
        try:
            atomic = linelist.atomic.T
            species = linelist.species
        except AttributeError:
            raise TypeError("linelist has to be a LineList type")

        nlines = len(linelist)
        species = np.asarray(species, "U8")

        assert (
            atomic.shape[1] == nlines
        ), f"Got wrong Linelist shape, expected ({nlines}, 8) but got {atomic.shape}"
        assert (
            atomic.shape[0] == 8
        ), f"Got wrong Linelist shape, expected ({nlines}, 8) but got {atomic.shape}"

        logger.debug("Passing linelist to smelib")
        self.lib.InputLineList(
            nlines, species, atomic, type=("int", "string", "double")
        )

        self.linelist = linelist

    def OutputLineList(self):
        """
        Return line list

        Returns
        -------
        atomic : array of size (nlines, 6)
            relevant data of the linelist
            wlcent, excit, gflog, gamrad, gamqst, gamvw
        """
        nlines = self.nlines
        atomic = np.zeros((nlines, 6))
        self.lib.OutputLineList(nlines, atomic, type=("int", "double"))
        return atomic

    def UpdateLineList(self, atomic, species, index):
        """
        Change line list parameters

        Parameters
        ---------
        atomic : array of size (nlines, 8)
            atomic linelist data for each line
            fields are: atom_number, ionization, wlcent, excit, gflog, gamrad, gamqst, gamvw
        species : array(string) of size (nlines,)
            names of the elements (with Ionization level)
        index : array(int) of size (nlines,)
            indices of the lines to update relative to the overall linelist
        """
        nlines = atomic.shape[0]
        assert (
            atomic.shape[1] == 8
        ), f"Got wrong Linelist shape, expected ({nlines}, 8) but got {atomic.shape}"

        assert (
            len(index) == nlines
        ), "Inconsistent number if lines, between index and linelist"
        assert (
            len(species) == nlines
        ), "Inconsistent number if lines, between index and linelist"

        atomic = atomic.T

        logger.debug("Updating linelist in smelib")
        self.lib.UpdateLineList(
            nlines, species, atomic, index, type=("int", "str", "double", "short")
        )

    def InputModel(self, teff, grav, vturb, atmo):
        """ Read in model atmosphere

        Parameters
        ---------
        teff : float
            effective Temperature in Kelvin
        grav : float
            surface gravity in log10(cgs)
        vturb : float
            turbulence velocity in km/s
        atmo : Atmo
            atmosphere structure (see Atmo for details)
        """

        if teff <= 0:
            raise ValueError("Temperature must be positive (unit is Kelvin)")
        if vturb < 0:
            raise ValueError("Turbulence velocity must be positive or zero")

        try:

            #   MOTYPE==0   means depth scale is "Tau", plane-parralel
            #   MOTYPE==1   means depth scale is "Rhox", plane-parralel
            #   MOTYPE==3   means depth scale is "RhoX", spherical
            #   MOTYPE==-1  fake value used with the call to OPMTRX get just
            #               just the line opacities

            if atmo.geom == "SPH":
                # Spherical only supports RHOX
                depth = atmo["RHOX"]
                motype = "SPH"
            else:
                motype = atmo.depth
                depth = atmo[motype]

            ndepth = len(depth)
            t = atmo.temp
            xne = atmo.xne
            xna = atmo.xna
            rho = atmo.rho
            vt = np.full(ndepth, vturb) if np.size(vturb) == 1 else vturb
            wlstd = atmo.wlstd
            opflag = atmo.opflag
            args = [
                ndepth,
                teff,
                grav,
                wlstd,
                motype,
                opflag,
                depth,
                t,
                xne,
                xna,
                rho,
                vt,
            ]
            type = "sdddusdddddd"  # s : short, d: double, u: unicode (string)

            if atmo.geom == "SPH":
                radius = atmo.radius
                height = atmo.height
                motype = "SPH"
                args = args[:4] + [motype, radius] + args[5:] + [height]
                type = type[:4] + "ud" + type[5:] + "d"
        except AttributeError as ae:
            raise TypeError(f"atmo has to be an Atmo type, {ae}")

        logger.debug("Inputing atmosphere model to smelib")
        self.lib.InputModel(*args, type=type)

        self.teff = teff
        self.grav = grav
        self.vturb = vturb
        self.atmo = atmo

    def InputAbund(self, abund):
        """
        Pass abundances to radiative transfer code.

        Calculate elemental abundances from abundance pattern and metallicity.
        Metallicity adjustment is not applied to H or He.
        Renormalize abundances after applying metallicity.
        Introduced limiter in case the proposed step in abundance is too large.

        Parameters
        ---------
        abund : Abund
            abundance structure to be passed (see Abund for more details)
        """
        # Convert abundances to the right format
        # metallicity is included in the abundance class, ignored in function call
        abund = abund("sme", raw=True)
        assert isinstance(abund, np.ndarray)
        abund[np.isnan(abund)] = -99

        logger.debug("Inputing abundances to smelib")
        self.lib.InputAbund(abund, type="double")

        self.abund = abund

    def Opacity(self, getData=False, motype=1):
        """ Calculate opacities

        Parameters
        ---------
        getData : bool
            if True copblu and copred (and copstd) will be returned
            requires that radiative transfer was run
        motype : int
            if getData is True and motype is 0 then copstd will also be returned

        Returns
        -------
        copblu : array of size (nmu,)
            only if getData is True
        copred : array of size (nmu,)
            only if getData is True
        copstd : array of size (nmu,)
            only if getData is True and motype is 0
        """
        args = []
        type = ""
        if getData:
            nmu = self.nmu
            copblu = np.zeros(nmu)
            copred = np.zeros(nmu)
            args = [nmu, copblu, copred]
            type = ["s", "d", "d"]

            if motype == 0:
                copstd = np.zeros(nmu)
                args += [copstd]
                type += ["d"]

        self.lib.Opacity(*args, type=type)

        return args[1:]

    def GetOpacity(self, switch, species=None, key=None):
        """
        Returns specific cont. opacity, different output depending on the input

        Parameters
        ----------
        switch : int

            :-3: COPSTD
            :-2: COPRED
            :-1: COPBLU
            :0: AHYD,
            :1: AH2P
            :2: AHMIN
            :3: SIGH
            :4: AHE1
            :5: AHE2,
            :6: AHEMIN
            :7: SIGHE,
            :8: ACOOL, continuous opacity C1, Mg1, Al1, Si1, Fe1, CH, NH, OH,
            :9: ALUKE, continuous opacity N1, O1, Mg2, Si2, Ca2,
            :10: AHOT
            :11: SIGEL
            :12: SIGH2

        """
        length = self.nmu
        result = np.ones(length)
        args = [switch, length, result]
        type = ["s", "s", "d"]

        if switch == 8:
            if species is not None:
                if key is None:
                    raise AttributeError(
                        "Both species and key keywords need to be set with switch 8, continous opacity"
                    )
                else:
                    args += [species, key]
                    type += ["u", "u"]
        elif switch == 9:
            if species is not None:
                args += [species]
                type += ["u"]

        self.lib.GetOpacity(*args, type=type)
        return result

    def Ionization(self, ion=0):
        """
        Calculate ionization balance for current atmosphere and abundances.
        Ionization state is stored in the external library.
        Ion is a bit flag with values (add them together to use multiple):

        :1: adopt particle number densities from EOS
        :2: adopt electron number densities from EOS
        :4: adopt gas densities (g/cm^3) from EOS

        instead of using values from model atmosphere. Different abundance patterns
        in the model atmosphere (usually scaled solar) and SME (may be non-solar)
        can affect line shape, e.g. shape of hydrogen lines.

        Parameters
        ----------
        ion : int
            flag that determines the behaviour of the C function
        """
        logger.debug("Calculating ionization in smelib")
        self.lib.Ionization(ion, type="short", raise_error=False, raise_warning=True)
        self.ion = ion

    def GetDensity(self):
        """
        Retrieve density in each layer

        Returns
        -------
        density : array of size (ndepth,)
            Density of the atmosphere in each layer
        """
        length = self.ndepth
        array = np.zeros(length, dtype=float)
        self.lib.GetDensity(length, array, type="sd")
        return array

    def GetNatom(self):
        """
        Get XNA

        Returns
        -------
        XNA : array of size (ndepth,)
            XNA in each layer
        """
        length = self.ndepth
        array = np.zeros(length, dtype=float)
        self.lib.GetNatom(length, array, type="sd")
        return array

    def GetNelec(self):
        """
        Get XNE (Electron number density) for each layer in the atmosphere

        Returns
        -------
        XNE : array of size (ndepth,)
            XNE in each layer
        """
        length = self.ndepth
        array = np.zeros(length, dtype=float)
        self.lib.GetNelec(length, array, type="sd")
        return array

    def Transf(
        self,
        mu,
        accrt,
        accwi,
        keep_lineop=False,
        long_continuum=True,
        nwmax=400000,
        wave=None,
    ):
        """
        Radiative Transfer Calculation

        Perform the radiative transfer calculation thorugh the atmosphere
        Requires that all parameters have been set beforehand

        Parameters
        ---------
        mu : array of shape (nmu,)
            mu angles (1 - cos(phi)) of different limb points along the stellar surface
        accrt : float
            accuracy of the radiative transfer integration
        accwi : float
            accuracy of the interpolation on the wavelength grid
        keep_lineop : bool, optional
            if True do not recompute the line opacities (default: False)
        long_continuum : bool, optional
            if True the continuum is calculated at every wavelength (default: True)
        nwmax : int, optional
            maximum number of wavelength points if wavelength grid is not set with wave (default: 400000)
        wave : array, optional
            wavelength grid to use for the calculation,
            if not set will use an adaptive wavelength grid with no constant step size (default: None)

        Returns
        -------
        nw : int
            number of actual wavelength points, i.e. size of wint_seg
        wint_seg : array of shape (nwave,)
            wavelength grid, the number of wavelengthpoints is equal to the number of lines * 2 - 1
            One point in the center of each line + plus one between the next line
        sint_seg : array of shape (nmu, nwave)
            spectrum for each mu point
        cint_seg : array of shape (nmu, nwave)
            continuum for each mu point
        """
        keep_lineop = 1 if keep_lineop else 0
        long_continuum = 1 if long_continuum else 0

        if wave is None:
            nw = 0
            wint_seg = np.zeros(nwmax)
        else:
            nwmax = nw = len(wave)
            wint_seg = np.asarray(wave)

        mu = np.asarray(mu)
        nmu = np.size(mu)

        # Prepare data:
        sint_seg = np.zeros((nwmax, nmu))  # line+continuum intensities
        cint_seg = np.zeros((nwmax, nmu))  # all continuum intensities
        cintr_seg = np.zeros((nmu))  # red continuum intensity
        nw = np.array([nw])

        type = "sdddiiddddss"  # s: short, d:double, i:int, u:unicode (string)

        logger.debug("Starting radiative Transfer calculations in smelib")
        self.lib.Transf(
            nmu,
            mu,
            cint_seg,
            cintr_seg,
            nwmax,
            nw,
            wint_seg,
            sint_seg,
            accrt,
            accwi,
            keep_lineop,
            long_continuum,
            type=type,
        )
        nw = nw[0]

        wint_seg = wint_seg[:nw]
        sint_seg = sint_seg[:nw, :].T
        cint_seg = cint_seg[:nw, :].T

        sint_seg = np.nan_to_num(sint_seg, copy=False)
        cint_seg = np.nan_to_num(cint_seg, copy=False)

        self.nmu = nmu

        return nw, wint_seg, sint_seg, cint_seg

    def CentralDepth(self, mu, accrt):
        """
        This subroutine explicitly solves the transfer equation
        for a set of nodes on the star disk in the centers of spectral
        lines. The results are specific intensities.

        Parameters
        ----------
        mu : array of size (nmu,)
            mu values along the stellar disk to calculate
        accrt : float
            precision of the radiative transfer calculation

        Returns
        -------
        table : array of size (nlines,)
            Centeral depth (i.e. specific intensity) of each line
        """

        nmu = np.size(mu)
        nwsize = self.nlines
        table = np.zeros(nwsize)

        self.lib.CentralDepth(nmu, mu, nwsize, table, accrt, type="idifd")
        self.nmu = nmu

        return table

    def GetLineOpacity(self, wave):
        """
        Retrieve line opacity data from the C library

        Parameters
        ----------
        wave : float
            Wavelength of the line opacity to retrieve

        Returns
        ---------
        lop : array
            line opacity
        cop : array
            continuum opacity including scatter
        scr : array
            Scatter
        tsf : array
            Total source function
        csf : array
            Continuum source function
        """
        nmu = self.nmu
        lop = np.zeros(nmu)
        cop = np.zeros(nmu)
        scr = np.zeros(nmu)
        tsf = np.zeros(nmu)
        csf = np.zeros(nmu)
        type = "dsddddd"
        self.lib.GetLineOpacity(wave, nmu, lop, cop, scr, tsf, csf, type=type)
        return lop, cop, scr, tsf, csf

    def GetLineRange(self):
        """ Get the effective wavelength range for each line
        i.e. the wavelengths for which the line has significant impact

        Parameters
        ----------
        nlines : int
            number of lines in the linelist

        Returns
        -------
        linerange : array of size (nlines, 2)
            lower and upper wavelength for each spectral line
        """
        nlines = self.nlines
        linerange = np.zeros((nlines, 2))

        self.lib.GetLineRange(linerange, nlines, type=("double", "int"))

        return linerange

    def InputNLTE(self, bmat, lineindex):
        """
        Input NLTE departure coefficients

        Parameters
        ----------
        bmat : array of size (2, ndepth)
            departure coefficient matrix
        lineindex : float
            index of the line in the linelist
        """
        ndepth = self.ndepth
        nlines = self.nlines

        if not isinstance(bmat, (list, np.ndarray)):
            raise TypeError("Departure coefficient matrix is not an array")

        bmat = np.atleast_2d(bmat)
        if bmat.shape[1] != 2:
            raise ValueError(
                f"Departure coefficient matrix has the wrong shape, expected ({ndepth}, 2) but got {bmat.shape} instead"
            )
        if bmat.shape[0] != ndepth:
            raise ValueError(
                f"Departure coefficient matrix has the wrong shape, expected ({ndepth}, 2) but got {bmat.shape} instead"
            )

        if not isinstance(lineindex, (int, np.integer)):
            raise TypeError("Lineindex is not an integer type")

        if not 0 <= lineindex < nlines:
            raise ValueError(
                f"Lineindex out of range, expected value between 0 and {nlines}, but got {lineindex} instead"
            )

        self.lib.InputDepartureCoefficients(bmat, lineindex, type=("double", "int"))

    def GetNLTE(self, line):
        """ Get the NLTE departure coefficients as stored in the C library

        Parameters
        ----------
        line : int
            requested line index, i.e. between 0 and number of lines

        Returns
        -------
        bmat : array of size (2, nrhox)
            departure coefficients for the given line index
        """
        nrhox = self.ndepth

        bmat = np.full((2, nrhox), -1.0, dtype=float)
        self.lib.GetDepartureCoefficients(
            bmat, nrhox, line, type=("double", "int", "int")
        )
        return bmat

    def ResetNLTE(self):
        """ Reset departure coefficients from any previous call, to ensure LTE as default """
        self.lib.ResetDepartureCoefficients()

    def GetNLTEflags(self):
        """Get an array that tells us which lines have been used with NLTE correction

        Parameters
        ----------
        linelist : int
            number of lines

        Returns
        -------
        nlte_flags : array(bool) of size (nlines,)
            True if line was used with NLTE, False if line is only LTE
        """
        nlines = self.nlines
        nlte_flags = np.zeros(nlines, dtype=np.int16)

        self.lib.GetNLTEflags(nlte_flags, nlines, type=("short", "int"))

        return nlte_flags.astype(bool)
