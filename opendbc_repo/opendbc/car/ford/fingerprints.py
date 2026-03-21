""" AUTO-FORMATTED USING opendbc/car/debug/format_fingerprints.py, EDIT STRUCTURE THERE."""
from opendbc.car.structs import CarParams
from opendbc.car.ford.values import CAR

Ecu = CarParams.Ecu

FW_VERSIONS = {
  CAR.F150: {
    (Ecu.engine, 0x7e0, None): [
      b'GL3A-14C204-JD\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KL3A-14C204-ND\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'FL3A-14C204-ABL\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'KL3A-14C337-DD\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    ],
  },
}
