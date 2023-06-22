# Multi-modal deep learning: Application to integrative modelling of electrocardiography and cardiac imaging
By Nikolaos Athanasopoulos

This repository is part of the thesis of the Master's in Data Science by the University of Barcelona 2022/2023.

### Abstract
The field of machine learning has undergone significant advancements and developments in medicine over the past few years. Strong deep learning techniques have been developed for the purpose of processing complicated medical data types as time-series data (such as electrocardiography), genetic data or medical imaging. However, these developments have often taken place in specialised ways, resulting in a lack of deep learning implementations that allow to seamlessly integrate medical data from different types. This diploma thesis investigates the potential of deep learning models to combine electrocardiography (ECG) and magnetic resonance imaging (MRI) data for improved cardiac analysis.

The research aims to overcome the costs, complexity, and processing time constraints of MRI, by developing a deep learning model capable of predicting cardiac structural dynamics based on ECG signals. The interest of this project relies on the potential of generating from a single ECG signal a pseudo-MRI Image, which corresponds to the same patient, providing significantly more detailed information related to the condition of the heart compared to the ECG alone. In this approach, we will benefit from both the advantages ECG processing has over MRI and the improved understanding of the heart provided by the generated pseudo-MRI.

The study utilizes a large collection of ECG and cardiac MRI pairs dataset derived from multiple patients, available in the UK Biobank, in order to build connections between these two modalities. By successfully integrating multimodal data, the proposed model can create opportunities for novel applications in anomaly detection, diagnosis and clinical decision-making. This innovative approach has the potential to transform the field of medical imaging by providing a more affordable, effective, and accessible way to analyze cardiac health and disease.

### Dataset
Disclaimer: The data used for this project are sensitive and therefore no data exploration can be publicly shown. Though, ECG and MRI datasets accesible to the public, can be found in UK Biobank. If you want to reproduce the output results provided, a folder named UKBB should be created and two more subfolders: ecg, where the ECG signals will be stored and NIFTI, where the MRI images will be stored. 
