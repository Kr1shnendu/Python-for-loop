from controllers.controller import SignalController
from signals.city_signal import CitySignal
from signals.highway_signal import HighwaySignal
from app_logger import logger

logger.info(f"Traffic Simulation Started...")

controller = SignalController()
no_vehicle = int(input("Enter number of vehicle:"))

city_signal = CitySignal(no_vehicle)
highway_signal = HighwaySignal(no_vehicle)

controller.operate(city_signal)
controller.operate(highway_signal)

logger.info(f"Simulation completed...")