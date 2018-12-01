# Analysis of imbalance in cloud.
Reference "Imbalance in the Cloud: an Analysis on Alibaba Cluster Trace".
As per the paper there was problem with allocation of resource which led to the spatial and temporal imbalances.
# Problem.
Resource allocated and used by jobs had alot of difference.
Since the resource allocated was way too much than required. Lot of other job remained in waiting state.
# Implementation.
As our final project we divide the project in two phases.
First Phase: Re-evaluated the paper as per our undersatnding. We found that the first graph mentioned in the paper had some issue. The graph was correct but explanation was not upto the mark. We also tried to analysed this problem.
During our second phase: we applied machine learning(logistic regression) to develop a model which can help the resource manager in the allocation of the resource such as CPU and Memory as per requirement.
# Techology
Python and R
Matplotlib
Scikit Learn
pandas
