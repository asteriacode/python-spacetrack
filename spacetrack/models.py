from spacetrack.deserialize import FromDict, datetime
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
        ("CDM_ID", "id", int),
        ("CREATION_DATE"),
        ("EMERGENCY_REPORTABLE", "is_emergency_reportable", lambda x: x == "Y"),
        ("TCA", "tca", datetime),
        ("MIN_RNG", "min_rng", float),
        ("PC", "pc", float),
        ("SAT_1_ID", "sat1_id", int),
        ("SAT_1_NAME", "sat1_name"),
        ("SAT1_OBJECT_TYPE", "sat1_type", ObjectType.from_string),
        ("SAT1_RCS", "sat1_rcs", ObjectSize.from_string),
        ("SAT_1_EXCL_VOL", "sat1_excl_vol"),
        ("SAT_2_ID", "sat1_id", int),
        ("SAT_2_NAME", "sat1_name"),
        ("SAT2_OBJECT_TYPE", "sat1_type", ObjectType.from_string),
        ("SAT2_RCS", "sat1_rcs", ObjectSize.from_string),
        ("SAT_2_EXCL_VOL", "sat1_excl_vol")
    ]

class Decay(FromDict):
    fields = [
        ("NORAD_CAT_ID", "norad_cat_id", int),
        ("OBJECT_NUMBER", "obj_number", int),
        ("OBJECT_ID", "obj_id"),
        ("OBJECT_NAME", "obj_name"),
        ("INTLDES", "intldes"),
        ("RCS", "rcs", int),
        ("RCS_SIZE", "rcs_size", ObjectSize.from_string),
        ("COUNTRY", "country"),
        ("MSG_EPOCH", "msg_epoch", datetime),
        ("DECAY_EPOCH", "decay_epoch"),
        ("SOURCE", "source"),
        ("MSG_TYPE", "msg_type"), # TODO
        ("PRECEDENCE", "precedence")
    ]

OBJ_CLASS_TO_CLASS = {
    'cdm_public': Conjunction,
    'decay': Decay
}