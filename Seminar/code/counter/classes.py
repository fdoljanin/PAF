class Star:
    def __init__(self, vmag, ra, dec):
        self.vmag = float(vmag)
        self.ra = float(ra)
        self.dec = float(dec)


class Location:
    def __init__(self, lat, lon):
        self.lat = float(lat)
        self.lon = float(lon)
