from geojson import LineString, Polygon, MultiPolygon, Feature, FeatureCollection


class Data:
    def __init__(self, data, **kwargs) -> None:
        self.data = data
        self.x_size = len(self.data[0])
        self.y_size = len(self.data)
        self.pixel_size = 360 / self.x_size


def contours(contour, geojson_properties: dict = None):
    # Transform matplotlib.contour to geojson
    line_features = []
    for collection, level in zip(contour.collections, contour.levels):
        for path in collection.get_paths():
            coordinates = path.vertices
            if len(coordinates) < 3:
                continue
            line = LineString(coordinates.tolist())
            properties = {"level": level}
            if geojson_properties:
                properties.update(geojson_properties)
            line_features.append(Feature(geometry=line, properties=properties))
    return FeatureCollection(line_features)


def overlap_contourfs(contourf, geojson_properties: dict = None):
    # Transform matplotlib.contourf to geojson with overlapping filled contours
    polygon_features = []
    for collection, level in zip(contourf.collections, contourf.levels):
        for path in collection.get_paths():
            for coord in path.to_polygons():
                polygon = Polygon(coordinates=[coord.tolist()])
                properties = {"level": level}
                if geojson_properties:
                    properties.update(geojson_properties)
                feature = Feature(geometry=polygon, properties=properties)
                polygon_features.append(feature)
    return FeatureCollection(polygon_features)


def contourfs(contourf, geojson_properties: dict = None):
    # Transform matplotlib.contourf to geojson with MultiPolygons
    polygon_features = []
    for collection, level in zip(contourf.collections, contourf.levels):
        coords = []
        for path in collection.get_paths():
            polygon = [linestring.tolist() for linestring in path.to_polygons()]
            coords.append(polygon)
        polygon = MultiPolygon(coordinates=coords)
        properties = {"level": level}
        if geojson_properties:
            properties.update(geojson_properties)
        feature = Feature(geometry=polygon, properties=properties)
        polygon_features.append(feature)
    return FeatureCollection(polygon_features)
