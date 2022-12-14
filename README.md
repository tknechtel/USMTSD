# Unsupervised Segmentation of Mutivariate Time Series Data (USMTSD)

Thesis Title: Unsupervised Segmentation of Mutivariate Time Series Data - A Survey and experimental Study 

This repository is part of the experimental study performed in context of my master thesis. There, four segmentation techniques for time series are evaluated and compared. To minimize implementation bias, however, we only utilized methods for which the source code was public available. We chose GGS [^1], FLUSS (STUMPY implementation) [^2], AutoPlait [^3] and IGTS [^4] based on the review we conducted in the first part of this work. First, we provided an overview of the selected methods in order to provide context. We developed a framework containing various types of multivariate time series datasets containing both real data (motion capture data, medical data, financial data, sensor data, and biological data) and synthetically generated data. The experiments were evaluated by calculating the Regime Score and the F1 Score. Across all dataset categories, IGTS DP performed the best in terms of F1 Score and Regime Score. Looking at the different datasets, IGTS DP has won 6 of 8 F1 Score evaluations and 5 of 8 Regime Score evaluations, and has therefore outperformed all other methods.

## Code
The [Code](https://github.com/tknechtel/USMTSD/tree/main/Code) folder contains the source file for IGTS, AutoPlait and GSS. For FLUSS we used the STUMPY api. The REA we used to extract the segmentation points is implemented directly in the colab notebook.

## Colab
The [Colab](https://github.com/tknechtel/USMTSD/tree/main/Colab) folder contains two different files. The Dataset_Visualisation.ipynb is used for the visulation of the different datasets to gain a first inside. The secound notebook contains the performed experiments.

## Data
The [Data](https://github.com/tknechtel/USMTSD/tree/main/Data) folder contain the different datasets we used in our experiments.

## Results
The results can be found in [here](https://github.com/tknechtel/USMTSD/blob/main/results.md).

References:

[^1]: Hallac, D., Nystrup, P., &amp; Boyd, S. (2018). Greedy gaussian segmentation of multivariate time series. Advances in Data Analysis and Classification, 13(3), 727???751. https://doi.org/10.1007/s11634-018-0335-0 
Github: https://github.com/cvxgrp/GGS

[^2]: Law, S. (2019). Stumpy: A powerful and scalable Python Library for Time Series Data Mining. Journal of Open Source Software, 4(39), 1504. https://doi.org/10.21105/joss.01504 
Github: https://github.com/TDAmeritrade/stumpy

[^3]: Matsubara, Y., Sakurai, Y., &amp; Faloutsos, C. (2014). Autoplait. Proceedings of the 2014 ACM SIGMOD International Conference on Management of Data. https://doi.org/10.1145/2588555.2588556 
Github: https://github.com/kokikwbt/autoplait

[^4]: Sadri, A., Ren, Y., & Salim, F. D. (2017). Information gain-based metric for recognizing transitions in 
human activities. Pervasive and Mobile Computing, 38, 92-109.
Github: https://github.com/cruiseresearchgroup/IGTS-python 
