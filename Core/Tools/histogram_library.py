# File: Histogram library
# Author: B. Suriah
# Date: 27 October 2026

import numpy as np

histograms = {
    "MuonMotherPdgCode" : {
        "column"    : "fMuonMotherPdgCode",
        "label"     : r"Particle",
        "custom"    : True
    },

    "MuonPt" : {
        "column"    : "fMuonPt",
        "label"     : r"$p_\text{T}$",
        "start"     : 0.0,
        "stop"      : 20.0,
        "bins"      : 2000
    },

    "MuonEta" : {
        "column"    : "fMuonEta",
        "label"     : r"$\eta$ distribution",
        "start"     : -5.0,
        "stop"      : 5.0,
        "bins"      : 500
    },

    "MuonPhi" : {
        "column"    : "fMuonPhi",
        "label"     : r"$\varphi$ distribution",
        "start"     : -2.0 * np.pi,
        "stop"      : 2.0 * np.pi,
        "bins"      : 500
    },

    "MuonFwdDcaX" : {
        "column"    : "fMuonFwdDcaX",
        "label"     : "Muon DcaX",
        "bins"      : 2000,
        "start"     : -20,
        "stop"      : 20
    },

    "MuonFwdDcaY" : {
        "column"    : "fMuonFwdDcaY",
        "label"     : "Muon DcaY",
        "bins"      : 2000,
        "start"     : -20,
        "stop"      : 20
    },

    "MuonDcaX_vs_phi" : {
        "axis_1" : {
            "column"    : "fMuonDcaX",
            "label"     : "Muon DcaX",
            "bins"      : 2000,
            "start"     : -20,
            "stop"      : 20
        },

        "axis_2" : {
            "column"    : "fMuonPhi",
            "label"     : r"$\varphi$",
            "bins"      : 200,
            "start"     : -2 * np.pi,
            "stop"      : 2 * np.pi
        }
    },

    "MuonDcaY_vs_phi" : {
        "axis_1" : {
            "column"    : "fMuonDcaY",
            "label"     : "Muon DcaY",
            "bins"      : 2000,
            "start"     : -20,
            "stop"      : 20
        },

        "axis_2" : {
            "column"    : "fMuonPhi",
            "label"     : r"$\varphi$",
            "bins"      : 200,
            "start"     : -2 * np.pi,
            "stop"      : 2 * np.pi
        }
    },

    "MuonDcaX_vs_eta" : {
        "axis_1" : {
            "column"    : "fMuonDcaX",
            "label"     : "Muon DcaX",
            "bins"      : 2000,
            "start"     : -20,
            "stop"      : 20
        },

        "axis_2" : {
            "column"    : "fMuonEta",
            "label"     : r"$\eta",
            "bins"      : 500,
            "start"     : -5.0,
            "stop"      : 5.0
        }
    },

    "MuonDcaY_vs_eta" : {
        "axis_1" : {
            "column"    : "fMuonDcaY",
            "label"     : "Muon DcaY",
            "bins"      : 2000,
            "start"     : -20,
            "stop"      : 20
        },

        "axis_2" : {
            "column"    : "fMuonEta",
            "label"     : r"$\eta",
            "bins"      : 500,
            "start"     : -5.0,
            "stop"      : 5.0
        }
    },

    "MuonPx" : {},

    "MuonPy": {},

    "MuonPz" : {},

    "MuonP" : {
        "column"    : "fMuonP",
        "label"     : r"$p$",
        "bins"      : 200,
        "start"     : 0.0,
        "stop"      : 20.0
    },

    "MuonNClusters" : {},

    "MuonPDca" : {
        "column"    : "fMuonPDca",
        "label"     : r"$p\cdot\text{{DCA}}$",
        "bins"      : 2000,
        "start"     : 0.0,
        "stop"      : 20.0
    },

    "pdca_vs_p" : {
        "axis_1" : {
            "column"    : "fMuonP",
            "label"     : r"$p$",
            "bins"      : 2000,
            "start"     : 0.0,
            "stop"      : 20.0
        },

        "axis_2" : {
            "column"    : "fMuonPDca",
            "label"     : r"$p\cdot\text{{DCA}}$",
            "bins"      : 200,
            "start"     : 0.0,
            "stop"      : 1000.0
        }
    },

    "pdca_vs_pt" : {
        "axis_1" : {
            "column"    : "fMuonPt",
            "label"     : r"$p$",
            "bins"      : 2000,
            "start"     : 0.0,
            "stop"      : 20.0
        },

        "axis_2" : {
            "column"    : "fMuonPDca",
            "label"     : r"$p\cdot\text{{DCA}}$",
            "bins"      : 200,
            "start"     : 0.0,
            "stop"      : 1000.0
        }
    },

    "pdca_vs_Rabs" : {
        "axis_1" : {
            "column"    : "fMuonRAtAbsorberEnd",
            "label"     : r"$p$",
            "bins"      : 100,
            "start"     : 0.0,
            "stop"      : 200.0
        },

        "axis_2" : {
            "column"    : "fMuonPDca",
            "label"     : r"$p\cdot\text{{DCA}}$",
            "bins"      : 200,
            "start"     : 0.0,
            "stop"      : 1000.0
        }
    },

    "MuonRAtAbsorberEnd" : {
        "column"    : "fMuonRAtAbsorberEnd",
        "label"     : r"$R_\text{{abs}}$",
        "bins"      : 100,
        "start"     : 0.0,
        "stop"      : 200.0
    },

    "MuonChi2" : {
        "column"    : "fMuonChi2",
        "label"     : r"$Chi2$",
        "bins"      : 100,
        "start"     : 0.0,
        "stop"      : 200.0
    },

    "MuonChi2MatchMCHMID" : {
        "column"    : "fMuonChi2MatchMCHMID",
        "label"     : r"$Chi2MCHMID$",
        "bins"      : 100,
        "start"     : 0.0,
        "stop"      : 200.0
    },

    "MuonChi2MatchMCHMFT" : {
        "column"    : "fMuonChi2MatchMCHMFT",
        "label"     : r"$Chi2MCHMFT$",
        "bins"      : 100,
        "start"     : 0.0,
        "stop"      : 200.0
    },

    "MuonMatchScoreMCHMFT" : {
        "column"    : "fMuonMatchScoreMCHMFT",
        "label"     : r"$Chi2MCHMFT$",
        "bins"      : 100,
        "start"     : 0.0,
        "stop"      : 200.0
    },

    "MuonTrackTime" : {
        "column"    : "fMuonTrackTime",
        "label"     : r"Time",
        "bins"      : 100,
        "start"     : -1.0,
        "stop"      : 1.0
    },

    "MuonTrackTimeRes" : {
        "column"    : "fMuonTrackTimeRes",
        "label"     : r"Time resolution",
        "bins"      : 100,
        "start"     : -1.0,
        "stop"      : 1.0
    },

    "MftPt" : {
        "column"    : "fMFTPt",
        "label"     : r"$p_\text{T}$",
        "start"     : 0.0,
        "stop"      : 20.0,
        "bins"      : 2000
    },

    "MftEta" : {
        "column"    : "fMFTEta",
        "label"     : r"$\eta$ distribution",
        "start"     : -5.0,
        "stop"      : 5.0,
        "bins"      : 500
    },

    "fMftPhi" : {
        "column"    : "fMFTPhi",
        "label"     : r"$\varphi$ distribution",
        "start"     : -2.0 * np.pi,
        "stop"      : 2.0 * np.pi,
        "bins"      : 500
    },

    "fMftTrackEtaVsPt" : {
        "axis_1" : {
            "column"    : "fMFTEta",
            "label"     : r"MFT $\eta$",
            "bins"      : 100,
            "start"     : -0.5,
            "stop"      : 15.5
        },
        "axis_2" : {
            "column"    : "fMFTPt",
            "label"     : r"MFT $p_\text{{T}}$",
            "bins"      : 100,
            "start"     : 0.0,
            "stop"      : 20.0
        }
    },

    "MftNClusters" : {
        "column"    : "fMftNClusters",
        "label"     : "MFT N Clusters",
        "bins"      : 16,
        "start"     : -0.5,
        "stop"      : 15.5
    },

    "MftClusterSize" : {
        "column"    : "fMftClusterSize",
        "label"     : "MFT Cluster Size",
        "bins"      : 101,
        "start"     : -0.5,
        "stop"      : 100.5
    },

    "MftMeanClusterSize" : {
        "column"    : "fMftMeanClusterSize",
        "label"     : "MFT Mean Cluster Size",
        "bins"      : 200,
        "start"     : 0,
        "stop"      : 20
    }
}