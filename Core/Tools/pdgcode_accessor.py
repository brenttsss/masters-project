# File: PDG code library accessor
# Authour: B. Suriah
# 27 October 2026

from pdgcode_library import pdg_codes

def fetch_pdg_label(pdg_code):

    # Convert the code into a string
    code = str(abs(pdg_code))

    if code in pdg_codes:
        label = pdg_codes[code]["label"]
        return label
    else:
        print("No corresponding MC label found, returning none!")
        return None

if __name__ == "__main__":
    code = 200
    print(fetch_pdg_label(code))