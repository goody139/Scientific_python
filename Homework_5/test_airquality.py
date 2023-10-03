from helpers import imports_of_your_file
import numpy as np

import matplotlib

try:

    import airquality as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'airquality.py'!"


PM2_5 = [18.750477001703594,4.290850694444449,7.578701754385964,23.04029017857141,5.575000000000003,6.142613430127046,24.347906137184115,4.255136054421766,2.3592294520547963,6.763707482993194,17.441925042589435,7.8656876061120515,4.883458262350943,3.099354838709676,12.299108391608401,12.355297297297287,7.349414802065403,8.200902777777776,9.527616487455193,19.51367346938777,28.537275985663083,17.024382608695667,25.466067019400356,37.53436115843268,30.074668930390505,19.151035653650247,5.117006920415226,8.956831345826249,10.469166666666666,14.039778911564628,18.4045183887916]

PM10 = [30.484940374787058,13.51687500000001,13.963789473684214,35.756160714285684,9.289980769230777,8.955226860254085,39.84241877256321,14.777517006802716,7.13246575342466,11.452585034013621,50.28444633730833,13.223904923599326,10.420749574105617,11.671629881154491,17.897045454545463,15.637441441441434,10.552512908777965,14.118993055555553,14.511254480286725,31.688554421768686,47.045985663082426,26.508991304347855,44.9462081128747,83.00008517887575,65.03293718166383,30.934974533106942,7.15019031141868,12.378057921635422,16.24758503401362,20.812721088435367,28.128266199649758]


def test_plot_airquality(filename="airquality", allowed_imports={"numpy", "matplotlib.pyplot", "helpers"}):
    """ Checks whether plots returned by plot_airquality have the correct attributes. """
    
    df = np.load('data/airdata.npy', allow_pickle=True)

    fig, ax1, ax2 = testfile.plot_airquality(df)

    # general checks
    assert isinstance(fig, matplotlib.figure.Figure), "The first returned variable should be a Figure!"
    assert isinstance(ax1, matplotlib.axes.Axes), "The second returned variable should be an Axes object!"
    assert isinstance(ax2, matplotlib.axes.Axes), "The third returned variable should be an Axes object!"

    # upper plot data checks
    assert len(ax1.lines) == 2, "You should plot exactly two lines in the upper plot!"
    assert np.allclose(PM2_5, ax1.lines[0].get_data()[1]) or np.allclose(PM2_5, ax1.lines[1].get_data()[1]),\
    "Neither line of the upper plot contains the correct PM2.5 data!"
    assert np.allclose(PM10, ax1.lines[0].get_data()[1]) or np.allclose(PM10, ax1.lines[1].get_data()[1]),\
    "Neither line of the upper plot contains the correct PM10 data!"

    # lower plot data checks
    assert len(ax2.containers) == 2, "You should have two barplots in the lower plot!"
    lower_ax_bars_a = [artist.get_height() for artist in ax2.containers[0]] 
    lower_ax_bars_b = [artist.get_height() for artist in ax2.containers[1]]
    assert np.allclose(PM2_5, lower_ax_bars_a) or np.allclose(PM2_5, lower_ax_bars_b),\
    "Neither barplot of the lower plot contains the correct PM2.5 data!"
    assert np.allclose(PM10, lower_ax_bars_a) or np.allclose(PM10, lower_ax_bars_b),\
    "Neither barplot of the lower plot contains the correct PM10 data!"

    # annotation and labeling 
    assert fig._suptitle.get_text() == "Fine dust concentration in Osnabrück (January 2019)", "The suptitle is not correct!"
    assert ax2.xaxis.label.get_text() == "Day", "The x-axis is supposed to enumerate the days of the month!"
    assert ax2.yaxis.label.get_text() == "Concentration", "The y-axis is supposed to measure the concentration of particles!"
    assert ax1.yaxis.label.get_text() == "Concentration", "The y-axis is supposed to measure the concentration of particles!"
    assert ax1._axes.yaxis._axes.title.get_text() == "Absolute fine dust concentration", "The title of the upper plot is not correct!"
    assert ax2._axes.yaxis._axes.title.get_text() == "Stacked PM2.5 and PM10", "The title of the lower plot is not correct!"
    assert ax1 in ax2.get_shared_x_axes().get_siblings(ax2), "The x-axis is not shared between plots!"
    assert ax1.legend_ is not None, "Your upper plot needs a legend!"    

    # imports check
    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are importing modules that are not allowed."

