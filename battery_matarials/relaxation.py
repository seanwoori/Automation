from fireworks import Firework, Workflow, LaunchPad
from pymatgen import Composition
from pymatgen.io.vasp.sets import MPRelaxSet
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.structure_prediction.substitution_probability import SubstitutionPredictor
from pymatgen.analysis.structure_matcher import StructureMatcher
import settings

# Materials Project API Key 입력
api_key = settings.MPR_API

# LaunchPad 연결
launchpad = LaunchPad.from_file('my_launchpad.yaml')

# 물질의 합성물을 결정
composition = Composition('LiFePO4')

# 물질의 Spacegroup 결정
spacegroup = 'Pnma'

# SubstitutionPredictor를 사용하여 다양한 합성물 생성
sp = SubstitutionPredictor(threshold=1e-5)
predictions = sp.predict(composition)

# 생성된 합성물들 중 Spacegroup가 일치하는 것을 선택
sm = StructureMatcher()
for prediction in predictions:
    s = prediction['structure']
    if sm.fit(s, Composition(composition)):
        if SpacegroupAnalyzer(s).get_space_group_symbol() == spacegroup:
            structure = s
            break

# 물질 구조의 최적화를 위한 fireworks 생성
relax_fw = Firework(
    wf_structure_optimization(structure, MPRelaxSet(structure, force_gamma=True),
                              vasp_cmd="vasp_std", db_file="db.json"),
    name='relax_fw')

# AutomaticSNL 객체 생성
asnl = AutomaticSNL()
# fireworks 생성
snl_fw = asnl.get_wf(structure, name='snl_fw')

# Workflow 생성
workflow = Workflow([relax_fw, snl_fw], {relax_fw: snl_fw})

# LaunchPad에 Workflow 등록
launchpad.add_wf(workflow)

