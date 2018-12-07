# challenge_lab
Data pipelines
We are using twitter APIs as the source for our twitter data. We are able to mine past tweets given a user. We collected data for Berkeley shops, Influencers and used this data for building models.
We plan to use Instagram data through their api or web mining to collect the data.



Machine learning and models
We built a machine learning model using Support vector machines (SVM), to predict the favorites for a user. We believe SVM can handle sparse data well and the tweets generally have ~40k+ word space.

API services
We used python flask to build a service for the machine learning model. This can help us in scaling when we build a site or an app. The API service can be used to handle the requests. We also Gunicorn to help make worker processes to the service to handle more requests. 
We also explored Google Vision api service which can be used in the future to analyse image data.


