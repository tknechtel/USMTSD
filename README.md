# TSS_time_series_segmentation
 Unsupervised segmentation of mutivarite time series

This repository is part of the experimental study performed in context of master thesis. There, four segmentation techniques for time series are evaluated and compared. To minimize implementation bias, however, we only utilized methods for which the source code was public available. We chose GGS, FLUSS, AutoPlait and IGTS based on the review we conducted in the first part of this work. First, we provided an overview of the selected methods in order to provide context. We developed a framework containing various types of multivariate time series datasets containing both real data (motion capture data, medical data, financial data, sensor data, and biological data) and synthetically generated data. The experiments were evaluated by calculating the Regime Score and the F1 Score. Across all dataset categories, IGTS DP performed the best in terms of F1 Score and Regime Score. Looking at the different datasets, IGTS DP has won 6 of 8 F1 Score evaluations and 5 of 8 Regime Score evaluations, and has therefore outperformed all other methods.


Results:

|   Dataset  |   Method     |   F1           |   RegimeScore  |
|------------|--------------|----------------|----------------|
|   apple    |   Autoplaid  |   0            |   0            |
|   apple    |   IGTS DP    |   0,545454545  |   0,025120579  |
|   apple    |   IGTS TD    |   0,4          |   0,063906752  |
|   apple    |   FLOSS 1    |   0,769230769  |   0,042001608  |
|   apple    |   FLOSS 2    |   0,769230769  |   0,042001608  |
|   apple    |   GGS        |   0,769230769  |   0,030144695  |
|   bee      |   Autoplait  |   0,8          |   0,154351396  |
|   bee      |   IGTS DP    |   1            |   0,027914614  |
|   bee      |   IGTS TD    |   0,5          |   0,418719212  |
|   bee      |   FLOSS 1    |   0            |   0,386699507  |
|   bee      |   FLOSS 2    |   0,666666667  |   0,250410509  |
|   bee      |   GGS        |   0,5          |   0,468801314  |
|   blood    |   Autoplait  |   0            |   0            |
|   blood    |   IGTS DP    |   0            |   0,450811461  |
|   blood    |   IGTS TD    |   0            |   0,467508181  |
|   blood    |   FLOSS 1    |   1            |   0,003673279  |
|   blood    |   FLOSS 2    |   1            |   0,002805049  |
|   blood    |   GGS        |   1            |   0,000667869  |
|   cd1      |   Autoplait  |   0,8          |   0,030412946  |
|   cd1      |   IGTS DP    |   1            |   0,009021577  |
|   cd1      |   IGTS TD    |   0,833333333  |   0,062686012  |
|   cd1      |   FLOSS 1    |   0,666666667  |   0,041759673  |
|   cd1      |   FLOSS 2    |   0,666666667  |   0,03655      |
|   cd1      |   GGS        |   0,933333333  |   0,01395      |
|   cd2      |   Autoplait  |   0,666666667  |   0,032462479  |
|   cd2      |   IGTS DP    |   1            |   0,013118399  |
|   cd2      |   IGTS TD    |   0,923076923  |   0,021456365  |
|   cd2      |   FLOSS 1    |   0,727272727  |   0,044246804  |
|   cd2      |   FLOSS 2    |   0,727272727  |   0,044246804  |
|   cd2      |   GGS        |   1            |   0,014897165  |
|   occ      |   IGTS DP    |   0,952380952  |   0,005347594  |
|   occ      |   IGTS TD    |   0,952380952  |   0,008377897  |
|   occ      |   FLOSS 1    |   0,842105263  |   0,020855615  |
|   occ      |   FLOSS 2    |   0,9          |   0,016755793  |
|   occ      |   GGS        |   0,869565217  |   0,014616756  |
|   syn1     |   IGTS DP    |   1            |   0,001020408  |
|   syn1     |   IGTS TD    |   0,933333333  |   0,066020408  |
|   syn1     |   FLOSS 1    |   0,6          |   0,096428571  |
|   syn1     |   FLOSS 2    |   0,6          |   0,099285714  |
|   syn1     |   GGS        |   0,833333333  |   0,081530612  |
|   syn2     |   Autoplait  |   0,526315789  |   0,003469388  |
|   syn2     |   IGTS DP    |   1            |   0,000918367  |
|   syn2     |   IGTS TD    |   1            |   0,000714286  |
|   syn2     |   FLOSS 1    |   0,666666667  |   0,019132653  |
|   syn2     |   FLOSS 2    |   0,727272727  |   0,016173469  |
|   syn2     |   GGS        |   0,727272727  |   0,014183673  |

