from emerald_shapeutils.alignment import sample_single_channel_raster_file, generate_interpolation_points_geodataframe_from_gdf
import pyvista as pv
import numpy as np

def linear_slice_from_lines(geodataframe, tif, mesh, id_column):
    # Takes a geodataframe and returns the cross sections as a pyvista multiblock object
    gdf = geodataframe
    splines__ = {}

    for item, value in gdf.iterrows():
        coords = np.array(value.geometry.coords)
        gdf_x = coords[:, 0]
        gdf_y = coords[:, 1]

        if tif is not None:
            gdf_z = sample_single_channel_raster_file(tif, gdf_x, gdf_y, gdf.crs)
        elif coords.shape[1] > 2:
            gdf_z = coords[:, 2]
        else:
            gdf_z = np.full(len(coords), 0)

        points = np.c_[gdf_x, gdf_y, gdf_z]
        spline = pv.Spline(points)
        spline["scalars"] = gdf_z
        name = value[id_column]
        splines__.update({name: spline})
    slice_lines = pv.MultiBlock(splines__)

    cross_sections = pv.MultiBlock()
    for i in slice_lines:
        #fixme: Find way to clip the cross section by the line being sliced from.
        slice_ = mesh.slice_along_line(i)
        cross_sections.append(slice_)
    return cross_sections

def lines_to_vtk(gdf, target_crs, dtm, sample_dist, id_column, offset=0):
    """ To be used for getting for e.g. infrastructure from a geodataframe to 3D
        This works on single or multiline shapefiles, once opened as a geodataframe.
        Offset provides verticle offset, for e.g. setting powerlines to sit above the surface. """
    gdf = gdf
    gdf = gdf.to_crs(target_crs)

    gdf.loc[:, 'new_points'] = ''
    for i in gdf.index:
        gdf.at[i, 'new_points'] = generate_interpolation_points_geodataframe_from_gdf(
            gdf.loc[[i], [str(id_column), 'geometry']],
            sample_dist,
            dtm_tif=dtm,
            plot=True,
            xdist_shift=0)

    point_list = []
    for item, value in gdf.iterrows():
        idx = np.concatenate(([-1], np.where(value.new_points["topo"].isna())[0], [len(value.new_points)]))
        for idxidx in range(len(idx) - 1):
            startidx = idx[idxidx] + 1
            endidx = idx[idxidx + 1] - 1
            if startidx >= endidx:
                continue
            d = value.new_points.loc[startidx:endidx]
            if offset is not None:
                d["topo"] = d["topo"] + offset
            x = np.array(d["x"])
            y = np.array(d["y"])
            zo = np.array(d["topo"])
            points = np.c_[x, y, zo]
            line = lines_from_points(points)
            line["scalars"] = zo
            point_list.append(line)
    blocks = pv.MultiBlock(point_list)
    return blocks

def lines_from_points(points):
    """Given an array of points, make a line set"""
    poly = pv.PolyData()
    poly.points = points
    cells = np.full((len(points)-1, 3), 2, dtype=np.int_)
    cells[:, 1] = np.arange(0, len(points)-1, dtype=np.int_)
    cells[:, 2] = np.arange(1, len(points), dtype=np.int_)
    poly.lines = cells
    return poly