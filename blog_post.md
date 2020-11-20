# Introduction
The year of 2020 has been a long and stressful one. With the existence of so many stressors I felt that for a dataset it would be nice to have a return to nature, enter the "Forest Cover Type Dataset". This dataset describes different sections of forest in the Roosevelt National Forest in Colorado.
The target I chose for this dataset was the Cover Type, or the type of trees primarly making up the cover in a 30m by 30m section of the forest. The dataset provides a number of cartographic features to use in predicting the Cover Type. 

# Data Cleaning and Feature Engineering
The dataset was provided by the Jock A. Blackard of the University of Colorado. The exploration of the dataset showed that it was already a very clean. There are no missing values or columns with open ended string data. The one problem I faced was that two features, Soil Type and Wilderness Area, were already One Hot Encoded which could lead to an impact to certain models.
The first steps I took for feature engineering were to revert the one hot encoding for Soil Type and Wilderness Area. Having the Soil Type categories further allowed me to extract the Climatic Zone and Geological Zone, as both were part of the Soil Type codes. The last feature I engineered was taking the Horizontal and Vertical distances to the nearest surface water and find the straight line distance to the nearest water, thank you Pythagoras and your theorem for making this feature possible. 

# Choosing Models

# Findings