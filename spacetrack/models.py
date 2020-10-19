from spacetrack.deserialize import FromDict, datetime, datetime_milli, date, boolean
from enum import Enum


class ObjectType(Enum):
    PAYLOAD = 1
    ROCKET_BODY = 2
    DEBRIS = 3
    UNKNOWN = 4
    OTHER = 5

    def from_string(x):
        return {
            "PAYLOAD": ObjectType.PAYLOAD,
            "ROCKET_BODY": ObjectType.ROCKET_BODY,
            "DEBRIS": ObjectType.DEBRIS,
            "UNKNOWN": ObjectType.UNKNOWN,
            "OTHER": ObjectType.OTHER
        }[x]


class ObjectSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

    def from_string(x):
        return {
            "SMALL": ObjectSize.SMALL,
            "MEDIUM": ObjectSize.MEDIUM,
            "LARGE": ObjectSize.LARGE
        }[x]


class Conjunction(FromDict):
    fields = [
        ("CDM_ID", "cdm_id", int),
        ("CREATION_DATE", "creation_date", datetime),
        ("EMERGENCY_REPORTABLE", "emergency_reportable", boolean),
        ("TCA", "tca", datetime_milli),
        ("MIN_RNG", "min_rng", float),
        ("PC", "pc", float),
        ("SAT_1_ID", "sat_1_id", int),
        ("SAT_1_NAME", "sat_1_name"),
        ("SAT1_OBJECT_TYPE", "sat1_object_type", ObjectType.from_string),
        ("SAT1_RCS", "sat1_rcs", ObjectSize.from_string),
        ("SAT_1_EXCL_VOL", "sat_1_excl_vol"),
        ("SAT_2_ID", "sat_2_id", int),
        ("SAT_2_NAME", "sat_2_name"),
        ("SAT2_OBJECT_TYPE", "sat2_object_type", ObjectType.from_string),
        ("SAT2_RCS", "sat2_rcs", ObjectSize.from_string),
        ("SAT_2_EXCL_VOL", "sat_2_excl_vol")
    ]


class Decay(FromDict):
    fields = [
        ("NORAD_CAT_ID", "norad_cat_id", int),
        ("OBJECT_NUMBER", "object_number", int),
        ("OBJECT_ID", "object_id"),
        ("OBJECT_NAME", "object_name"),
        ("INTLDES", "intldes"),
        ("RCS", "rcs", int),
        ("RCS_SIZE", "rcs_size", ObjectSize.from_string),
        ("COUNTRY", "country"),
        ("MSG_EPOCH", "msg_epoch", datetime),
        ("DECAY_EPOCH", "decay_epoch"),
        ("SOURCE", "source"),
        ("MSG_TYPE", "msg_type"),  # TODO
        ("PRECEDENCE", "precedence")
    ]


class Pertubations(FromDict):
    fields = [
        ("CCSDS_OMM_VERS", "ccsds_omm_vers"),
        ("COMMENT", "comment"),
        ("CREATION_DATE", "creation_date", datetime),
        ("ORIGINATOR", "originator"),
        ("OBJECT_NAME", "object_name"),
        ("OBJECT_ID", "object_id"),
        ("CENTER_NAME", "center_name"),
        ("REF_FRAME", "ref_frame"),
        ("TIME_SYSTEM", "time_system"),
        ("MEAN_ELEMENT_THEORY", "mean_element_theory"),
        ("EPOCH", "epoch", datetime_milli),
        ("MEAN_MOTION", "mean_motion", float),
        ("ECCENTRICITY", "eccentricity", float),
        ("INCLINATION", "inclination", float),
        ("RA_OF_ASC_NODE", "ra_of_asc_node", float),
        ("ARG_OF_PERICENTER", "arg_of_pericenter", float),
        ("MEAN_ANOMALY", "mean_anomaly", float),
        ("EPHEMERIS_TYPE", "ephemeris_type", int),
        ("CLASSIFICATION_TYPE", "classification_type"),
        ("NORAD_CAT_ID", "norad_cat_id", int),
        ("ELEMENT_SET_NO", "element_set_no", int),
        ("REV_AT_EPOCH", "rev_at_epoch", int),
        ("BSTAR", "bstar", float),
        ("MEAN_MOTION_DOT", "mean_motion_dot", float),
        ("MEAN_MOTION_DDOT", "mean_motion_ddot", float),
        ("SEMIMAJOR_AXIS", "semimajor_axis", float),
        ("PERIOD", "period", float),
        ("APOAPSIS", "apoapsis", float),
        ("PERIAPSIS", "periapsis", float),
        ("OBJECT_TYPE", "object_type", ObjectType.from_string),
        ("RCS_SIZE", "rcs_size", ObjectSize.from_string),
        ("COUNTRY_CODE", "country_code"),
        ("LAUNCH_DATE", "launch_date", date),
        ("SITE", "site"),
        ("DECAY_DATE", "decay_date", date),
        ("FILE", "file", int),
        ("GP_ID", "gp_id", int),
        ("TLE_LINE0", "tle_line0"),
        ("TLE_LINE1", "tle_line1"),
        ("TLE_LINE2", "tle_line2")
    ]


class Satellite(FromDict):
    fields = [
        ("INTLDES", "intldes"),
        ("NORAD_CAT_ID", "norad_cat_id", int),
        ("OBJECT_TYPE", "object_type", ObjectType.from_string),
        ("SATNAME", "satname"),
        ("COUNTRY", "country"),
        ("LAUNCH", "launch", date),
        ("SITE", "site"),
        ("DECAY", "decay", date),
        ("PERIOD", "period", float),
        ("INCLINATION", "inclination", float),
        ("APOGEE", "apogee", int),
        ("PERIGEE", "perigee", int),
        ("COMMENT", "comment"),
        ("COMMENTCODE", "commentcode"),
        ("RCSVALUE", "rcsvalue", int),
        ("RCS_SIZE", "rcs_size", ObjectSize.from_string),
        ("FILE", "file", int),
        ("LAUNCH_YEAR", "launch_year", int),
        ("LAUNCH_NUM", "launch_num", int),
        ("LAUNCH_PIECE", "launch_piece"),
        ("CURRENT", "current", boolean),
        ("OBJECT_NAME", "object_name"),
        ("OBJECT_ID", "object_id"),
        ("OBJECT_NUMBER", "object_number", int)
    ]


class Direction(Enum):
    ASCENDING = 1
    DESCENDING = 2

    def from_string(x):
        return {
            "ASCENDING": ObjectSize.ASCENDING,
            "DESCENDING": ObjectSize.DESCENDING
        }[x]


class TrackingInfo(FromDict):
    fields = [
        ("NORAD_CAT_ID", "norad_cat_id", int),
        ("MSG_EPOCH", "msg_epoch", datetime),
        ("INSERT_EPOCH", "insert_epoch", datetime),
        ("DECAY_EPOCH", "decay_epoch", datetime),
        ("WINDOW", "window", int),
        ("REV", "rev", int),
        ("DIRECTION", "direction", Direction.from_string),
        ("LAT", "lat", float),
        ("LON", "lon", float),
        ("INCL", "incl", float),
        ("NEXT_REPORT", "next_report", int),
        ("ID", "id", int),
        ("HIGH_INTEREST", "high_interest", boolean),
        ("OBJECT_NUMBER", "object_number", int)
    ]


OBJ_CLASS_TO_CLASS = {
    'cdm_public': Conjunction,
    'decay': Decay,
    'gp': Pertubations,
    'satcat': Satellite,
    'tip': TrackingInfo
}
