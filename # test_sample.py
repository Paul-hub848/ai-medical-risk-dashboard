# test_sample.py
api_key = "secret_key_12345"
url = "http://insecure-api.com/data"

import pickle
model = pickle.load(open("model.pkl", "rb"))