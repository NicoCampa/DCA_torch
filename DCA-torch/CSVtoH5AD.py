import pandas as pd
import scanpy as sc

counts = pd.read_csv("./simulate/counts.csv", index_col=0)
truecounts = pd.read_csv("./simulate/truecounts.csv", index_col=0)
dropout = pd.read_csv("./simulate/dropout.csv", index_col=0)
cellinfo = pd.read_csv("./simulate/cellinfo.csv")
geneinfo = pd.read_csv("./simulate/geneinfo.csv")

adata = sc.AnnData(counts)
adata.var_names = geneinfo['Gene']
adata.obs = cellinfo.set_index('Cell') 

adata.layers['true_counts'] = truecounts
adata.layers['dropout'] = dropout

# Save to .h5ad format
adata.write("./data/simulatedData.h5ad")