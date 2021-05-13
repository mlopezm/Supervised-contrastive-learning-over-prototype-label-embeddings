# Supervised-contrastive-learning-over-prototype-label-embeddings
Code of the paper: "Supervised contrastive learning over prototype-label embeddings for network intrusion detection"

This repository contains the code and dataset files for the paper: "Supervised contrastive learning over prototype-label embeddings for network intrusion detection", , Manuel Lopez-Martin, Antonio Sanchez-Esguevillas, Juan Ignacio Arribas and Belen Carro.

The datasets files area avilable on this location: https://drive.google.com/drive/folders/1QSf-0wK-pTKHamA13xW4KpNxcTTJsqt2?usp=sharing . These files contain the NSL-KDD and UNSW-NB15 (ADFA) intrusion detection datasets. 

The simulation scope extends to the following scenarios:

1. one
2. two

The code for the second scenario is in the file: "Calc probability collision ip and port only.R"



The simulation has been done in R

The simulations demonstrate that the probability of collision (for a single NAE) depends on the maximum hash value (k) following the expression (1/k)^2 . Considering the three NAEs simulatenously the probability is (1/k)^6. In scenario 1 and 2 with a k=3000, the collision probability obtained for a single NAE is between 1e-07 and 2e-07, which is very close to the theoretical 1.111111e-07 (1/3000)^2 . And, in scenario 3 with a k=30, the collision probability obtained for a single NAE is between 0.0011342 and 0.0022053, which is also very close to the theoretical 0.001111111 (1/30)^2

In all simulations with a k=3000, not a single simultaneous collision has appeared for the three NAEs with a number of samples in the simulation of 1e+7.

The code is prepared to be executed in the cloud using Google Colaboratory https://colab.research.google.com/notebooks/intro.ipynb
