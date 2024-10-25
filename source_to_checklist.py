import os

from checklist_object import checklist_object
import pickle_actions as pickle

def convert_set_products_to_checklist_objects_by_category(category_identifier):
    category_file_list = fetch_category_set_files(category_identifier)

    for file in category_file_list:
        set_source_product_list, set_name = pickle.open_dump_file("dumps/" + category_identifier + "/" + file.replace(".pkl",""))
        set_checklist_objects = convert_source_products_to_checklist_objects(set_source_product_list,set_name)
        pickle.write_to_dump_file(set_checklist_objects,"checklists/" + category_identifier + "/" + file.replace(".pkl",""))

def fetch_category_set_files(category_identifier):
    return os.listdir("dumps/" + category_identifier)

def fetch_category_checklist_files(category_identifier):
    return os.listdir("checklists/" + category_identifier)

def convert_source_products_to_checklist_objects(source_products, set_name):
    checklist_objects = []
    for product in source_products:
        variantName = ""
        printRun = product.printRun
        setName = set_name
        if "[" in product.productName and "]" in product.productName:
            variantName = product.productName.split('[')[1].split(']')[0]
            playerName = product.productName.split("[")[0].strip()
            cardNumber = product.productName.split("]")[1].strip()
            #print("VARIANT FOUND: ",playerName, "-", variantName, "-", cardNumber, "-", printRun, "-", setName)
            checklist_objects.append(checklist_object(playerName, variantName, cardNumber, printRun, setName))
        else:
            product_name_split_by_hash = product.productName.split("#")
            product_name_split_by_name = product.productName.split(product_name_split_by_hash[0])

            playerName = product_name_split_by_hash[0].strip()
            cardNumber = product_name_split_by_name[1].strip()
            #print("VARIANT NOT FOUND: ",playerName, "-", variantName, "-", cardNumber, "-", printRun, "-", setName)
            checklist_objects.append(checklist_object(playerName, variantName, cardNumber, printRun, setName))

    return checklist_objects