"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    if all_cars == "":
        return []
    make_and_model = ""
    all_cars_in_list = []
    cars_in_letters = []
    for element in all_cars:
        if element != ",":
            cars_in_letters += [element]
        else:
            make_and_model = make_and_model.join(cars_in_letters)
            all_cars_in_list.append(make_and_model)
            cars_in_letters = []
            make_and_model = ""
            continue
    make_and_model = make_and_model.join(cars_in_letters)
    all_cars_in_list.append(make_and_model)
    return all_cars_in_list


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    all_cars_in_list = list_of_cars(all_cars)
    car_makes_in_list = []
    some_make = ""
    for element in all_cars_in_list:
        for i in range(len(element)):
            if element[i] == " ":
                some_make = element[:i]
                break
        if some_make not in car_makes_in_list:
            car_makes_in_list.append(some_make)
    return car_makes_in_list
    #
    # make_in_letters = []
    # for element in all_cars_in_list:
    #     for i in element:
    #         if i == " ":
    #             break
    #         make_in_letters += [i]
    #     some_make = some_make.join(make_in_letters)
    #     if some_make not in car_makes_in_list:
    #         car_makes_in_list.append(some_make)
    #     make_in_letters = []
    #     some_make = ""


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    all_cars_in_list = list_of_cars(all_cars)
    car_models_in_list = []
    some_model = ""
    for element in all_cars_in_list:
        for i in range(len(element)):
            if element[i] == " ":
                some_model = element[i + 1:]
                break
        if some_model not in car_models_in_list:
            car_models_in_list.append(some_model)
    return car_models_in_list


def search_by_make(all_cars: str, make: str) -> list:
    """Find makes in list."""
    all_cars_in_list = list_of_cars(all_cars)
    founded_cars = []
    for element in all_cars_in_list:
        if make.capitalize() in element.capitalize():
            founded_cars += [element]
    return founded_cars

# element.endswith(model.capitalize()): model.capitalize() in element:
# car.endswith(model.capitalize()):
# for i in range(len(element)):
#     if element[i] == " ":
#         some_model = element[:i]
#         break


def search_by_model(all_cars: str, model: str) -> list:
    """Find models in list."""
    found_cars = []
    all_cars_in_list = list_of_cars(all_cars)
    for element in all_cars_in_list:
        for el in element.split(" "):
            if model.capitalize() == el.capitalize() and element.index(el) != 0:
                found_cars.append(element)
    return found_cars


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    cars_list = list_of_cars(all_cars)
    makes_list = car_makes(all_cars)
    specific_models_list = []
    final_list = []
    some_model = ""
    for make in makes_list:
        for car in cars_list:
            if make in car:
                for i in range(len(car)):
                    if car[i] == " ":
                        some_model = car[i + 1:]
                        break
                if some_model not in specific_models_list:
                    specific_models_list.append(some_model)
        make_and_models_list = [make, specific_models_list]
        final_list.append(make_and_models_list)
        specific_models_list = []
    return final_list


if __name__ == '__main__':
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40,Audi A4,Audi a4 2021", "a4"))

    print(car_make_and_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon lux,Skoda Superb,Skoda Superb,BMW x5"))
    # [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon']]]

    print(car_make_and_models("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [['Mazda', ['6']]]
    print(car_make_and_models(""))  # []
