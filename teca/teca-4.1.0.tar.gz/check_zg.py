import numpy as np

















# Earth radius is a function of latitude
#
# Re = sqrt( [ (Ree^2 * cos(B))^2 + (Rep^2 * sin(B))^2 ] / [ (Ree * cos(B))^2 + (Rep * sin(B))^2 ] )
#
# where:
#
# Ree = 6378.137 km (at equator)
# Rep = 6356.752 km (at pole)
# B = degrees latitude
# Re is in units of km.
def earth_radius_km(dlat):
    lat = np.pi * dlat / 180.0
    Ree = 6378.137
    Rep = 6356.752
    coslat = np.cos(lat)
    sinlat = np.sin(lat)
    a = Ree*Ree * coslat
    b = Rep*Rep * sinlat
    c = Ree * coslat
    d = Rep * sinlat
    Re = np.sqrt( (a*a + b*b) / ( c*c + d*d ) )
    return Re

def earth_radius_m(dlat):
    lat = np.pi * dlat / 180.0
    Ree = 6378137
    Rep = 6356752
    coslat = np.cos(lat)
    sinlat = np.sin(lat)
    a = Ree*Ree * coslat
    b = Rep*Rep * sinlat
    c = Ree * coslat
    d = Rep * sinlat
    Re = np.sqrt( (a*a + b*b) / ( c*c + d*d ) )
    return Re

def geopotential_height(dlat, altm):
    G = 6.67430e-11
    me = 5.9722e24
    g0 = -9.80665
    re = earth_radius_m(dlat)
    Z = G * me / g0 * (1.0 / (re + altm) - 1.0/re)
    return Z

def accel(dlat, altm):
    G = 6.67430e-11
    me = 5.9722e24
    re = earth_radius_m(dlat)
    r = re + altm
    g = -G*me / ( r*r )
    return g

def geopotential_height_const_re(altm):
    G = 6.67430e-11
    me = 5.9722e24
    g0 = -9.80665
    re = 6371001
    Z = G * me / g0 * (1.0 / (re + altm) - 1.0/re)
    return Z

def altitude(dlat, Z):
    G = 6.67430e-11
    me = 5.9722e24
    g0 = -9.80665
    re = earth_radius_m(dlat)
    a = -re*re*Z*g0 / (re*Z*g0 + G*me)
    return a


dlat = np.linspace(-90.0, 90, 13)
rekm = earth_radius_km(dlat)
rem = earth_radius_m(dlat)

print('earth radius')
print('============')
n = len(dlat)
i = 0
while i < n:
    print('%f = %g, %g'%(dlat[i], rekm[i], rem[i]/1000))
    i += 1
print('\n\n')

zm = np.array([0, 1e3, 10e3, 100e3, 500e3])
Z = geopotential_height(40.0, zm)
Zcre = geopotential_height_const_re(zm)
g = accel(40.0, zm)


print('geopotential')
print('============')
n = len(zm)
i = 0
while i < n:
    print('%f = %g, %g, %f'%(zm[i]/1e3, Z[i]/1e3, Zcre[i]/1e3, g[i]))
    i += 1
print('\n\n')


a = altitude(40.0, Z)
print('altitude')
print('========')
n = len(a)
i = 0
while i < n:
    print('%f, %g, %f'%(zm[i], Z[i], a[i]))
    i += 1



# Gravity as a function of altitude
#
# g(z) = G * me / r^2
#
# where:
#
# G = 6.67430 E-11 m^3 / kg / s (gravitational constant)
# me = 5.9722 E24 kg
# r = altitude from center of the Earth in meters
#   = Re(B) + z
#
#   where : B is degree's latitude.

