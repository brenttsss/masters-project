# File: Histogram library
# Author: B. Suriah
# Date: 27 October 2026

import numpy as np

histograms = {
    "fMuonMotherPdgCode" : {
        "label"     : r"Particle",
        "custom"    : True
    },

    "fMuonPt" : {
        "label"     : r"$p_\text{T}$",
        "start"     : 0.0,
        "stop"      : 20.0,
        "bins"      : 2000
    },

    "fMuonEta" : {
        "label"     : r"$\eta$ distribution",
        "start"     : -5.0,
        "stop"      : 5.0,
        "bins"      : 500
    },

    "fMuonPhi" : {
        "label"     : r"$\varphi$ distribution",
        "start"     : -2.0 * np.pi,
        "stop"      : 2.0 * np.pi,
        "bins"      : 500
    }
}