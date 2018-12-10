cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [model[0] for model in cars.values()]


get_first_model_each_manufacturer()


def get_all_matching_models(cars=cars, grep='CO'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matched_models = [
        model
        for car in cars.values()
        for model in car
        if grep.lower() in model.lower()
    ]

    return sorted(matched_models)


get_all_matching_models()


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    # return dict([(key, sorted(value)) for key, value in cars.items()])
    return {
        manufacturer: sorted(models)
        for manufacturer, models in cars.items()
    }


sort_car_models()
