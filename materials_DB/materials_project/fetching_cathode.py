import pandas as pd
from itertools import combinations
from mp_api.client import MPRester
import settings 

api_key = settings.MPR_API

# 인스턴스 생성
m = MPRester(api_key)

# 공간군 리스트 ~ 올리빈 및 층상구조
spacegroup_list = ["Fm-3m", "R-3m"]

# 양극재 대상 금속 리스트 ~ 3d metals
elements_list = ["Fe", "Ni", "Co", "Mn"]

df_list = []
for i in range(1, 5):
    for elements in combinations(elements_list, i):
        criteria = {
            "elements": {"$all": list(elements)},
            "nelements": len(elements) + 1,
            "spacegroup.symbol": {"$in": spacegroup_list},
        }
        properties = ["material_id", "pretty_formula", "formation_energy_per_atom"]
        data = m.query(criteria, properties)
        df_list.append(pd.DataFrame(data))

df = pd.concat(df_list, ignore_index=True)

# csv 파일로 저장
df.to_csv("materials_data.csv", index=False)