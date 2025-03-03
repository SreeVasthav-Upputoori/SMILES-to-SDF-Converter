# SMILES to SDF Converter

This project converts SMILES strings from an Excel file into an SDF file using RDKit. It is useful for cheminformatics workflows where molecular structures need to be converted into 3D representations.

## Features
- Reads an Excel file with 'NAMES' and 'SMILES' columns.
- Converts SMILES strings to RDKit molecular objects.
- Adds hydrogen atoms and generates 3D conformers.
- Saves the output in an SDF file format.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script using:
```sh
python main.py
```
Ensure that `molecules.xlsx` contains the required columns: NAMES and SMILES respectively.

## Dependencies
The following Python packages are required:
- `pandas`
- `rdkit`
- `openpyxl`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any questions or suggestions, please reach out via GitHub issues.
