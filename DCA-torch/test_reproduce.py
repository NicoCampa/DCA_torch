#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:31:41 2023

@author: yxk
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:52:35 2023

@author: yxk
"""

import scanpy as sc 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 


adata = sc.read("data/simulatedData.h5ad")
adata.X = np.float64(adata.X) ## 一定得是这个float64,否则结果是不能复现的
sc.pp.normalize_total(adata,target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.pl.umap(adata,color=["Group"],show=False)
plt.savefig("data/sim6_umap1.png")



##
data = pd.read_csv("./sim6_raw_counts.csv",index_col=0)
meta = pd.read_csv("./sim6_meta_info.csv",index_col=0)

adata = sc.AnnData(data.values,obs = meta)
adata.X = np.float64(adata.X)
sc.pp.normalize_total(adata,target_sum=1e4)

sc.pp.log1p(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.pl.umap(adata,color=["Group"],show=False)
print(adata.obsm["X_umap"])
plt.savefig("./sim6_umap2.png")


