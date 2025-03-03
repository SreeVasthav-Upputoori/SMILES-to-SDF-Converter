import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import SDWriter

def convert_smiles_to_sdf(input_excel, output_sdf):
    """Convert SMILES from an Excel file to a single SDF file."""
    df = pd.read_excel(input_excel, engine="openpyxl")
    df.columns = [col.strip().upper() for col in df.columns]
    
    name_col = next((col for col in df.columns if "NAMES" in col), None)
    smiles_col = next((col for col in df.columns if "SMILES" in col), None)

    if not name_col or not smiles_col:
        raise ValueError(f"Could not find 'NAMES' or 'SMILES' columns in {input_excel}.")

    smiles_list = df[[name_col, smiles_col]].dropna().values.tolist()
    writer = SDWriter(output_sdf)

    for name, smiles in smiles_list:
        mol = Chem.MolFromSmiles(str(smiles))
        if mol is None:
            print(f"Skipping invalid SMILES: {smiles}")
            continue

        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol, AllChem.ETKDG())
        mol.SetProp("_Name", str(name).strip())
        writer.write(mol)

    writer.close()
    print(f"SDF file saved: {output_sdf}")

if __name__ == "__main__":
    input_excel_file = "molecules.xlsx"
    output_sdf_file = "molecules.sdf"
    convert_smiles_to_sdf(input_excel_file, output_sdf_file)
