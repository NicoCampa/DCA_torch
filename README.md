# DCA_torch
Implementation of Deep Count Autoencoder method for scRNA-seq in PyTorch for university seminar

Workflow to simulate data and apply to it DCA:

1. simulate the data using the R file simulate/simulateData.R
2. create AnnData file from the csv created by the R script running in the terminal: python CSVtoH5AD.py
3. now run DCA on the data simulated and converted, using: python run.py

the output wuold be under result folder. 1 plot  is focused on the outcomes of denoising and dimensionality reduction via an autoencoder (dca_emb.png), the 2nd one is specifically aimed at showcasing the effects of imputation on the data's structure and clustering (imputeX.png).
An additional file is saved in data folder, which is the denoised version of the data.
