try:
    import geopandas
except ImportError:
    geopandas = None
from threedigrid_builder.base import OutputInterface
from threedigrid_builder.constants import CalculationType
from threedigrid_builder.constants import ContentType
from threedigrid_builder.constants import LineType
from threedigrid_builder.constants import NodeType

import numpy as np
import pygeos


__all__ = ["GeopackageOut"]


def _enum_to_str(arr, enum_type):
    result = np.full_like(arr, "", dtype=object)
    result[arr != -9999] = [enum_type(x).name for x in arr[arr != -9999]]
    return result


class GeopackageOut(OutputInterface):
    def __init__(self, path):
        if geopandas is None:
            raise ImportError("Cannot write to GPKG if geopandas is not available.")
        if not path.suffix.lower() == ".gpkg":
            raise ValueError("Extension should be .gpkg")
        super().__init__(path)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def write_nodes(self, nodes, epsg_code=None, **kwargs):
        """Write "nodes" and "cells" layers to a geopackage

        Args:
            nodes (Nodes)
            epsg_code (int)
        """
        node_data = nodes.to_dict()

        # construct points from nodes.coordinates
        node_geometries = np.empty(len(nodes), dtype=object)
        coordinates = node_data.pop("coordinates")
        has_coord = np.isfinite(coordinates).all(axis=1)
        node_geometries[has_coord] = pygeos.points(coordinates[has_coord])

        # construct cells from nodes.bounds
        bounds = node_data.pop("bounds")
        has_cell = np.isfinite(bounds).all(axis=1)
        cell_geometries = np.empty(len(nodes), dtype=object)
        cell_geometries[has_cell] = pygeos.box(*bounds[has_cell].T)

        # convert enums to strings
        node_data["node_type"] = _enum_to_str(node_data["node_type"], NodeType)
        node_data["content_type"] = _enum_to_str(node_data["content_type"], ContentType)
        node_data["calculation_type"] = _enum_to_str(
            node_data["calculation_type"], CalculationType
        )

        # Attribute data must only be 1D
        node_data.pop("pixel_coords")

        # construct the geodataframes
        df_nodes = geopandas.GeoDataFrame(
            node_data, geometry=node_geometries, crs=epsg_code
        )
        df_cells = geopandas.GeoDataFrame(
            node_data, geometry=cell_geometries, crs=epsg_code
        )

        df_nodes.to_file(self.path, layer="nodes", driver="GPKG")
        df_cells.to_file(self.path, layer="cells", driver="GPKG")

    def write_lines(self, lines, epsg_code=None, **kwargs):
        """Write "lines" layer to a geopackage

        Args:
            lines (Lines)
            epsg_code (int)
        """
        line_data = lines.to_dict()

        # convert enums to strings
        line_data["kcu"] = _enum_to_str(line_data["kcu"], LineType)
        line_data["content_type"] = _enum_to_str(line_data["content_type"], ContentType)

        # gpkg cannot deal with 2D arrays, cast lines.line to 2 1D arrays
        line_data["node_1"], line_data["node_2"] = line_data.pop("line").T
        line_data.pop("line_coords")
        line_data.pop("cross_pix_coords")

        # construct the geodataframe
        df_lines = geopandas.GeoDataFrame(
            line_data, geometry="line_geometries", crs=epsg_code
        )

        df_lines.to_file(self.path, layer="lines", driver="GPKG")
