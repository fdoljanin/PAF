from math_helper import *

__all__ = ['get_star_checker']


def is_observable(star, location, jd_time):
    az, alt = ra_dec_to_alt_az(star, location, jd_time)
    return alt > 0


def is_visible_by_eye(star):
    return star.vmag < 6.5


def get_checker(criteria):
    def checker(star):
        for criterion in criteria:
            if not criterion(star):
                return False
        return True

    return checker


def get_star_checker(location, time):
    jd_time = time_to_jd(time)

    def is_observable_local(star): return is_observable(
        star, location, jd_time)

    return get_checker([is_observable_local, is_visible_by_eye])
