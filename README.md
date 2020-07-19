# Movie_Review_Spoiler_Detector

Project Organization
------------

    
    
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │   
    ├── notebooks          <- Jupyter notebooks
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    |
    ├── src                <- Source code for use in this project.
    │  
    │   ├── Flask App files         <- Scripts to run the Flask application
    │  
    │   ├── GCP     <- Scripts to turn generate files for Google Cloud Platform
    |
    │   ├── server.py        <- Scripts to train models and then use trained models to make
    
    
    The detector detects if the review has a spoiler or not using Naive Bayes algorithm.

    Flask files folder contains files for Flask web application implementation.

    GCP folder contains Source Distribution Package(SDP) for custom model deployment in Google Cloud Platform(GCP).

    CustomPred.py is a fuction for custom prediction on GCP.

    NB1.joblib and model.pkl are serialized versions of the trained model.

    server.py is for setting up the HTTP endpoint using Flask.

    setup.py is for creating a SDP.

    text_proc.py is the preprocessing function for the model.
    
   

