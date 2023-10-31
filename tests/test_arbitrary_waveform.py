"""
A Python module for radar simulation

---

- Copyright (C) 2018 - PRESENT  radarsimx.com
- E-mail: info@radarsimx.com
- Website: https://radarsimx.com

::

    ██████╗  █████╗ ██████╗  █████╗ ██████╗ ███████╗██╗███╗   ███╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██║████╗ ████║╚██╗██╔╝
    ██████╔╝███████║██║  ██║███████║██████╔╝███████╗██║██╔████╔██║ ╚███╔╝ 
    ██╔══██╗██╔══██║██║  ██║██╔══██║██╔══██╗╚════██║██║██║╚██╔╝██║ ██╔██╗ 
    ██║  ██║██║  ██║██████╔╝██║  ██║██║  ██║███████║██║██║ ╚═╝ ██║██╔╝ ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝

"""

from scipy import signal
import numpy as np
import numpy.testing as npt

from radarsimpy import Radar, Transmitter, Receiver
from radarsimpy.simulator import simc  # pylint: disable=no-name-in-module
from radarsimpy.processing import range_fft  # pylint: disable=no-name-in-module


def test_arbitrary_waveform_cpp():
    tx_channel = dict(
        location=(0, 0, 0),
    )

    freq_nonlinear = np.array(
        [
            2.40750000e10,
            2.40760901e10,
            2.40771786e10,
            2.40782654e10,
            2.40793506e10,
            2.40804341e10,
            2.40815161e10,
            2.40825964e10,
            2.40836750e10,
            2.40847521e10,
            2.40858275e10,
            2.40869012e10,
            2.40879734e10,
            2.40890439e10,
            2.40901127e10,
            2.40911800e10,
            2.40922456e10,
            2.40933096e10,
            2.40943719e10,
            2.40954326e10,
            2.40964917e10,
            2.40975491e10,
            2.40986049e10,
            2.40996591e10,
            2.41007117e10,
            2.41017626e10,
            2.41028119e10,
            2.41038595e10,
            2.41049055e10,
            2.41059499e10,
            2.41069927e10,
            2.41080338e10,
            2.41090733e10,
            2.41101111e10,
            2.41111473e10,
            2.41121819e10,
            2.41132149e10,
            2.41142462e10,
            2.41152759e10,
            2.41163039e10,
            2.41173304e10,
            2.41183552e10,
            2.41193783e10,
            2.41203999e10,
            2.41214198e10,
            2.41224380e10,
            2.41234546e10,
            2.41244696e10,
            2.41254830e10,
            2.41264947e10,
            2.41275048e10,
            2.41285133e10,
            2.41295202e10,
            2.41305254e10,
            2.41315289e10,
            2.41325309e10,
            2.41335312e10,
            2.41345298e10,
            2.41355269e10,
            2.41365223e10,
            2.41375161e10,
            2.41385082e10,
            2.41394987e10,
            2.41404876e10,
            2.41414748e10,
            2.41424605e10,
            2.41434444e10,
            2.41444268e10,
            2.41454075e10,
            2.41463866e10,
            2.41473640e10,
            2.41483399e10,
            2.41493140e10,
            2.41502866e10,
            2.41512575e10,
            2.41522268e10,
            2.41531945e10,
            2.41541605e10,
            2.41551249e10,
            2.41560876e10,
            2.41570488e10,
            2.41580083e10,
            2.41589661e10,
            2.41599224e10,
            2.41608770e10,
            2.41618299e10,
            2.41627812e10,
            2.41637309e10,
            2.41646790e10,
            2.41656254e10,
            2.41665702e10,
            2.41675134e10,
            2.41684550e10,
            2.41693949e10,
            2.41703331e10,
            2.41712698e10,
            2.41722048e10,
            2.41731381e10,
            2.41740699e10,
            2.41750000e10,
        ]
    )

    tx_nonlinear = Transmitter(
        f=freq_nonlinear,
        t=np.linspace(0, 80e-6, 100),
        tx_power=40,
        prp=100e-6,
        pulses=1,
        channels=[tx_channel],
    )

    rx_channel = dict(
        location=(0, 0, 0),
    )

    rx = Receiver(
        fs=2e6,
        noise_figure=12,
        rf_gain=20,
        load_resistor=500,
        baseband_gain=30,
        channels=[rx_channel],
    )

    radar_nonlinear = Radar(transmitter=tx_nonlinear, receiver=rx)

    target_1 = dict(location=(200, 0, 0), speed=(-5, 0, 0), rcs=20, phase=0)
    target_2 = dict(location=(95, 20, 0), speed=(-50, 0, 0), rcs=15, phase=0)
    target_3 = dict(location=(30, -5, 0), speed=(-22, 0, 0), rcs=5, phase=0)

    targets = [target_1, target_2, target_3]

    data_nonlinear = simc(radar_nonlinear, targets, noise=False)

    data_matrix_nonlinear = data_nonlinear["baseband"]

    range_window = signal.windows.chebwin(
        radar_nonlinear.sample_prop["samples_per_pulse"], at=60
    )

    range_profile_nonlinear = range_fft(data_matrix_nonlinear[:, :, :], range_window)

    range_profile = 20 * np.log10(np.abs(range_profile_nonlinear[0, 0, :]))

    npt.assert_allclose(
        range_profile,
        np.array(
            [
                -62.07849925,
                -62.20544263,
                -62.3609653,
                -62.52068991,
                -62.82363417,
                -63.09356487,
                -63.47789793,
                -64.18130834,
                -64.60987307,
                -66.02836818,
                -67.13391398,
                -70.23615273,
                -72.45375246,
                -70.23223916,
                -62.44448776,
                -55.28323117,
                -44.90115332,
                -29.81956035,
                -14.49433127,
                -2.98812246,
                1.51677569,
                -2.58718742,
                -13.81816558,
                -29.03688553,
                -44.14889749,
                -54.00768546,
                -60.09270676,
                -65.05351556,
                -69.6472799,
                -71.800232,
                -69.62770834,
                -68.94634515,
                -67.23959839,
                -66.4684642,
                -65.84670853,
                -65.18528611,
                -65.16536654,
                -64.42158345,
                -64.56269682,
                -64.21940498,
                -64.13403445,
                -63.96734378,
                -63.89617219,
                -63.92413024,
                -63.67429634,
                -63.79338911,
                -63.63722851,
                -63.5906069,
                -63.52304426,
                -63.44301377,
                -63.25882984,
                -62.97776338,
                -62.81673071,
                -62.29870445,
                -61.51990969,
                -60.17178873,
                -57.42435564,
                -52.11263294,
                -44.68573101,
                -36.52549748,
                -28.62836867,
                -21.75108895,
                -16.49123683,
                -13.25631776,
                -11.95225453,
                -12.47511286,
                -14.90360124,
                -19.33855372,
                -25.52285679,
                -33.04353452,
                -41.417082,
                -49.96591448,
                -57.38237831,
                -61.74431814,
                -63.67970419,
                -64.67236933,
                -65.60568643,
                -66.18370905,
                -67.04782568,
                -67.57896027,
                -67.45416173,
                -70.47643695,
                -68.39915052,
                -70.42200467,
                -70.77337434,
                -71.47014485,
                -72.1479753,
                -73.10817846,
                -73.42157313,
                -74.76747679,
                -74.98488992,
                -76.60993838,
                -76.86852787,
                -78.43480714,
                -78.86280941,
                -79.6829764,
                -81.03839696,
                -81.15559215,
                -81.15908901,
                -80.74672171,
                -80.91295929,
                -79.74260663,
                -78.73328366,
                -78.542396,
                -77.19543595,
                -76.88676823,
                -75.74101536,
                -75.42609875,
                -74.38697279,
                -74.391502,
                -73.31543608,
                -73.19368319,
                -72.73405164,
                -72.41793273,
                -72.0656123,
                -72.21822767,
                -71.98010131,
                -72.20412219,
                -73.42387124,
                -75.39698377,
                -83.62495715,
                -70.22757179,
                -60.84535869,
                -53.54270958,
                -47.15529457,
                -41.60347116,
                -36.94486216,
                -33.19081623,
                -30.1734301,
                -27.56615969,
                -25.41211038,
                -24.03246716,
                -23.01086849,
                -22.46216564,
                -22.46245021,
                -22.84614203,
                -23.71823433,
                -25.22794965,
                -26.95956288,
                -29.39757125,
                -32.74418113,
                -36.6561175,
                -40.81409585,
                -45.07456568,
                -49.43015643,
                -53.49715924,
                -56.91404228,
                -59.09205822,
                -60.32502533,
                -60.82214102,
                -61.18274026,
                -61.31916065,
                -61.41273532,
                -61.57555024,
                -61.63466541,
                -61.64666817,
                -61.73058582,
                -61.85520663,
                -61.81663542,
                -62.01865996,
            ]
        ),
        rtol=3,
    )
