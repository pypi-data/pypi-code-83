from rdkit import Chem
from rdkit.Chem import AllChem

def rdkit_optimize(smiles)
    print(type(smiles))
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol,maxIters=200)
    return mol