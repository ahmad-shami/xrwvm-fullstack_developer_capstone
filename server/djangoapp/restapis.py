# Uncomment the imports below before you add the function code
# import requests
import os
from django.http import JsonResponse
from dotenv import load_dotenv
import requests


load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments

# def post_review(data_dict):
# Add code for posting review
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print("Network exception occurred {e}")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        result = response.json()
        
        # Ensure the result contains the 'sentiment' key
        if "sentiment" in result:
            return result
        else:
            return {"sentiment": "unknown", "confidence": 0.0}
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        # Return a default response in case of failure
        return {"sentiment": "error", "confidence": 0.0}

#def analyze_review_sentiments(text):
#    request_url = sentiment_analyzer_url + "analyze/" + text
#    try:
        # Call the GET method of the requests library
#        response = requests.get(request_url)
#        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON response
#        result = response.json()
        
        # Validate the presence of expected keys in the response
#        if "sentiment" in result and "confidence" in result:
#            return result
#        else:
#            return {"sentiment": "unknown", "confidence": 0.0, "error": "Missing keys in response"}
    
#    except requests.exceptions.RequestException as e:
        # Handle HTTP and network-related errors
#        print(f"Network exception occurred: {e}")
#        return {"sentiment": "error", "confidence": 0.0, "error": str(e)}
#    except ValueError as e:
        # Handle JSON decoding errors
#        print(f"Error decoding JSON response: {e}")
#        return {"sentiment": "error", "confidence": 0.0, "error": "Invalid JSON response"}
#    except Exception as e:
        # Catch any other unexpected exceptions
#        print(f"Unexpected error: {e}")
#        return {"sentiment": "error", "confidence": 0.0, "error": str(e)}



def get_dealer_reviews(request, dealer_id):
    # If dealer ID is provided
    if dealer_id:
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_request(endpoint)
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])
            print(response)
            
            # Safely assign sentiment
            review_detail['sentiment'] = response.get("sentiment", "unknown")
        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print("Network exception occurred: {e}")

