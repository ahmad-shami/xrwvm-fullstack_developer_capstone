from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    car_model_data = [
        {"name": "Pathfinder", "car_type": "SUV", "year": 2023, "make": car_make_instances[0]},
        {"name": "Qashqai", "car_type": "SUV", "year": 2023, "make": car_make_instances[0]},
        {"name": "XTRAIL", "car_type": "SUV", "year": 2023, "make": car_make_instances[0]},
        {"name": "A-Class", "car_type": "SUV", "year": 2023, "make": car_make_instances[1]},
        {"name": "C-Class", "car_type": "SUV", "year": 2023, "make": car_make_instances[1]},
        {"name": "E-Class", "car_type": "SUV", "year": 2023, "make": car_make_instances[1]},
        {"name": "A4", "car_type": "SUV", "year": 2023, "make": car_make_instances[2]},
        {"name": "A5", "car_type": "SUV", "year": 2023, "make": car_make_instances[2]},
        {"name": "A6", "car_type": "SUV", "year": 2023, "make": car_make_instances[2]},
        {"name": "Sorrento", "car_type": "SUV", "year": 2023, "make": car_make_instances[3]},
        {"name": "Carnival", "car_type": "SUV", "year": 2023, "make": car_make_instances[3]},
        {"name": "Cerato", "car_type": "Sedan", "year": 2023, "make": car_make_instances[3]},
        {"name": "Corolla", "car_type": "Sedan", "year": 2023, "make": car_make_instances[4]},
        {"name": "Camry", "car_type": "Sedan", "year": 2023, "make": car_make_instances[4]},
        {"name": "Kluger", "car_type": "SUV", "year": 2023, "make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_type=data["car_type"],
            year=data["year"],
            make=data["make"],
            dealer_id=1,
        )

