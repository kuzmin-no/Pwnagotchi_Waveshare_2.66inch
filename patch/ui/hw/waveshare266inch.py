import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class Waveshare266inch(DisplayImpl):
    def __init__(self, config):
        super(Waveshare266inch, self).__init__(config, 'waveshare266inch')
        self._display = None

    def layout(self):
        fonts.setup(10, 9, 10, 32, 25, 9)
        self._layout['width'] = 296
        self._layout['height'] = 152
        self._layout['face'] = (94, 22)
        self._layout['name'] = (5, 65)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (28, 0)
        self._layout['uptime'] = (230, 0)
        self._layout['line1'] = [0, 14, 296, 14]
        self._layout['line2'] = [0, 138, 296, 138]
        self._layout['friend_face'] = (150, 65)
        self._layout['friend_name'] = (190, 65)
        self._layout['shakes'] = (0, 140)
        self._layout['mode'] = (270, 140)
        self._layout['status'] = {
            'pos': (38, 80),
            'font': fonts.status_font(fonts.Medium),
            'max': 40
        }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare v1 2.66 inch display")
        from pwnagotchi.ui.hw.libs.waveshare.v266inch.epd2in66 import EPD
        self._display = EPD()
        self._display.init()
        self._display.Clear()

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.display(buf)

    def clear(self):
        self._display.Clear()
