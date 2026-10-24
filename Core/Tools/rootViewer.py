import uproot
import pandas as pd
import awkward as ak
from pathlib import Path

def tree_merger(root_file: str | Path) -> pd.DataFrame | None:

    # Correctly match all keys that have a DF_ directory and end with '/O2dqmuoncandidate'
    with uproot.open(root_file) as file:
        valid_tree_paths = []
        for key in file.keys():
            clean_key = key.split(";")[0]
            if "DF_" in clean_key and clean_key.endswith("/O2dqmuoncandidate"):
                valid_tree_paths.append(f"{root_file}:{clean_key}")

    # De-duplicate paths if any exist
    valid_tree_paths = list(set(valid_tree_paths))

    print(f"Found {len(valid_tree_paths)} valid directories to merge")

    if len(valid_tree_paths) > 0:

        # Concatenate all valid trees into an Awkward Array
        array = uproot.concatenate(valid_tree_paths)

        # Convert to a Pandas DataFrame using the correct v2+ function
        df = ak.to_dataframe(array)

        return df
    else:
        print("No matching trees were found. Please verify the keys in your root file")