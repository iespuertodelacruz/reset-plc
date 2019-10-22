import time

import config
from plc import PlcHandler

plc_handler = PlcHandler()
plc_handler.login(url=config.PLC_URL,
                  username=config.PLC_USERNAME,
                  password=config.PLC_PASSWORD)
plc_handler.stop()
time.sleep(1)
plc_handler.run()
