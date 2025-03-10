import torch as th

import util.plotter as plt
import util.sky as sky
from util.config import hnum, vnum

with th.no_grad():
    view = sky.skyview(0.0, 0.0, 0.0)
    plt.plot(
        open('zenith.png', 'wb'),
        view.reshape(1, hnum, vnum)
    )

    view = sky.skyview(0.0, 90.0, 0.0)
    plt.plot(
        open('polar.png', 'wb'),
        view.reshape(1, hnum, vnum)
    )

    view = sky.skyview(82.0, 0.0, 0.0)
    plt.plot(
        open('orion.png', 'wb'),
        view.reshape(1, hnum, vnum)
    )

    view = sky.skyview(248.0, -26.0, 0.0)
    plt.plot(
        open('scorpius.png', 'wb'),
        view.reshape(1, hnum, vnum)
    )

    view = sky.skyview(182.0, 58.0, 0.0)
    plt.plot(
        open('ursamajor.png', 'wb'),
        view.reshape(1, hnum, vnum)
    )
