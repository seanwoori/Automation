import numpy as np
from cgcnn.model import CrystalGraphConvNet
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split
from sklearn.model_selection import train_test_split

# 데이터 로딩
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.materials
collection = db.formation_energy

X = []
y = []

for doc in collection.find({}):
    elem_a = doc['pretty_formula'].split()[0]
    elem_b = doc['pretty_formula'].split()[1]
    elements = [elem_a, elem_b]
    elements.sort()
    X.append((doc['input'], doc['neighbors'], elements))
    y.append(doc['formation_energy_per_atom'])

# 학습용 데이터와 테스트용 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 하이퍼파라미터 정의
orig_atom_fea_len = X[0][0].shape[-1]
nbr_fea_len = X[0][1].shape[-1]
atom_fea_len = 128
n_conv = 3
h_fea_len = [128, 256, 512]
pooling = "max"
input_shapes = {"atom": (None, orig_atom_fea_len), "nbr": (None, nbr_fea_len), "idx": (None, )}

# 모델 정의
model = CrystalGraphConvNet(atom_fea_len, nbr_fea_len, h_fea_len, n_conv, pooling)

# 손실 함수 정의
criterion = nn.MSELoss()

# 옵티마이저 정의
optimizer = optim.Adam(model.parameters(), lr=1e-3)

# 데이터셋 정의
class CGCNNDataSet(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        sample = {}
        sample['atom'] = torch.Tensor(self.X[idx][0])
        sample['nbr'] = torch.Tensor(self.X[idx][1])
        sample['idx'] = torch.LongTensor([idx])
        target = torch.Tensor([self.y[idx]])
        return sample, target

# 데이터로더 정의
train_dataset = CGCNNDataSet(X_train, y_train)
test_dataset = CGCNNDataSet(X_test, y_test)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

