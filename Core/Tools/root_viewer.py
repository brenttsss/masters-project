import uproot
import pandas as pd
import awkward as ak
from pathlib import Path

def tree_merger(root_file: str | Path, all=False) -> pd.DataFrame | None:

    nKeys = 0

    # Correctly match all keys that have a DF_ directory and end with '/O2dqmuoncandidate'
    with uproot.open(root_file) as file:
        valid_tree_paths = []
        for key in file.keys():
            clean_key = key.split(";")[0]

            nKeys += 1

            if "DF_" in clean_key and clean_key.endswith("/O2dqmuoncandidate"):
                valid_tree_paths.append(f"{root_file}:{clean_key}")

    # De-duplicate paths if any exist
    valid_tree_paths = list(set(valid_tree_paths))

    print(f"Found {len(valid_tree_paths)} valid directories to merge")

    if len(valid_tree_paths) > 0:
        # Concatenate all valid trees into an Awkward Array
        array = uproot.concatenate(valid_tree_paths, allow_missing=True)

        # Convert to flattened table
        df_complete_muons = ak.to_dataframe(array)          # Save only muons with complete rows (i.e, no missing values)
        n_complete_muons = len(df_complete_muons)

        # Expose all muons (including muons with missing values)
        df_all_muons = ak.to_dataframe(array, how="outer")  # Save muons even with incomplete rows (i.e. missing values)
        n_all_muons = len(df_all_muons)

        print(f"Number of complete muons: {n_complete_muons} \n" +
              f"Number of all muons: {n_all_muons}")

        if all:
            return df_all_muons
        else:
            return df_complete_muons
    
    else:
        print("No matching trees were found. Please verify the keys in your root file!")


if __name__ == "__main__":

    # TESTING Only
    from pathlib import Path

    # Path to AnalysisResults_trees.root file ONLY
    test_file = Path("/Users/brentonsuriah/Desktop/AnalysisResults_trees.root")

    if test_file.exists():
        print(f"Running on test on {test_file}")
        df = tree_merger(str(test_file))

    else:
        print("Test ROOT file not found. Update path to test.")
