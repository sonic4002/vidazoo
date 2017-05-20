﻿FROM python:2
ADD roulette_game.py /
ENV TERM dumb
ENV TERM xterm-color
CMD ["python","./roulette_game.py"]