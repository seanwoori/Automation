from mp_api.client import MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
import matplotlib.pyplot as plt
import numpy as np
import settings

# Materials Project API Key 입력
api_key = settings.MPR_API

# MPRester 객체 생성
mpr = MPRester(api_key)

# 전기화학적 안정성(electrochemical stability)이 높은 물질들을 요청
criteria = {"icsd_ids": {"$exists": True}, "e_above_hull": {"$lt": 0.1}, "band_gap": {"$gt": 2}, "unit_cell_formula": {"$exists": True}, "pretty_formula": {"$exists": True}}
properties = ["material_id", "pretty_formula", "formation_energy_per_atom", "energy_per_atom", "band_gap", "total_magnetization", "volume", "density"]
data = mpr.summary.search(criteria=criteria, property=properties)

# Compatibility 객체 생성
compat = MaterialsProjectCompatibility()

# Mongodb type query
query = {
    'task_ids': {'$in': ['mp-33787', 'mp-2550', 'mp-540786', 'mp-5827', 'mp-568345', 'mp-554444']},
    'nelements': {'$lte': 4},
    'energy_above_hull': {'$lte': 0.1},
    'band_gap': {'$gte': 1},
    'elements': {'$all': ['Li', 'Mn', 'O']},
    'icsd_ids': {'$exists': False},
}

# query에 해당하는 물질들의 정보 fetch
results = mpr.summary.search(query, ["task_id", "pretty_formula", "e_above_hull", "band_gap"])

# 가져온 물질들의 formation energy per atom과 band gap을 Materials Project Compatibility를 사용하여 보정
entries = []
for r in results:
    entry = mpr.get_entry_by_material_id(r['task_id'])
    entry = compat.process_entry(entry)
    entries.append(entry)

# PhaseDiagram 객체 생성
pd = PhaseDiagram(entries)

# PhaseDiagram plot
pd_plotter = PDPlotter(pd)
pd_plotter.show()

# Grand Potential Phase Diagram plot
elements = ["Li", "Na", "K", "Mg", "Ca", "Zn", "Al", "Ti", "Fe", "Co", "Ni", "Cu"]
plotter = PDPlotter(pd, show_unstable=True)
plt = plotter.plot_grand_pots(chem_pot_limits={el: (-2, 2) for el in elements})
plt.show()

# 가져온 물질들의 formation energy per atom과 band gap을 출력
for e in entries:
    print("{}: formation_energy_per_atom = {:.4f}, band_gap = {:.4f}".format(e.entry_id, e.energy_per_atom, e.band_gap))

