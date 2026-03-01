from signals.base_signal import TrafficSignal
from app_logger import logger

from config import (
    CITY_HIGH_GREEN_TIME,
    CITY_LOW_GREEN_TIME,
    CITY_SIGNAL_TRAFFIC_LIMIT
)

class CitySignal(TrafficSignal):

    def green_time(self):
        logger.info(f"Calculating green time for City signal")
        if self._vehicle_count < CITY_SIGNAL_TRAFFIC_LIMIT:
            return CITY_LOW_GREEN_TIME
        return CITY_HIGH_GREEN_TIME
    
    def signal_type(self):
        return "City Signal"