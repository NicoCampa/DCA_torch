from time import time
import math, os
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.nn import Parameter
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from DCA.zinbAutoencoder import zinbAutoencoder
from DCA.single_cell_tools import *
import numpy as np
from sklearn import metrics
import h5py
import scanpy as sc
from DCA.preprocess import read_dataset, normalize
torch.set_default_tensor_type(torch.DoubleTensor)
import matplotlib.pyplot as plt
torch.manual_seed(42)

adata = sc.read("./data/simulatedData.h5ad")
device = "cpu"
batch_size = 32
pretrain_epochs= 150

adata = read_dataset(adata,
                 transpose=False,
                 test_split=False,
                 copy=True)

adata = normalize(adata,
                  size_factors=True,
                  normalize_input=True,
                  logtrans_input=True)

input_size = adata.n_vars
model = zinbAutoencoder(input_dim=adata.n_vars, z_dim=32, 
            encodeLayer=[64], decodeLayer=[64], device=device)

print(str(model))
t0 = time()
model.fit(X=adata.X, X_raw=adata.raw.X, size_factor=adata.obs.size_factors, 
                            batch_size= batch_size, epochs=pretrain_epochs)

print('Pretraining time: %d seconds.' % int(time() - t0))
print(model.imputeX.shape)
adata.obsm["X_emb"] = model.emb_X
sc.pp.neighbors(adata,use_rep="X_emb")
sc.tl.umap(adata)
sc.pl.umap(adata,color=["Group"],show=False)
plt.savefig("./result/dca_emb.png")


print(np.max(model.imputeX.data.numpy()))
adata_ae = sc.AnnData(model.imputeX.data.numpy(),obs= adata.obs,var= adata.var)
adata_ae.write("./adata_denoise.h5ad")
adata_ae.layers["denoised_count"] = adata_ae.X.copy()
sc.pp.normalize_total(adata_ae)
sc.pp.log1p(adata_ae)
sc.tl.tsne(adata_ae)
sc.pl.tsne(adata_ae,color=["Group"],show=False)
plt.savefig("./result/imputeX.png")

print(model.imputeX)

# evaluation 
# import scanpy as sc 
# adata_true = sc.read("./data/simulatedData.h5ad")
# print(np.max(adata_true.X))
# print(adata_true)
# from sklearn.metrics import mean_squared_error
# print(mean_squared_error(adata_true[:,adata_ae.var_names].X.copy(), adata_ae.layers["denoised_count"]) )




