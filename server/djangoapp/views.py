# Uncomment the required imports before adding the code

# from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime
import os
from django.conf import settings
from .models import CarMake, CarModel
from .populate import initiate  # Ensure correct import for initiate function
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .restapis import get_request, analyze_review_sentiments

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt


def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provided credentials can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    data = {"userName": ""}
    return JsonResponse(data)


# Create a `registration` view to handle sign up request
@csrf_exempt


def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except Exception as e:
        # If not, simply log that this is a new user
        logger.debug(f"{e} {username} is a new user")

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)
    else:
        data = {"userName": username, "error": "Already Registered"}
        return JsonResponse(data)


def get_cars(request):
    # Check if CarMake data exists
    count = CarMake.objects.filter().count()
    if count == 0:
        initiate()  # Populate data if empty

    # Fetch all CarModel objects with related CarMake data
    car_models = CarModel.objects.select_related('make')

    # Prepare a list of car details
    cars = []
    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.make.name,
            "Type": car_model.car_type,
            "Year": car_model.year,
            "Price": car_model.price,
            "MakeDescription": car_model.make.description,
            "MakeCountry": car_model.make.country if hasattr(car_model.make, "country") else None,
            "MakeEstablishedYear": car_model.make.established_year if hasattr(car_model.make, "established_year") else None,
        })

    # Return the car details as a JSON response
    return JsonResponse({"CarModels": cars})


def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchDealer/{dealer_id}"
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


def add_review(request):
    if not request.user.is_anonymous:
        try:
            # response = post_review(data)
            return JsonResponse({"status": 200})
        except Exception as e:
            logger.error(f"Error in posting review: {e}")
            return JsonResponse({"status": 401, "message": "Error in posting review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})


def get_dealer_reviews(request, dealer_id):
    if not dealer_id:
        return JsonResponse({"status": 400, "message": "Bad Request"})

    endpoint = f"/fetchReviews/dealer/{dealer_id}"
    reviews = get_request(endpoint)

    if isinstance(reviews, list):
        for review in reviews:
            review['sentiment'] = analyze_review_sentiments(review['review'])['sentiment']
    else:
        reviews = []

    return JsonResponse({"status": 200, "reviews": reviews})


def register_view(request):
    index_path = os.path.join(settings.BASE_DIR, 'static', 'index.html')

    try:
        with open(index_path, 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        return HttpResponse("Error: index.html not found", status=404)

    return HttpResponse(html_content)
