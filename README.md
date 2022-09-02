# Unsupervised Segmentation of Mutivarite Time Series (USMTSD)

Thesis Title: Unsupervised Segmentation of Mutivarite Time Series

This repository is part of the experimental study performed in context of my master thesis. There, four segmentation techniques for time series are evaluated and compared. To minimize implementation bias, however, we only utilized methods for which the source code was public available. We chose GGS, FLUSS, AutoPlait and IGTS based on the review we conducted in the first part of this work. First, we provided an overview of the selected methods in order to provide context. We developed a framework containing various types of multivariate time series datasets containing both real data (motion capture data, medical data, financial data, sensor data, and biological data) and synthetically generated data. The experiments were evaluated by calculating the Regime Score and the F1 Score. Across all dataset categories, IGTS DP performed the best in terms of F1 Score and Regime Score. Looking at the different datasets, IGTS DP has won 6 of 8 F1 Score evaluations and 5 of 8 Regime Score evaluations, and has therefore outperformed all other methods.

# References

Sadri, A., Ren, Y., & Salim, F. D. (2017). Information gain-based metric for recognizing transitions in 
human activities. Pervasive and Mobile Computing, 38, 92-109.
Github: https://github.com/cruiseresearchgroup/IGTS-python 

Hallac, D., Nystrup, P., &amp; Boyd, S. (2018). Greedy gaussian segmentation of multivariate time series. Advances in Data Analysis and Classification, 13(3), 727–751. https://doi.org/10.1007/s11634-018-0335-0 
Github: https://github.com/cvxgrp/GGS

Law, S. (2019). Stumpy: A powerful and scalable Python Library for Time Series Data Mining. Journal of Open Source Software, 4(39), 1504. https://doi.org/10.21105/joss.01504 
Github: https://github.com/TDAmeritrade/stumpy

Matsubara, Y., Sakurai, Y., &amp; Faloutsos, C. (2014). Autoplait. Proceedings of the 2014 ACM SIGMOD International Conference on Management of Data. https://doi.org/10.1145/2588555.2588556 
Github: https://github.com/kokikwbt/autoplait
