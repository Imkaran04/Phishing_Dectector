

from API import get_prediction

# path to trained model
model_path = "PHISHING DOMAIN.ipynb"

# input url
url = "www.tesla.com/"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)

