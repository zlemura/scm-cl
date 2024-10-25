import os
import time
import random

import source as source
import source_to_checklist as source_to_checklist
import pickle_actions as pickle

def fetch_set_lists_for_categories():
        category_identifiers = ["baseball-cards", "basketball-cards", "football-cards", "hockey-cards", "soccer-cards",
                                "racing-cards", "wrestling-cards", "ufc-cards"]
        # Write set lists for categories.
        for category_identifier in category_identifiers:
            source_set_list = source.fetch_all_set_identifiers_for_category(category_identifier)
            pickle.write_to_dump_file(source_set_list, "dumps/category_set_lists/" + category_identifier)
            sleep_time = random.randrange(1,6)
            print("Processed " + category_identifier + ". Sleeping for " + sleep_time.__str__() + " seconds.")
            time.sleep(sleep_time)

        # Read set lists for categories.
        for category_identifier in category_identifiers:
            set_results = pickle.open_dump_file("dumps/category_set_lists/" + category_identifier)
            for result in set_results:
                print(result.__dict__)
            print(category_identifier + " has " + len(set_results).__str__() + " set results.")

def fetch_set_lists_for_category():
    category_identifiers = ["baseball-cards", "basketball-cards", "football-cards", "hockey-cards", "soccer-cards",
                                "racing-cards", "wrestling-cards", "ufc-cards"]

    for category_identifier in category_identifiers:
        category_set_list = pickle.open_dump_file("dumps/category_set_lists/" + category_identifier)
        counter = 1
        for set_identifier in category_set_list:
            print("Processing " + counter.__str__() + " of " + len(category_set_list).__str__())
            file_path_for_set = "dumps/" + category_identifier + "/" + set_identifier.href
            file_name_for_set = "dumps/" + category_identifier + "/" + set_identifier.href + ".pkl"
            if os.path.isfile(file_name_for_set) == True:
                print("File exists for " + set_identifier.href)
                counter += 1
                continue
            set_product_list = source.fetch_set_results(set_identifier.href)
            pickle.write_to_dump_file(set_product_list, file_path_for_set)
            counter += 1
            print("Finished processing " + counter.__str__() + " of " + len(category_set_list).__str__())

def convert_category_source_products_to_checklist_objects():
    category_identifiers = ["baseball-cards", "basketball-cards", "football-cards", "hockey-cards", "soccer-cards",
                                    "racing-cards", "wrestling-cards", "ufc-cards"]
    for category in category_identifiers:
        print("Processing ", category)
        source_to_checklist.convert_set_products_to_checklist_objects_by_category(category)
        print("Finished processing", category)

def run():
    # create database table files in CSV for data.
    # tables outlined in Google Doc.
    print("Hi")


if __name__ == '__main__':
    run()