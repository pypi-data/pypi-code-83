"""Conversions Module
    """

def img_to_csv(folderpath, fname):
    """Create CSV file from image locations and attributes

    Args:
        folderpath (str): path to directory of images
        fname (str): output name
    """    
  
    import csv
    import pandas

    df = dict_to_df(folderpath)

    df.to_csv(fname, index=False)

    """
        with open('photos.csv', 'w', newline='') as file:
            fieldnames = ['filename', 'latdd', 'longdd']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
    """

def img_to_geojson(folderpath, fname):
    """Create GeoJSON from image locations and attributes

    Args:
        folderpath (str): Path to directory of images
        fname (string): Output filename
    """ 

    df = dict_to_df(folderpath)
    gdf = df_to_gdf(df)
    gdf.to_file(fname, driver='GeoJSON')

    print('{} geotagged images saved to GeoJSON file'.format(len(gdf['geometry'])))

def img_to_geopackage(folderpath, fname):
    """Geopackage file from image locations

    Args:
        folderpath (str): Path to directory of images
        fname (string): Output filename
    """ 
    df = dict_to_df(folderpath)
    gdf = df_to_gdf(df)
    gdf.to_file(fname, layer='images', driver='GPKG')

    print('{} geotagged images saved to GeoPackage file'.format(len(gdf['geometry'])))

def img_to_shp(folderpath, fname):
    """Create ESRI Shapefile from image locations and attributes

    Args:
        folderpath (str): Path to directory of images
        fname (string): Output filename
    """    
    df = dict_to_df(folderpath)
    for x in  df.select_dtypes(include=['datetime64']).columns.tolist(): df[x] = df[x].astype(str)
    gdf = df_to_gdf(df)

    gdf.to_file("imgs_shp.shp")

    print('{} geotagged images saved to shapefile'.format(len(gdf['geometry'])))

def img_to_kml(folderpath, fname):
    """Create KML file from image locations and attributes

    Args:
        folderpath (str): path to directory of images
        fname (str): output filename
    """    
    import fiona
    df = dict_to_df(folderpath)
    gdf = df_to_gdf(df)

    fiona.supported_drivers['KML'] = 'rw'
    gdf.to_file(fname, driver='KML')

    print('{} geotagged images saved to KML file'.format(len(gdf['geometry'])))

def imgdict(folderpath):
    """Creates dictionary of info from image EXIF data

    Args:
        folderpath (str): path to directory of images

    Returns:
        dict: dictionary of metadata for each image. See docs for schema.
    """    

    import os, exifread, datetime, uassist
    from exifread.utils import get_gps_coords

    masterdict = {}

    for filename in os.listdir(folderpath):
        if filename.endswith(".jpg") or filename.endswith(".JPG"): 
            filepath = folderpath + "/" + filename
            f = open(filepath, 'rb')
            tags = exifread.process_file(f, details=False)

            # GPS Altitude Values
            gpsaltval = [c.decimal() for c in tags["GPS GPSAltitude"].values]
            gpsalt = round(gpsaltval[0], 2)

            # GPS Coords
            gps = get_gps_coords(tags)
            latdd = round(gps[0], 7)
            longdd = round(gps[1], 7)

            xy = [latdd, longdd]
            #xyz = [latdd, longdd, gpsalt]

            # timestamps
            datetimestr = str(tags.get("Image DateTime"))
            datetimeobj = datetime.datetime.strptime(datetimestr, '%Y:%m:%d %H:%M:%S')
            
            # model
            make = str(tags["Image Make"])
            model = str(tags["Image Model"])
            makemodel = (make + " " + model)
            
            #image width and height
            imgh = str(tags.get("EXIF ExifImageLength"))
            imgw = str(tags.get("EXIF ExifImageWidth"))
            imghw = (imgw + " x " + imgh)

            masterdict[filename] = [filename, latdd, longdd, gpsalt, datetimeobj, makemodel, imghw, xy, filepath]
            
            continue
        else:
            continue

    return masterdict

def dict_to_df(folderpath):
    """Convert dictionary to Pandas Dataframe

    Args:
        folderpath (str): image directory path

    Returns:
        dataframe: a Pandas dataframe
    """    
    import pandas

    idict = imgdict(folderpath)

    cols = ['filename','latdd','longdd','altitude','datetime','makemodel','height_width','xy_pair','filepath']

    df = pandas.DataFrame.from_dict(idict, orient='index', columns=cols)

    return df

def df_to_gdf(df):
    """converts dataframe to geodataframe

    Args:
        df (dataframe): a pandas dataframe

    Returns:
        geodataframe: geopandas spatially enabled dataframe
    """    
    import geopandas

    gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.longdd, df.latdd))
    gdf = gdf.drop(columns=['xy_pair'])

    return gdf








