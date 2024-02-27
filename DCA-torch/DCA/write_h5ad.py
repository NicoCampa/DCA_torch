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


adata = sc.read("./sim6_group_True.h5ad")
print(adata)
data= pd.DataFrame(adata.X,index = adata.obs.index,columns=adata.var_names)
data.to_csv("./sim6_ture_counts.csv")
meta_info = adata.obs
meta_info.to_csv("./sim6_true_meta_info.csv")
# sc.pp.normalize_total(adata,target_sum=1e4)
# sc.pp.log1p(adata)
# sc.tl.pca(adata,svd_solver='arpack',random_state=1)
# print(adata.obsm["X_pca"])

# sc.pp.neighbors(adata,random_state=1)
# sc.tl.umap(adata,random_state=1)
# print(adata.obsm["X_umap"])
# sc.pl.umap(adata,color=["Group"],show=False)
# plt.savefig("./sim6_umap1.png")

# print(adata)
# data= pd.DataFrame(adata.X,index = adata.obs.index,columns=adata.var_names)
# data.to_csv("./sim6_raw_counts.csv")
# meta_info = adata.obs
# meta_info.to_csv("./sim6_meta_info.csv")

# array([[  27,   96,   10, ..., 1944,    8,  189],
#        [  27,   45,   18, ..., 1284,    6,  149],
#        [  20,   52,   24, ..., 1197,   13,  105],
#        ...,
#        [  38,   61,    0, ..., 1013,    8,    0],
#        [  27,   67,    0, ..., 1125,    8,   83],
#        [   9,    0,   26, ..., 1097,    2,   73]], dtype=int32)


##
# data = pd.read_csv("./sim6_raw_counts.csv",index_col=0)
# meta = pd.read_csv("./sim6_meta_info.csv",index_col=0)

# adata = sc.AnnData(data.values,obs = meta)
# adata.X = np.float64(adata.X)
# sc.pp.normalize_total(adata,target_sum=1e4)
# # array([[  2.8521025 ,  10.140809  ,   1.0563343 , ..., 205.3514    ,
# #           0.84506744,  19.964718  ],
# #        [  4.109214  ,   6.8486896 ,   2.739476  , ..., 195.41594   ,
# #           0.9131586 ,  22.676773  ],
# #        [  2.825577  ,   7.3465004 ,   3.3906925 , ..., 169.1108    ,
# #           1.8366251 ,  14.83428   ],
# #        ...,
# #        [  7.3530836 ,  11.803634  ,   0.        , ..., 196.01773   ,
# #           1.5480176 ,   0.        ],
# #        [  4.6613607 ,  11.5670805 ,   0.        , ..., 194.22336   ,
# #           1.3811439 ,  14.329369  ],
# #        [  1.8328073 ,   0.        ,   5.2947764 , ..., 223.39883   ,
# #           0.4072905 ,  14.866103  ]], dtype=float32)
# sc.pp.log1p(adata)
# sc.tl.pca(adata,svd_solver='arpack',random_state=1)
# print(adata.obsm["X_pca"])
# sc.pp.neighbors(adata,random_state=1)
# sc.tl.umap(adata,random_state=1)
# sc.pl.umap(adata,color=["Group"],show=False)
# print(adata.obsm["X_umap"])
# plt.savefig("./sim6_umap2.png")

