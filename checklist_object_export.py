import pickle_actions as pickle

import csv
import os

def export_category_checklist_objects(category):
    category_objects = fetch_all_objects_for_category(category)

    create_set_files_for_category(category)

    # create_set_files_for_category
    # create_player_name_files_for_category
    # create_variant_files_for_category
    # create_print_run_files_for_category
    # create_year_files_for_category
    # create_enum_files_for_category

def fetch_all_objects_for_category(category):
    category_set_file_list = os.listdir("checklists/" + category)

    category_objects = []

    for file in category_set_file_list:
        file_objects = pickle.open_dump_file("checklists/" + category + "/" + file.replace(".pkl", ""))
        category_objects += file_objects

    return category_objects

def create_set_files_for_category(category):
    category_set_file_list = os.listdir("checklists/" + category)

    for file_name in category_set_file_list:
        print("Processing ", file_name)
        file_objects = pickle.open_dump_file("checklists/" + category + "/" + file_name.replace(".pkl", ""))
        objects_to_add_to_file = []
        for object in file_objects:
            objects_to_add_to_file.append(convert_checklist_object_to_row(object))
        write_to_csv_file("exports/sets/" + category + "/" + file_name.replace(".pkl","") + ".csv", objects_to_add_to_file)
        print("Processed ", file_name)


def convert_checklist_object_to_row(checklist_object):
    year = fetch_year_from_set_name(checklist_object.setName)
    manufacturer = fetch_manufacturer_from_set_name(checklist_object.setName)
    playerName = checklist_object.playerName
    characters_to_remove = [("ō", "o")]
    for character in characters_to_remove:
        if character[0] in playerName:
            playerName = playerName.replace(character[0], character[1])

    '''
    print(playerName, checklist_object.variantName, checklist_object.cardNumber, \
           checklist_object.printRun, checklist_object.setName, year, manufacturer)
    '''

    return playerName.strip(), checklist_object.variantName.strip(), checklist_object.cardNumber.strip(), \
           checklist_object.printRun, checklist_object.setName.strip(), year, manufacturer.strip()


def fetch_year_from_set_name(setName):
    year = int(setName.split(" ")[0])
    return year


def fetch_manufacturer_from_set_name(setName):
    product_list = ["Bowman", "Donruss", "Finest", "Fleer", "Leaf", "Score", "Stadium Club",
                    "Upper Deck", "Hoops", "Skybox", "Ultra", "O-Pee-Chee", "Collector's Choice"]

    manufacturer_list = ["Topps", "Panini"]

    for product in product_list:
        if product in setName:
            return product

    for manufacturer in manufacturer_list:
        if manufacturer in setName:
            return manufacturer

def write_to_csv_file(file_name, objects_to_write):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile,  delimiter='|')
        writer.writerows(objects_to_write)

class object_csv_structure:
    def __init__(self, playerName, variantName, cardNumber, printRun, setName, setYear, setManufacturer):
        self.playerName = playerName
        self.variantName = variantName
        self.cardNumber = cardNumber
        self.printRun = printRun
        self.setName = setName
        self.setYear = setYear
        self.setManufacturer = setManufacturer
