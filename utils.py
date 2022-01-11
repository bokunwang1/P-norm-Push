import numpy as np
import pandas as pd

def load_magic_data():
    '''
    1.  fLength:  continuous  # major axis of ellipse [mm]
    2.  fWidth:   continuous  # minor axis of ellipse [mm]
    3.  fSize:    continuous  # 10-log of sum of content of all pixels [in #phot]
    4.  fConc:    continuous  # ratio of sum of two highest pixels over fSize  [ratio]
    5.  fConc1:   continuous  # ratio of highest pixel over fSize  [ratio]
    6.  fAsym:    continuous  # distance from highest pixel to center, projected onto major axis [mm]
    7.  fM3Long:  continuous  # 3rd root of third moment along major axis  [mm]
    8.  fM3Trans: continuous  # 3rd root of third moment along minor axis  [mm]
    9.  fAlpha:   continuous  # angle of major axis with vector to origin [deg]
    10.  fDist:    continuous  # distance from origin to center of ellipse [mm]
    11.  class:    g,h         # gamma (signal), hadron (background)
    '''

    Ynames = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
              'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'identity']

    featureNames = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym',
                    'fM3Long', 'fM3Trans', 'fAlpha', 'fDist']

    filepath = 'data/magic04.data'

    data = pd.read_csv(filepath, names=Ynames, header=None)

    data['identity'][data['identity'] == 'g'] = 1
    data['identity'][data['identity'] == 'h'] = 0

    X = data[featureNames].values
    Y = data['identity'].values.astype('int64')

    return (X, Y, Ynames)
