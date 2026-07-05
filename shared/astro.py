"""Minimal secular astrodynamics: J2 nodal regression, small-transfer dv.

Deliberately the simplest physics that can trip a gate (campaign spec):
secular J2 rates and impulsive two-burn transfers. No numerical propagation.
"""
import numpy as np

MU = 398600.4418      # km^3/s^2
RE = 6378.137         # km
J2 = 1.08262668e-3


def sma_from_mean_motion(rev_per_day):
    n = np.asarray(rev_per_day) * 2.0 * np.pi / 86400.0  # rad/s
    return (MU / n**2) ** (1.0 / 3.0)


def v_circ(a_km):
    return np.sqrt(MU / np.asarray(a_km))  # km/s


def raan_rate_deg_day(a_km, ecc, inc_deg):
    """Secular J2 nodal regression rate [deg/day]."""
    a = np.asarray(a_km, dtype=float)
    p = a * (1.0 - np.asarray(ecc) ** 2)
    n = np.sqrt(MU / a**3)  # rad/s
    rate = -1.5 * J2 * (RE / p) ** 2 * n * np.cos(np.radians(inc_deg))  # rad/s
    return np.degrees(rate) * 86400.0


def hohmann_dv_km_s(a1_km, a2_km):
    """Total two-burn coplanar circular-to-circular transfer dv [km/s]."""
    a1, a2 = np.asarray(a1_km, float), np.asarray(a2_km, float)
    at = 0.5 * (a1 + a2)
    dv1 = np.abs(np.sqrt(MU * (2.0 / a1 - 1.0 / at)) - np.sqrt(MU / a1))
    dv2 = np.abs(np.sqrt(MU / a2) - np.sqrt(MU * (2.0 / a2 - 1.0 / at)))
    return dv1 + dv2


def plane_change_dv_km_s(a_km, dinc_deg):
    return 2.0 * v_circ(a_km) * np.sin(np.radians(np.abs(dinc_deg)) / 2.0)


def deorbit_dv_km_s(a_km, perigee_alt_km=60.0):
    """One-burn dv from circular orbit to a reentry perigee [km/s]."""
    a = np.asarray(a_km, float)
    rp = RE + perigee_alt_km
    at = 0.5 * (a + rp)
    return np.abs(np.sqrt(MU / a) - np.sqrt(MU * (2.0 / a - 1.0 / at)))


def mean_projected_area_cylinder(length_m, diam_m):
    """Cauchy: mean projected area of a convex body = total surface / 4."""
    L, D = np.asarray(length_m, float), np.asarray(diam_m, float)
    surface = np.pi * D * L + 0.5 * np.pi * D**2
    return surface / 4.0  # m^2
