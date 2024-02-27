library(splatter)


#set wd
setwd('~/Documents/DCA-torch/simulate')

sim = splatSimulate(group.prob = c(1/3,1/3,1/3),
                     nGenes = 200,
                     batchCells = 2000,
                     dropout.type = 'experiment',
                     method = 'groups',
                     seed = 42,
                     dropout.shape = -1,
                     dropout.mid = 5)

counts <- as.data.frame(t(counts(sim)))
truecounts <- as.data.frame(t(assays(sim)$TrueCounts))
dropout <- as.matrix(assays(sim)$Dropout)
mode(dropout) <- 'integer'
dropout <- as.data.frame(t(dropout))
cellinfo <- as.data.frame(colData(sim))
geneinfo <- as.data.frame(rowData(sim))

# In summary, using these parameters, the simulation is configured 
# to create a realistic experimental scenario where genes with lower 
# expression levels are more likely to experience dropout, with a 
# specific focus on modeling the dropout behavior around a midpoint 
# expression level of 5. However, the use of a negative shape parameter 
# should be verified, as it may not be applicable or might require specific 
# handling within the Splatter framework.

write.csv(counts, "./counts.csv", row.names = TRUE)
write.csv(truecounts, "./truecounts.csv", row.names = TRUE)
write.csv(dropout, "./dropout.csv", row.names = TRUE)
write.csv(cellinfo, "./cellinfo.csv", row.names = FALSE)
write.csv(geneinfo, "./geneinfo.csv", row.names = FALSE)
