from aiida import load_profile
from aiida.orm import QueryBuilder
from aiida.orm.nodes.data.structure import StructureData

load_profile()

qb = QueryBuilder()

qb.append(StructureData)

qb.add_filter(StructureData, {'elements': {'in': ['Fe', 'Co', 'Mn', 'Ni']}})

results = qb.all()

for result in results:
    structure = result[0]
    print(f"Structure PK: {structure.pk}")
    print(f"Structure formula: {structure.get_formula()}")
    print()
