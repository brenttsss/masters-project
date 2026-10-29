# File: Histogram accessor
# Author: B. Suriah
# Date: 27 October 2026

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{siunitx}'

from .histogram_library import histograms
from .pdgcode_accessor import fetch_pdg_label

class HistogramAccessor:

    def __init__(self, 
                 df : pd.DataFrame, 
                 column : str, 
                 area_norm : bool = True, 
                 save : bool = False):

        self.df : pd.DataFrame = df
        self.column : str = column
        self.area_norm : bool = area_norm
        self.save : bool = save

        self.label = histograms[column].get("label")
        self.start = histograms[column].get("start")
        self.stop = histograms[column].get("stop")
        self.bins = histograms[column].get("bins")

    def fetch_column(self, column):
        return self.df[column]

    def make_bins(self, start : float, stop : float, bins : int) -> np.ndarray:
        return np.linspace(start, stop, bins + 1)

    def plot(self, save : bool | None = None):
        should_save = self.save if save is None else save

        values = self.fetch_column(self.column).dropna()

        figure, axis = plt.subplots()

        axis.hist(values, bins=self.make_bins(self.start, self.stop, self.bins), label="Background", density=self.area_norm)

        axis.set_xlabel(self.label)
        axis.set_xlim(left=self.start, right=self.stop)
        axis.set_ylabel("Density" if self.area_norm else "Entries")
        axis.legend()

        plt.show()

    def plot_pdgcodes(self, save : bool | None = None):
        should_save = self.save if save is None else save

        # Remove missing values and use the absolute PDG code
        pdg_codes = (self.fetch_column(self.column).dropna().abs().astype(int))

        # Count occurences of each absolute PDG code
        counts = pdg_codes.value_counts().sort_index()

        # Convert each PDG code into its LaTeX label
        labels = []
        for code in counts.index:
            label = fetch_pdg_label(code)

            # Fallback for codes not present in pdgcode_library
            labels.append(label if label is not None else rf"$\mathrm{{PDG}}\ {code}")

        figure, axis = plt.subplots()

        axis.bar(labels, counts.values)

        axis.set_xlabel(self.label)
        axis.set_ylabel("Entries")
        axis.set_yscale("log")

        # axis.tick_params(axis='x', rotation=45)

        plt.show()

if __name__ == "__main__":
    df = pd.read_csv("muon_table.csv")

    pt = HistogramAccessor(df=df, column="fMuonMotherPdgCode", area_norm=False, save=False)
