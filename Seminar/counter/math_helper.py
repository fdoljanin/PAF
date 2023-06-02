import math

__all__ = ['time_to_jd', 'ra_dec_to_alt_az']


def unpack_datetime(date):
    return map(int, date.strftime(
        "%Y %m %d %H %M %S").split())


def time_to_jd(date):
    year, month, day, hour, minute, second = unpack_datetime(date)
    if month <= 2:
        year -= 1
        month += 12

    a = math.floor(year / 100)
    b = 2 - a + math.floor(a / 4)

    jd = math.floor(365.25 * (year + 4716)) + math.floor(
        30.6001 * (month + 1)) + day + b - 1524.5

    jd += (hour + minute / 60.0 + second / 3600.0) / 24.0

    return jd


def deg_to_rad(deg):
    return deg * math.pi / 180.0


def ra_dec_to_alt_az(star, location, jd_ut):
    ra, dec, lat, lon = map(
        deg_to_rad, (star.ra, star.dec, location.lat, location.lon))

    gmst = greenwich_mean_sidereal_time(jd_ut)
    local_sidereal_time = (gmst + lon) % (2 * math.pi)

    H = (local_sidereal_time - ra)
    if H < 0:
        H += 2 * math.pi
    if H > math.pi:
        H = H - 2 * math.pi

    az = math.atan2(math.sin(H), math.cos(
        H) * math.sin(lat) - math.tan(dec) * math.cos(lat))
    alt = math.asin(math.sin(lat) * math.sin(dec) +
                    math.cos(lat) * math.cos(dec) * math.cos(H))
    az -= math.pi

    if az < 0:
        az += 2 * math.pi
    return az, alt


def greenwich_mean_sidereal_time(jd):
    t = (jd - 2451545.0) / 36525.0

    gmst = earth_rotation_angle(jd) + (0.014506 + 4612.156534 * t + 1.3915817 * t**2 - 0.00000044 *
                                       t**3 - 0.000029956 * t**4 - 0.0000000368 * t**5) / 60.0 / 60.0 * math.pi / 180.0
    gmst %= 2 * math.pi
    if gmst < 0:
        gmst += 2 * math.pi

    return gmst


def earth_rotation_angle(jd):
    t = jd - 2451545.0
    f = jd % 1.0

    theta = 2 * math.pi * (f + 0.7790572732640 + 0.00273781191135448 * t)
    theta %= 2 * math.pi
    if theta < 0:
        theta += 2 * math.pi

    return theta
