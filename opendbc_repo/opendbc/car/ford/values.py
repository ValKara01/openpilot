from opendbc.car import dbc_dict
from collections import namedtuple
from cereal import car
from typing import Dict, List, Union
from opendbc.car.docs_definitions import CarInfo
from opendbc.car.fw_query_definitions import FwQueryConfig, Request, StdQueries
Ecu = car.CarParams.Ecu

AngleRateLimit = namedtuple('AngleRateLimit', ['speed_points', 'max_angle_diff_points'])
AngleLimit = namedtuple('AngleLimit', ['speed_points', 'max_angle_points'])

class CarControllerParams:

  # These rate limits are also enforced by the Panda safety code.
  RATE_LIMIT_UP = AngleRateLimit(speed_points=[0., 5., 15.], max_angle_diff_points=[7.5, 1.2, .225])
  RATE_LIMIT_DOWN = AngleRateLimit(speed_points=[0., 5., 15.], max_angle_diff_points=[7.5, 5.25, 0.6])

  APA_STEP = 2 # 50hz
  # Angle limits
  
  ANGLE_LIMIT = AngleLimit(speed_points=[0., 5., 15.], max_angle_points=[180., 90., 45.])

class CAR:
  F150 = 'F150'

CAR_INFO: Dict[str, Union[CarInfo, List[CarInfo]]] = {
  CAR.F150: CarInfo("Ford F150", "All"),
}


DBC = {
  CAR.F150: dbc_dict('ford_f150'),
}

FW_QUERY_CONFIG = FwQueryConfig(
  requests=[
    Request(
      [StdQueries.MANUFACTURER_SOFTWARE_VERSION_REQUEST],
      [StdQueries.MANUFACTURER_SOFTWARE_VERSION_RESPONSE],
      bus=0,
    ),
    Request(
      [StdQueries.TESTER_PRESENT_REQUEST, StdQueries.MANUFACTURER_SOFTWARE_VERSION_REQUEST],
      [StdQueries.TESTER_PRESENT_RESPONSE, StdQueries.MANUFACTURER_SOFTWARE_VERSION_RESPONSE],
      bus=0,
    ),
    Request(
      [StdQueries.MANUFACTURER_SOFTWARE_VERSION_REQUEST],
      [StdQueries.MANUFACTURER_SOFTWARE_VERSION_RESPONSE],
    ),
    Request(
      [StdQueries.TESTER_PRESENT_REQUEST, StdQueries.MANUFACTURER_SOFTWARE_VERSION_REQUEST],
      [StdQueries.TESTER_PRESENT_RESPONSE, StdQueries.MANUFACTURER_SOFTWARE_VERSION_RESPONSE],
    ),
    Request(
      [StdQueries.MANUFACTURER_SOFTWARE_VERSION_REQUEST],
      [StdQueries.MANUFACTURER_SOFTWARE_VERSION_RESPONSE],
      bus=4,
    ),
    Request(
      [StdQueries.TESTER_PRESENT_REQUEST, StdQueries.MANUFACTURER_SOFTWARE_VERSION_REQUEST],
      [StdQueries.TESTER_PRESENT_RESPONSE, StdQueries.MANUFACTURER_SOFTWARE_VERSION_RESPONSE],
      bus=4,
    ),
  ],
)
