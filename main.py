import time

import plac

import config
from plc import PlcHandler


def main(debug: ('debug mode', 'flag'),
         headfull: ('make the browser visible', 'flag')):
    plc_handler = PlcHandler(debug=debug, headless=not headfull)
    plc_handler.login(url=config.PLC_URL,
                      username=config.PLC_USERNAME,
                      password=config.PLC_PASSWORD)
    plc_handler.stop()
    time.sleep(1)
    plc_handler.run()


if __name__ == '__main__':
    plac.call(main)
