import time

import plac

import config
from plc import PlcHandler


def main(debug: ('make the browser visible', 'flag', 'd')):
    plc_handler = PlcHandler(not debug)
    plc_handler.login(url=config.PLC_URL,
                      username=config.PLC_USERNAME,
                      password=config.PLC_PASSWORD)
    plc_handler.stop()
    time.sleep(1)
    plc_handler.run()


if __name__ == '__main__':
    plac.call(main)
