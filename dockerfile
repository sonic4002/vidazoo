﻿FROM python:2
ADD roulette_game.py /
ENV TERM dumb
CMD ["python","./roulette_game.py"]