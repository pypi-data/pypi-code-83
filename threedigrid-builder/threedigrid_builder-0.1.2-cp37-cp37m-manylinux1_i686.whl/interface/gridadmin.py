from threedigrid_builder.base import OutputInterface
from threedigrid_builder.constants import ContentType
from threedigrid_builder.constants import LineType
from threedigrid_builder.constants import NodeType

import numpy as np
import pygeos


try:
    import h5py
except ImportError:
    h5py = None

__all__ = ["GridAdminOut"]


NODE_TYPES_1D = (NodeType.NODE_1D_NO_STORAGE, NodeType.NODE_1D_STORAGE)

LINE_TYPES_1D = (
    LineType.LINE_1D_EMBEDDED,
    LineType.LINE_1D_ISOLATED,
    LineType.LINE_1D_CONNECTED,
    LineType.LINE_1D_LONG_CRESTED,
    LineType.LINE_1D_SHORT_CRESTED,
    LineType.LINE_1D_DOUBLE_CONNECTED,
)

LINE_TYPES_1D2D = (
    LineType.LINE_1D2D_SINGLE_CONNECTED_WITH_STORAGE,
    LineType.LINE_1D2D_SINGLE_CONNECTED_WITHOUT_STORAGE,
    LineType.LINE_1D2D_DOUBLE_CONNECTED_WITH_STORAGE,
    LineType.LINE_1D2D_DOUBLE_CONNECTED_WITHOUT_STORAGE,
    LineType.LINE_1D2D_POSSIBLE_BREACH,
    LineType.LINE_1D2D_ACTIVE_BREACH,
)

LINE_TYPES_1D2D_GW = (
    LineType.LINE_1D2D_GROUNDWATER_OPEN_WATER,
    LineType.LINE_1D2D_GROUNDWATER_SEWER,
)


class GridAdminOut(OutputInterface):
    def __init__(self, path):
        if h5py is None:
            raise ImportError("Cannot write to HDF5 if h5py is not available.")
        super().__init__(path)

    def __enter__(self):
        self._file = h5py.File(self.path, mode="w")
        return self

    def __exit__(self, *args, **kwargs):
        self._file.close()

    def write_grid_characteristics(self, nodes, lines, epsg_code):
        """Write the "attrs" of the gridadmin file.

        Args:
            nodes (Nodes)
            lines (Lines)
            epsg_code (int)

        Raises:
            ValueError if it exists already.
        """

        self._file.attrs.create("epsg_code", epsg_code, dtype="i4")

        is_1d = np.isin(nodes.node_type, NODE_TYPES_1D)
        if is_1d.any():
            extent_1d = np.array(
                [
                    np.amin(nodes.coordinates[is_1d, 0]),
                    np.amin(nodes.coordinates[is_1d, 1]),
                    np.amax(nodes.coordinates[is_1d, 0]),
                    np.amax(nodes.coordinates[is_1d, 1]),
                ]
            )
            self._file.attrs.create("extent_1d", extent_1d, dtype="i4")
            self._file.attrs.create("has_1d", 1, dtype="i4")
        else:
            self._file.attrs.create(
                "extent_1d", np.array([-9999.0, -9999.0, -9999.0, -9999.0])
            )
            self._file.attrs.create("has_1d", 0, dtype="i4")

        is_2d = nodes.node_type == NodeType.NODE_2D_OPEN_WATER
        if is_2d.any():
            extent_2d = np.array(
                [
                    np.amin(nodes.bounds[is_2d, 0]),
                    np.amin(nodes.bounds[is_2d, 1]),
                    np.amax(nodes.bounds[is_2d, 2]),
                    np.amax(nodes.bounds[is_2d, 3]),
                ]
            )
            self._file.attrs.create("extent_2d", extent_2d, dtype="i4")
            self._file.attrs.create("has_2d", 1, dtype="i4")
        else:
            self._file.attrs.create(
                "extent_2d", np.array([-9999.0, -9999.0, -9999.0, -9999.0])
            )
            self._file.attrs.create("has_2d", 0, dtype="i4")
        self._file.attrs.create("has_interception", 0, dtype="i4")
        self._file.attrs.create("has_pumpstations", 0, dtype="i4")
        self._file.attrs.create("has_simple_infiltration", 0, dtype="i4")
        self._file.attrs.create("model_name", b"...")
        self._file.attrs.create("model_slug", b"...")
        self._file.attrs.create("revision_hash", b"...")
        self._file.attrs.create("revision_nr", 0, dtype="i4")
        self._file.attrs.create("threedigrid_builder_version", 0, dtype="i4")

    def write_grid_counts(self, nodes, lines):
        """Write the "meta" group in the gridadmin file.

        Args:
            nodes (Nodes)
            lines (Lines)

        Raises:
            ValueError if it exists already.
        """
        group = self._file.create_group("meta")
        NODATA_YET = 0

        n2dtot = np.count_nonzero(nodes.node_type == NodeType.NODE_2D_OPEN_WATER)
        group.create_dataset("n2dtot", data=n2dtot, dtype="i4")
        group.create_dataset("n2dobc", data=NODATA_YET, dtype="i4")
        group.create_dataset("ngr2bc", data=NODATA_YET, dtype="i4")

        n1dtot = np.count_nonzero(np.isin(nodes.node_type, NODE_TYPES_1D))
        group.create_dataset("n1dtot", data=n1dtot, dtype="i4")
        group.create_dataset("n1dobc", data=NODATA_YET, dtype="i4")

        liutot = np.count_nonzero(lines.kcu == LineType.LINE_2D_U)
        group.create_dataset("liutot", data=liutot, dtype="i4")
        livtot = np.count_nonzero(lines.kcu == LineType.LINE_2D_V)
        group.create_dataset("livtot", data=livtot, dtype="i4")

        group.create_dataset("lgutot", data=NODATA_YET, dtype="i4")
        group.create_dataset("lgvtot", data=NODATA_YET, dtype="i4")

        l1dtot = np.count_nonzero(np.isin(lines.kcu, LINE_TYPES_1D))
        group.create_dataset("l1dtot", data=l1dtot, dtype="i4")

        infl1d = np.count_nonzero(np.isin(lines.kcu, LINE_TYPES_1D2D))
        group.create_dataset("infl1d", data=infl1d, dtype="i4")

        ingrw1d = np.count_nonzero(np.isin(lines.kcu, LINE_TYPES_1D2D_GW))
        group.create_dataset("ingrw1d", data=ingrw1d, dtype="i4")
        group.create_dataset("jap1d", data=NODATA_YET, dtype="i4")

    def write_quadtree(self, quadtree_statistics):
        """Write the "grid_coordinate_attributes" group in the gridadmin file.

        Args:
            quadtree (QuadTree)

        Raises:
            ValueError if it exists already.
        """

        group = self._file.create_group("grid_coordinate_attributes")
        for k, v in quadtree_statistics.items():
            group.create_dataset(k, data=v, dtype=get_dtype(v))

    def write_nodes(self, nodes, **kwargs):
        """Write the "nodes" group in the gridadmin file

        Raises a ValueError if it exists already.

        Notes:
            Some datasets were 64-bit integers, but now they are saved as 32-bit integers.
            The following datasets were added: code.
            For floats (double) we use NaN instead of -9999.0 to denote empty.

        Args:
            nodes (Nodes)
        """
        group = self._file.create_group("nodes")
        shape = (len(nodes),)

        # Some convenient masks:
        is_mh = nodes.content_type == ContentType.TYPE_V2_MANHOLE
        is_cn = is_mh | (nodes.content_type == ContentType.TYPE_V2_CONNECTION_NODES)
        is_2d = nodes.node_type == NodeType.NODE_2D_OPEN_WATER

        # Datasets that match directly to a nodes attribute:
        self.write_dataset(group, "id", nodes.id + 1)
        self.write_dataset(group, "code", nodes.code.astype("S32"), fill=b"")
        self.write_dataset(group, "display_name", nodes.code.astype("S64"), fill=b"")
        self.write_dataset(group, "node_type", nodes.node_type)
        self.write_dataset(group, "calculation_type", nodes.calculation_type)
        self.write_dataset(group, "coordinates", nodes.coordinates.T)
        self.write_dataset(group, "cell_coords", nodes.bounds.T)
        self.write_dataset(group, "nodk", nodes.nodk)
        self.write_dataset(group, "nodm", nodes.nodm)
        self.write_dataset(group, "nodn", nodes.nodn)
        self.write_dataset(group, "storage_area", nodes.storage_area)

        # content pk is only set for connection nodes, otherwise 0
        content_pk = np.full(len(nodes), 0, dtype="i4")
        content_pk[is_cn] = nodes.content_pk[is_cn]
        self.write_dataset(group, "content_pk", content_pk)
        # is_manhole is 1 for manholes, otherwise -9999
        is_manhole = is_mh.astype("i4")
        is_manhole[~is_mh] = -9999
        self.write_dataset(group, "is_manhole", is_manhole)

        # unclear what is the difference: seems bottom_level is for 1D, and z_coordinate
        # for 2D, but some nodes have both sets (then they are equal)
        # missing in gridadmin: dimp (bottom level groundwater)
        self.write_dataset(group, "bottom_level", nodes.dmax)
        self.write_dataset(group, "z_coordinate", nodes.dmax)

        # 2D stuff that is derived from 'bounds'
        pixel_width = np.full(len(nodes), -9999, dtype="i4")
        if is_2d.any():
            pixel_width[is_2d] = (
                nodes.pixel_coords[is_2d, 2] - nodes.pixel_coords[is_2d, 0]
            )

        self.write_dataset(group, "x_coordinate", nodes.coordinates[:, 0])
        self.write_dataset(group, "y_coordinate", nodes.coordinates[:, 1])
        self.write_dataset(group, "pixel_coords", nodes.pixel_coords.T)
        self.write_dataset(group, "pixel_width", pixel_width)

        # can be collected from SQLite, but empty for now:
        self.write_dataset(
            group, "zoom_category", np.full(len(nodes), -9999, dtype="i4")
        )
        self.write_dataset(
            group, "initial_waterlevel", np.full(shape, -9999, dtype=np.float64)
        )
        # (manhole specific:)
        self.write_dataset(
            group, "manhole_indicator", np.full(len(nodes), -9999, dtype="i4")
        )
        self.write_dataset(
            group, "shape", np.full(len(nodes), b"-999", dtype="S4"), fill=b""
        )
        self.write_dataset(
            group, "drain_level", np.full(shape, -9999, dtype=np.float64)
        )
        self.write_dataset(
            group, "surface_level", np.full(shape, -9999, dtype=np.float64)
        )
        self.write_dataset(group, "width", np.full(shape, -9999, dtype=np.float64))

        # unknown
        self.write_dataset(group, "sumax", np.full(shape, -9999, dtype=np.float64))

    def write_lines(self, lines, **kwargs):
        """Write the "lines" group in the gridadmin file

        Raises a ValueError if it exists already.

        Notes:
            Some datasets were 64-bit integers, but now they are saved as 32-bit integers.
            The following datasets were added: ds1d, dpumax, flod, flou, cross1, cross2,
            cross_weight
            For floats (double) we use NaN instead of -9999.0 to denote empty.

        Args:
            lines (Lines)
        """
        group = self._file.create_group("lines")
        shape = (len(lines),)
        fill_int = np.full(shape, -9999, dtype="i4")
        fill_float = np.full(shape, -9999, dtype=float)
        is_channel = lines.content_type == ContentType.TYPE_V2_CHANNEL

        l2d = np.isin(lines.kcu, (LineType.LINE_2D_U, LineType.LINE_2D_V))
        # Datasets that match directly to a lines attribute:
        self.write_dataset(group, "id", lines.id + 1)
        self.write_dataset(group, "code", lines.code.astype("S32"), fill=b"")
        self.write_dataset(
            group, "display_name", lines.display_name.astype("S64"), fill=b""
        )

        lines.kcu[l2d] = LineType.LINE_2D
        self.write_dataset(group, "kcu", lines.kcu)
        calculation_type = fill_int.copy()
        calculation_type[is_channel] = lines.kcu[is_channel] + 100
        self.write_dataset(group, "calculation_type", calculation_type)
        self.write_dataset(group, "line", lines.line.T + 1)
        self.write_dataset(group, "cross_pix_coords", lines.cross_pix_coords.T)
        self.write_dataset(group, "ds1d", lines.ds1d)
        self.write_dataset(group, "lik", lines.lik)
        self.write_dataset(group, "lim", lines.lim)
        self.write_dataset(group, "lin", lines.lin)

        content_type = np.full(len(lines), b"", dtype="S10")
        for ind in np.where(lines.content_type != -9999)[0]:
            content_type_name = ContentType(lines.content_type[ind]).name
            content_type[ind] = content_type_name.lstrip("TYPE_").lower()[:10]

        self.write_dataset(group, "content_type", content_type, fill=b"")
        self.write_dataset(group, "content_pk", lines.content_pk)
        self.write_dataset(group, "dpumax", lines.dpumax)
        self.write_dataset(group, "flod", lines.flod)
        self.write_dataset(group, "flou", lines.flou)
        self.write_dataset(group, "cross1", lines.cross1)
        self.write_dataset(group, "cross2", lines.cross2)
        self.write_dataset(group, "cross_weight", lines.cross_weight)
        self.write_dataset(group, "line_coords", lines.line_coords.T)
        self.write_dataset(
            group,
            "discharge_coefficient",
            lines.discharge_coefficient_positive,
        )
        self.write_dataset(
            group,
            "discharge_coefficient_negative",
            lines.discharge_coefficient_negative,
        )
        self.write_dataset(
            group,
            "discharge_coefficient_positive",
            lines.discharge_coefficient_positive,
        )

        # Transform an array of linestrings to list of coordinate arrays (x,y,x,y,...)
        coords = pygeos.get_coordinates(lines.line_geometries)
        end = np.cumsum(pygeos.get_num_coordinates(lines.line_geometries))
        start = np.roll(end, 1)
        start[0] = 0
        line_geometries = [coords[a:b].ravel() for a, b in zip(start, end)]
        line_geometries.insert(0, np.array([-9999.0, -9999.0]))
        # The dataset has a special "variable length" dtype. This one is special specific write method.
        vlen_dtype = h5py.special_dtype(vlen=np.dtype(float))
        group.create_dataset(
            "line_geometries",
            data=np.array(line_geometries, dtype=object),
            dtype=vlen_dtype,
        )

        # can be collected from SQLite, but empty for now:
        self.write_dataset(group, "connection_node_end_pk", fill_int)
        self.write_dataset(group, "connection_node_start_pk", fill_int)
        self.write_dataset(group, "crest_level", fill_float)
        self.write_dataset(group, "crest_type", fill_int)
        self.write_dataset(group, "cross_section_height", fill_int)
        self.write_dataset(group, "cross_section_shape", fill_int)
        self.write_dataset(group, "cross_section_width", fill_float)
        self.write_dataset(group, "dist_calc_points", fill_float)
        self.write_dataset(group, "friction_type", fill_int)
        self.write_dataset(group, "friction_value", fill_float)
        self.write_dataset(group, "invert_level_end_point", fill_float)
        self.write_dataset(group, "invert_level_start_point", fill_float)
        self.write_dataset(group, "material", fill_int)
        self.write_dataset(group, "sewerage", fill_int)
        self.write_dataset(group, "sewerage_type", fill_int)
        self.write_dataset(group, "zoom_category", fill_int)

    def write_dataset(self, group, name, values, fill=-9999):
        """Create the correct size dataset for writing to gridadmin.h5 and
        filling the extra indices with correct fillvalues.

        Args:
            group (hdf5 group): group to write to in hdf5 file.
            name (str): Name of dataset
            values (array): Values of dataset to write.
            fill: fillvalue with same dtype as values.
        """
        if values.ndim == 1:
            ds = group.create_dataset(
                name, (values.shape[0] + 1,), dtype=values.dtype, fillvalue=fill
            )
            ds[1:] = values
        elif values.ndim == 2:
            ds = group.create_dataset(
                name,
                (values.shape[0], values.shape[1] + 1),
                dtype=values.dtype,
                fillvalue=fill,
            )
            ds[:, 1:] = values
        else:
            ValueError("Too many dimensions for values.")


def get_dtype(value):
    """Return a numpy dtype based on input value.

    Args:
        value (ndarray, int, float, bool)
    """
    elem_type = type(value)
    if elem_type is np.ndarray:
        dtype = value.dtype
    elif elem_type is int:
        dtype = np.int32
    elif elem_type is float:
        dtype = np.float64
    elif elem_type is bool:
        dtype = bool
    else:
        dtype = object
    return dtype
