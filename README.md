# Supervised-contrastive-learning-over-prototype-label-embeddings
Code of the paper: "Supervised contrastive learning over prototype-label embeddings for network intrusion detection"

This repository contains the code and dataset files for the paper: "Supervised contrastive learning over prototype-label embeddings for network intrusion detection", Manuel Lopez-Martin, Antonio Sanchez-Esguevillas, Juan Ignacio Arribas and Belen Carro.

The dataset files are available on this location: https://drive.google.com/drive/folders/1QSf-0wK-pTKHamA13xW4KpNxcTTJsqt2?usp=sharing . These files contain:
1. The original NSL-KDD and UNSW-NB15 (ADFA) intrusion detection datasets:  UNSW_NB15_training-set.csv, UNSW_NB15_testing-set.csv and KDDTest+.txt, KDDTrain+.txt; which are available from: https://www.unb.ca/cic/datasets/nsl.html and https://researchdata.edu.au/unsw-nb15-dataset
2. The datasets after data processing: NSL_KDD_Load.pkl and ADFA_Load.pkl. These are the files that are used in the paper code.

All code fies are available in this repository. The description of the different files is as follows:
1. NSL_KDD_Load v2.0.ipynb :  Code to perform the data processing of the NSL-KDD dataset
2. ADFA_Load 1.0.ipynb : Code to perform the data processing of the UNSW-NB15 dataset
3. IDS_NSL-KDD v2.0-5labels-information fusion.ipynb: Code for the most representative models proposed in the paper, applied to the NSL-KDD dataset
4. IDS_UNSW-NB15 v2.0-10labels-information fusion.ipynb: Code for the most representative models proposed in the paper, applied to the UNSW-NB15 dataset
5. Lib.py: Code file with some auxiliary functions for data processing

The different models presented in each code file are:

- NSL-KDD (IDS_NSL-KDD v2.0-5labels-information fusion.ipynb)
1. LBL, ConCE (with embedding dimensions 2 and 10)
2. LBL, ConLE
3. RLB-CL, E2NMS
4. RLB-CL, E2NAMS
5. RLB-CL, E2WNAMS (1,0.5,0.5)
6. RLB-CL, ENMS
7. RLB-CL, CE+ENMS
8. RLB-CL, NMM
9. RLB-CL, CE+NMM
10. RLB-CL, CEDist+NMM
11. RLB-CL, WNAMM (1,0.5,1,0.5)
12. RLB-CL, NAMM
13. RLB-CL, AMM
14. RLB-CL, ConN

- UNSW-NB15 (IDS_UNSW-NB15 v2.0-10labels-information fusion.ipynb)
1. LBL, ConCE
2. LBL, ConLE
3. RLB-CL, E2NMS
4. RLB-CL, ENMS
5. RLB-CL, CE+ENMS
6. RLB-CL, NMM
7. RLB-CL, NAMM
8. RLB-CL, MMoLE

Each model includes: the architecture of the model, the results of the training phase, the performance metrics for the test set and the visualization of the clusters. The chosen models correspond mainly to models with an embedding dimension of two (to facilitate the visualization of the clusters) and to the multiclass case (because they are more complex and representative).

The code can be executed in the cloud using Google Colaboratory https://colab.research.google.com/notebooks/intro.ipynb
