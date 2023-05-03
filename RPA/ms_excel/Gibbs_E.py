import pyexcel as pe

data = pe.get_records(file_name="filename.xlsx")

def calculate_gibbs_energy(h, s, t):
    return h - t * s

for row in data:
    enthalpy = float(row['Enthalpy'])
    zpe = float(row['Zero-point energy'])
    entropy = float(row['Entropy'])
    temperature = 298.15  # Insert temperature condition

    # calculating Gibbs free energy
    gibbs_energy = calculate_gibbs_energy(enthalpy + zpe, entropy, temperature)

    print(f"Gibbs Free Energy = {gibbs_energy} eV")
