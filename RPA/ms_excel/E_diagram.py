import pyexcel as pe
import matplotlib.pyplot as plt

records = pe.get_records(file_name="data.xlsx")

data = []
for r in records:
    data.append((r['Reaction Coordinate'], r['Gibbs Free Energy (eV)']))

x, y = zip(*data)
plt.plot(x, y)
plt.xlabel("Reaction Coordinate")
plt.ylabel("Gibbs Free Energy (eV)")
plt.title("Gibbs Free Energy Profile")
plt.grid()

sheet = pe.Sheet(data)
sheet.name = "Gibbs Free Energy Profile"
book = pe.Book([sheet])
book.save_as("output.xlsx")
