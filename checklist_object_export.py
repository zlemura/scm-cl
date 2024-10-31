import pickle_actions as pickle

import csv
import os
import time

def export_category_checklist_objects(category):
    category_objects = fetch_all_objects_for_category(category)

def fetch_all_objects_for_category(category):
    category_set_file_list = os.listdir("checklists/" + category)

    category_objects = []

    for file in category_set_file_list:
        file_objects = pickle.open_dump_file("checklists/" + category + "/" + file.replace(".pkl", ""))
        category_objects += file_objects

    return category_objects

def create_set_files_for_category(category):
    category_set_file_list = os.listdir("checklists/" + category)

    for file in category_set_file_list:
        file_objects = pickle.open_dump_file("checklists/" + category + "/" + file.replace(".pkl", ""))

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