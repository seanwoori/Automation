from mp_api.client import MPRester
import settings 

api_key = settings.MPR_API

# 인스턴스 생성
m = MPRester(api_key)

# 특정 양극재 물질 입력란
data = m.get_data("insert_your_cathode_id_here")

# 데이터를 출력
for entry in data:
    print("물질 ID:", entry['material_id'])
    print("화학식:", entry['pretty_formula'])
    print("형성 에너지 (eV/atom):", entry['formation_energy_per_atom'])
    dos = m.get_dos_by_material_id(entry['material_id'])
    print("DOS 데이터:", dos)