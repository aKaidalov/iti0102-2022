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
    if all_cars == "":
        return []
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
    if all_cars == "":
        return []
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


def search_by_make(all_cars: str) -> list:
    """Find make in list."""
    if all_cars == "":
        return []
    all_cars_in_list = list_of_cars(all_cars)
    find_make = input("What car do you want to find? ")
    founded_cars = []
    for element in all_cars_in_list:
        if find_make.capitalize() in element.capitalize():
            founded_cars += [element]
    return founded_cars


if __name__ == '__main__':
    print(list_of_cars("Audi A4,Skoda Superb,Audi A4"))  # ["Audi A4", "Skoda Superb", "Audi A4"]
    print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
    # ['Audi', 'Skoda', 'BMW', 'Seat']

    print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']

    print(car_makes(""))  # []

    print(car_models("Audi A4,Skoda Superb,Audi A4,Audi A6,Tesla Model S"))  # ["A4", "Superb", "A6"]

    print(search_by_make("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))