# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xarray as xr
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import logging

from . import ptf

logger = logging.getLogger(__name__)

__all__ = ["soilgrids", "soilgrids_sediment"]

soildepth_cm = np.array([0.0, 5.0, 15.0, 30.0, 60.0, 100.0, 200.0])
soildepth_mm = 10.0 * soildepth_cm
M_minmax = 10000.0
nodata = -9999.0

# default z [cm] of soil layers wflow_sbm: 10, 40, 120, > 120
# mapping of wflow_sbm parameter c to soil layer SoilGrids
c_sl_index = [2, 4, 6, 7]


def average_soillayers(ds, soilthickness):

    """
    Determine weighted average of soil property at different depths over soil thickness,
    using the trapezoidal rule.
    See also: Hengl, T., Mendes de Jesus, J., Heuvelink, G. B. M., Ruiperez Gonzalez, M., Kilibarda,
    M., Blagotic, A., et al.: SoilGrids250m: Global gridded soil information based on machine learning,
    PLoS ONE, 12, https://doi.org/10.1371/journal.pone.0169748, 2017.

    Parameters
    ----------
    ds: xarray.Dataset
        Dataset containing soil property at each soil depth [sl1 - sl7].
    soilthickness : xarray.DataArray
        Dataset containing soil thickness [cm].

    Returns
    -------
    da_av : xarray.DataArray
        Dataset containing weighted average of soil property.

    """

    da_sum = soilthickness * 0.0
    # set NaN values to 0.0 (to avoid RuntimeWarning in comparison soildepth)
    d = soilthickness.fillna(0.0)

    for i in range(1, 7):

        da_sum = da_sum + (
            (soildepth_cm[i] - soildepth_cm[i - 1])
            * (ds["sl" + str(i)] + ds["sl" + str(i + 1)])
            * (d >= soildepth_cm[i])
            + (d - soildepth_cm[i - 1])
            * (ds["sl" + str(i)] + ds["sl" + str(i + 1)])
            * ((d < soildepth_cm[i]) & (d > soildepth_cm[i - 1]))
        )

    da_av = xr.apply_ufunc(
        lambda x, y: x * (1 / (y * 2)),
        da_sum,
        soilthickness,
        dask="parallelized",
        output_dtypes=[float],
    )

    da_av = da_av.raster.interpolate_na()

    return da_av


def thetas_layers(ds):

    """
    Determine saturated water content (thetaS) per soil layer based on PTF.

    Parameters
    ----------
    ds: xarray.Dataset
        Dataset containing soil properties at each soil depth [sl1 - sl7].

    Returns
    -------
    ds : xarray.Dataset
        Dataset containing thetaS [m3/m3] for each soil layer.

    """

    da_lst = []
    for l in range(1, 8):
        da = xr.apply_ufunc(
            ptf.thetas_toth,
            ds["ph_sl" + str(l)],
            ds["bd_sl" + str(l)],
            ds["clyppt_sl" + str(l)],
            ds["sltppt_sl" + str(l)],
            dask="parallelized",
            output_dtypes=[float],
        )
        da.name = "sl" + str(l)
        da_lst.append(da)
    ds = xr.merge(da_lst)
    return ds


def thetar_layers(ds):

    """
    Determine residual water content (thetaR) per soil layer depth based on PTF.

    Parameters
    ----------
    ds: xarray.Dataset
        Dataset containing soil properties at each soil depth [sl1 - sl7].

    Returns
    -------
    ds : xarray.Dataset
        Dataset containing thetaR [m3/m3] for each soil layer depth.

    """

    da_lst = []
    for l in range(1, 8):
        da = xr.apply_ufunc(
            ptf.thetar_toth,
            ds["oc_sl" + str(l)],
            ds["clyppt_sl" + str(l)],
            ds["sltppt_sl" + str(l)],
            dask="parallelized",
            output_dtypes=[float],
        )
        da.name = "sl" + str(l)
        da_lst.append(da)
    ds = xr.merge(da_lst)
    return ds


def pore_size_distrution_index_layers(ds, thetas):

    """
    Determine pore size distribution index per soil layer depth based on PTF.

    Parameters
    ----------
    ds: xarray.Dataset
        Dataset containing soil properties at each soil depth [sl1 - sl7].
    thetas: xarray.Dataset
        Dataset containing thetaS at each soil layer depth.

    Returns
    -------
    ds : xarray.Dataset
        Dataset containing pore size distribution index [-] for each soil layer
        depth.

    """

    da_lst = []
    for l in range(1, 8):
        da = xr.apply_ufunc(
            ptf.pore_size_index_brakensiek,
            ds["sndppt_sl" + str(l)],
            thetas["sl" + str(l)],
            ds["clyppt_sl" + str(l)],
            dask="parallelized",
            output_dtypes=[float],
        )
        da.name = "sl" + str(l)
        da = da.raster.interpolate_na()
        da_lst.append(da)
    ds = xr.merge(da_lst)
    return ds


def kv_layers(ds, thetas, ptf_name):

    """
    Determine vertical saturated hydraulic conductivity (KsatVer) per soil layer depth based on PTF.

    Parameters
    ----------
    ds: xarray.Dataset
        Dataset containing soil properties at each soil depth [sl1 - sl7].
    thetas: xarray.Dataset
        Dataset containing thetaS at each soil layer depth.
    ptf_name : str
        PTF to use for calculation KsatVer.

    Returns
    -------
    ds : xarray.Dataset
        Dataset containing KsatVer [mm/day] for each soil layer depth.
    """
    da_lst = []
    for l in range(1, 8):
        if ptf_name == "brakensiek":
            da = xr.apply_ufunc(
                ptf.kv_brakensiek,
                thetas["sl" + str(l)],
                ds["clyppt_sl" + str(l)],
                ds["sndppt_sl" + str(l)],
                dask="parallelized",
                output_dtypes=[float],
            )
        elif ptf_name == "cosby":
            da = xr.apply_ufunc(
                ptf.kv_cosby,
                ds["clyppt_sl" + str(l)],
                ds["sndppt_sl" + str(l)],
                dask="parallelized",
                output_dtypes=[float],
            )

        da.name = "kv"
        da = da.raster.interpolate_na()
        da_lst.append(da)
    ds = xr.concat(da_lst, pd.Index(soildepth_mm, name="z"))
    return ds


def func(x, b):
    return np.exp(-b * x)


def do_linalg(x, y):
    """
    Apply np.linalg.lstsq and return fitted parameter.

    Parameters
    ----------
    x : array_like (float)
        “Coefficient” matrix.
    y : array_like (float)
        dependent variable.

    Returns
    -------
    popt_0 : float
        Optimal value for the parameter fit.

    """
    idx = ~np.isinf(np.log(y))
    return np.linalg.lstsq(x[idx, np.newaxis], np.log(y[idx]), rcond=None)[0][0]


def do_curve_fit(x, y):
    """
    Apply scipy.optimize.curve_fit and return fitted parameter. If least-squares minimization
    fails with an inital guess p0 of 1e-3, and 1e-4, np.linalg.lstsq is used for curve fitting.

    Parameters
    ----------
    x : array_like of M length (float)
        independent variable.
    y : array_like of M length (float)
        dependent variable.

    Returns
    -------
    popt_0 : float
        Optimal value for the parameter fit.

    """
    idx = ~np.isinf(np.log(y))
    try:
        # try curve fitting with certain p0
        popt_0 = curve_fit(func, x[idx], y[idx], p0=(1e-3))[0]
    except RuntimeError:
        try:
            # try curve fitting with lower p0
            popt_0 = curve_fit(func, x[idx], y[idx], p0=(1e-4))[0]
        except RuntimeError:
            # do linalg  regression instead
            popt_0 = np.linalg.lstsq(x[idx, np.newaxis], np.log(y[idx]), rcond=None)[0][
                0
            ]
    return popt_0


def constrain_M(M, popt_0, M_minmax):
    """Constrain M parameter with the value M_minmax"""
    M = xr.where((M > 0) & (popt_0 == 0), M_minmax, M)
    M = xr.where(M > M_minmax, M_minmax, M)
    M = xr.where(M < 0, M_minmax, M)
    return M


def soilgrids(ds, ds_like, ptfKsatVer, logger=logger):

    """
    Returns soil parameter maps at model resolution based on soil properties from SoilGrids dataset.
    Ref: Hengl, T., Mendes de Jesus, J., Heuvelink, G. B. M., Ruiperez Gonzalez, M., Kilibarda, 
    M., Blagotic, A., et al.: SoilGrids250m: Global gridded soil information based on machine learning, 
    PLoS ONE, 12, https://doi.org/10.1371/journal.pone.0169748, 2017.

    The following soil parameter maps are calculated:\
    - thetaS            : average saturated soil water content [m3/m3]\
    - thetaR            : average residual water content [m3/m3]\
    - KsatVer           : vertical saturated hydraulic conductivity at soil surface [mm/day]\
    - SoilThickness     : soil thickness [mm]\
    - SoilMinThickness  : minimum soil thickness [mm] (equal to SoilThickness)\
    - M                 : model parameter [mm] that controls exponential decline of KsatVer with soil depth 
                         (fitted with curve_fit (scipy.optimize)), bounds of M are checked\
    - M_                : model parameter [mm] that controls exponential decline of KsatVer with soil depth 
                         (fitted with numpy linalg regression), bounds of M_ are checked\
    - M_original        : M without checking bounds\
    - M_original_       : M_ without checking bounds\
    - c_0               : Brooks Corey coefficient [-] based on pore size distribution index at depth
                          1st soil layer (100 mm) wflow_sbm\
    - c_1               : idem c_0 at depth 2nd soil layer (400 mm) wflow_sbm\
    - c_2               : idem c_0 at depth 3rd soil layer (1200 mm) wflow_sbm\
    - c_3               : idem c_0 at depth 4th soil layer (> 1200 mm) wflow_sbm\
    - KsatVer_[z]cm     : KsatVer [mm/day] at soil depths [z] of SoilGrids data [0.0, 5.0, 15.0, 30.0, 60.0, 100.0, 200.0]\
                
    
    Parameters
    ----------
    ds : xarray.Dataset
        Dataset containing soil properties.
    ds_like : xarray.DataArray
        Dataset at model resolution.
    ptfKsatVer : str
        PTF to use for calculcation KsatVer.

    Returns
    -------
    ds_out : xarray.Dataset
        Dataset containing gridded soil parameters.
    """

    ds_out = xr.Dataset(coords=ds_like.raster.coords)

    # set nodata values in dataset to NaN (based on soil property SLTPPT at first soil layer)
    ds = xr.where(ds["sltppt_sl1"] == ds["sltppt_sl1"].raster.nodata, np.nan, ds)

    logger.info("calculate and resample thetaS")
    thetas_sl = thetas_layers(ds)
    thetas = average_soillayers(thetas_sl, ds["soilthickness"])
    thetas = thetas.raster.reproject_like(ds_like, method="average")
    ds_out["thetaS"] = thetas.astype(np.float32)

    logger.info("calculate and resample thetaR")
    thetar_sl = thetar_layers(ds)
    thetar = average_soillayers(thetar_sl, ds["soilthickness"])
    thetar = thetar.raster.reproject_like(ds_like, method="average")
    ds_out["thetaR"] = thetar.astype(np.float32)

    soilthickness_hr = ds["soilthickness"].raster.interpolate_na()
    soilthickness = soilthickness_hr.raster.reproject_like(ds_like, method="average")
    # wflow_sbm cannot handle (yet) zero soil thickness
    soilthickness = xr.where(soilthickness == 0.0, np.nan, soilthickness)
    soilthickness = soilthickness.raster.interpolate_na()
    ds_out["SoilThickness"] = (
        soilthickness.astype(np.float32) * 10.0
    )  # from [cm] to [mm]
    ds_out["SoilMinThickness"] = xr.DataArray.copy(ds_out["SoilThickness"], deep=False)

    logger.info("calculate and resample KsatVer")
    kv_sl_hr = kv_layers(ds, thetas_sl, ptfKsatVer)
    kv_sl = xr.ufuncs.log(kv_sl_hr)
    kv_sl = kv_sl.raster.reproject_like(ds_like, method="average")
    kv_sl = xr.ufuncs.exp(kv_sl)

    logger.info("calculate and resample pore size distribution index")
    lambda_sl_hr = pore_size_distrution_index_layers(ds, thetas_sl)
    lambda_sl = xr.ufuncs.log(lambda_sl_hr)
    lambda_sl = lambda_sl.raster.reproject_like(ds_like, method="average")
    lambda_sl = xr.ufuncs.exp(lambda_sl)

    da_c = []
    for (i, sl_ind) in enumerate(c_sl_index):
        #        ds_out["c_" + str(i)] = 3.0 + (2.0 / lambda_sl["sl" + str(sl_ind)])
        #        da_c.append(ds_out["c_" + str(i)])
        da_c.append(3.0 + (2.0 / lambda_sl["sl" + str(sl_ind)]))
    # TO DO check -- should coordinate be linked to layer?
    #    da = xr.concat(da_c,'layer')
    da = xr.concat(
        da_c, pd.Index(np.arange(len(c_sl_index), dtype=int), name="layer")
    ).transpose("layer", ...)
    da.name = "c"
    ds_out["c"] = da

    ksatver = kv_sl[0]
    ds_out["KsatVer"] = ksatver.drop("z").astype(np.float32)

    for i in range(0, len(soildepth_cm)):
        kv = kv_sl[i].drop("z")
        ds_out["KsatVer_" + str(soildepth_cm[i]) + "cm"] = kv.astype(np.float32)

    kv = kv_sl / kv_sl[0]
    logger.info("fit z - log(KsatVer) with numpy linalg regression (y = b*x) -> M_")
    popt_0 = xr.apply_ufunc(
        do_linalg,
        soildepth_mm,
        kv,
        input_core_dims=[["z"], ["z"]],
        vectorize=True,
        output_dtypes=[float],
    )

    M_ = (thetas - thetar) / (-popt_0)
    ds_out["M_original_"] = M_.astype(np.float32)
    M_ = constrain_M(M_, popt_0, M_minmax)
    ds_out["M_"] = M_.astype(np.float32)

    logger.info("fit zi - Ksat with curve_fit (scipy.optimize) -> M")
    popt_0 = xr.apply_ufunc(
        do_curve_fit,
        kv.z,
        kv,
        input_core_dims=[["z"], ["z"]],
        vectorize=True,
        output_dtypes=[float],
    )

    M = (thetas - thetar) / (popt_0)
    ds_out["M_original"] = M.astype(np.float32)
    M = constrain_M(M, popt_0, M_minmax)
    ds_out["M"] = M.astype(np.float32)

    ds_out["f"] = popt_0.astype(np.float32)

    # wflow soil map is based on USDA soil classification
    soilmap = ds["tax_usda"].raster.interpolate_na()
    soilmap = soilmap.raster.reproject_like(ds_like, method="mode")
    ds_out["wflow_soil"] = soilmap.astype(np.float32)

    # for writing pcraster map files a scalar nodata value is required
    for var in ds_out:
        ds_out[var] = ds_out[var].fillna(nodata)
        ds_out[var].raster.set_nodata(nodata)

    return ds_out


def soilgrids_sediment(ds, ds_like, usleK_method, logger=logger):

    """
    Returns soil parameter maps for sediment modelling at model resolution based on soil properties\ 
    from SoilGrids dataset.

    The following soil parameter maps are calculated:\
        - PercentClay: clay content of the topsoil [%]\
        - PercentSilt: silt content of the topsoil [%]\
        - PercentOC: organic carbon in the topsoil [%]\
        - ErosK: mean detachability of the soil (Morgan et al., 1998) [g/J]\
        - USLE_K: soil erodibility factor from the USLE equation [-]\
    
    Parameters
    ----------
    ds : xarray.Dataset
        Dataset containing soil properties.
    ds_like : xarray.DataArray
        Dataset at model resolution.
    usleK_method : str
        Method to use for calculation of USLE_K {"renard", "epic"}.

    Returns
    -------
    ds_out : xarray.Dataset
        Dataset containing gridded soil parameters for sediment modelling.
    """

    ds_out = xr.Dataset(coords=ds_like.raster.coords)

    # set nodata values in dataset to NaN (based on soil property SLTPPT at first soil layer)
    ds = xr.where(ds["sltppt_sl1"] == ds["sltppt_sl1"].raster.nodata, np.nan, ds)

    # soil properties
    pclay = ds["clyppt_sl1"].raster.interpolate_na()
    percentclay = pclay.raster.reproject_like(ds_like, method="average")
    ds_out["PercentClay"] = percentclay.astype(np.float32)

    psilt = ds["sltppt_sl1"].raster.interpolate_na()
    percentsilt = psilt.raster.reproject_like(ds_like, method="average")
    ds_out["PercentSilt"] = percentsilt.astype(np.float32)

    poc = ds["oc_sl1"].raster.interpolate_na()
    percentoc = poc.raster.reproject_like(ds_like, method="average")
    ds_out["PercentOC"] = percentoc.astype(np.float32)

    # Detachability of the soil
    erosK = xr.apply_ufunc(
        ptf.ErosK_texture,
        pclay,
        psilt,
        dask="parallelized",
        output_dtypes=[float],
    )
    erosK = erosK.raster.reproject_like(ds_like, method="average")
    ds_out["ErosK"] = erosK.astype(np.float32)

    # USLE K parameter
    if usleK_method == "renard":
        usleK = xr.apply_ufunc(
            ptf.UsleK_Renard,
            pclay,
            psilt,
            dask="parallelized",
            output_dtypes=[float],
        )
    elif usleK_method == "epic":
        usleK = xr.apply_ufunc(
            ptf.UsleK_EPIC,
            pclay,
            psilt,
            dask="parallelized",
            output_dtypes=[float],
        )
    usleK = usleK.raster.reproject_like(ds_like, method="average")
    ds_out["USLE_K"] = usleK.astype(np.float32)

    # for writing pcraster map files a scalar nodata value is required
    for var in ds_out:
        ds_out[var] = ds_out[var].fillna(nodata)
        ds_out[var].raster.set_nodata(nodata)

    return ds_out
