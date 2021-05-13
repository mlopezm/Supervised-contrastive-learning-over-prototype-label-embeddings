# Supervised-contrastive-learning-over-prototype-label-embeddings
Code of the paper: "Supervised contrastive learning over prototype-label embeddings for network intrusion detection"

This repository contains the code and the files obtained for the Monte Carlo simulation on the probability that two source and destination network address elements (NAE) have a simultaneous collision on both their source and destination parts.

This simulation is part of the work done in the following work: “Network intrusion detection with a novel hierarchy of distances between embeddings of hash IP addresses”, Manuel Lopez-Martin, Belen Carro, Juan Ignacio Arribas, Antonio Sanchez-Esguevillas.

The simulation scope extends to the following scenarios:

1. one
2. two

The code for the second scenario is in the file: "Calc probability collision ip and port only.R"

The datsets area avilable on this location: https://drive.google.com/drive/folders/1QSf-0wK-pTKHamA13xW4KpNxcTTJsqt2?usp=sharing

The simulation has been done in R

The simulations demonstrate that the probability of collision (for a single NAE) depends on the maximum hash value (k) following the expression (1/k)^2 . Considering the three NAEs simulatenously the probability is (1/k)^6. In scenario 1 and 2 with a k=3000, the collision probability obtained for a single NAE is between 1e-07 and 2e-07, which is very close to the theoretical 1.111111e-07 (1/3000)^2 . And, in scenario 3 with a k=30, the collision probability obtained for a single NAE is between 0.0011342 and 0.0022053, which is also very close to the theoretical 0.001111111 (1/30)^2

In all simulations with a k=3000, not a single simultaneous collision has appeared for the three NAEs with a number of samples in the simulation of 1e+7.

The code is prepared to be executed in the cloud using Google Colaboratory https://colab.research.google.com/notebooks/intro.ipynb
