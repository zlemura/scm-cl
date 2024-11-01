import pickle_actions as pickle

import csv
import os

def export_category_checklist_objects(category):
    '''
    TODO
     create_variant_files_for_category
     create_print_run_files_for_category
     create_year_files_for_category
     create_enum_files_for_category
    '''
    category_objects = fetch_all_objects_for_category(category)

    #create_set_files_for_category(category)

    #create_player_name_files_for_category(category_objects, category)

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

def create_player_name_files_for_category(category_objects, category):
    a = ['a',[]]
    b = ['b',[]]
    c = ['c',[]]
    d = ['d',[]]
    e = ['e',[]]
    f = ['f',[]]
    g = ['g',[]]
    h = ['h',[]]
    i = ['i',[]]
    j = ['j',[]]
    k = ['k',[]]
    l = ['l',[]]
    m = ['m',[]]
    n = ['n',[]]
    o = ['o',[]]
    p = ['p',[]]
    q = ['q',[]]
    r = ['r',[]]
    s = ['s',[]]
    t = ['t',[]]
    u = ['u',[]]
    v = ['v',[]]
    w = ['w',[]]
    x = ['x',[]]
    y = ['y',[]]
    z = ['z',[]]

    print("Starting to separate objects into letters.")

    for object in category_objects:
        if len(object.playerName) == 0:
            continue
        first_char_of_player_name = object.playerName[0].lower()
        if first_char_of_player_name.isalpha() == 0:
            continue
        if first_char_of_player_name == "a":
            a[1].append(object)
        if first_char_of_player_name == "b":
            b[1].append(object)
        if first_char_of_player_name == "c":
            c[1].append(object)
        if first_char_of_player_name == "d":
            d[1].append(object)
        if first_char_of_player_name == "e":
            e[1].append(object)
        if first_char_of_player_name == "f":
            f[1].append(object)
        if first_char_of_player_name == "g":
            g[1].append(object)
        if first_char_of_player_name == "h":
            h[1].append(object)
        if first_char_of_player_name == "i":
            i[1].append(object)
        if first_char_of_player_name == "j":
            j[1].append(object)
        if first_char_of_player_name == "k":
            k[1].append(object)
        if first_char_of_player_name == "l":
            l[1].append(object)
        if first_char_of_player_name == "m":
            m[1].append(object)
        if first_char_of_player_name == "n":
            n[1].append(object)
        if first_char_of_player_name == "o":
            o[1].append(object)
        if first_char_of_player_name == "p":
            p[1].append(object)
        if first_char_of_player_name == "q":
            q[1].append(object)
        if first_char_of_player_name == "r":
            r[1].append(object)
        if first_char_of_player_name == "s":
            s[1].append(object)
        if first_char_of_player_name == "t":
            t[1].append(object)
        if first_char_of_player_name == "u":
            u[1].append(object)
        if first_char_of_player_name == "v":
            v[1].append(object)
        if first_char_of_player_name == "w":
            w[1].append(object)
        if first_char_of_player_name == "x":
            x[1].append(object)
        if first_char_of_player_name == "y":
            y[1].append(object)
        if first_char_of_player_name == "z":
            z[1].append(object)

    all_letters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

    print("Finished separating objects into letters.")

    for letter in all_letters:
        current_letter = letter[0]
        current_letter_obects = letter[1]
        if len(current_letter_obects) == 0:
            print("Current letter - ", current_letter, " - has no records. Skipping.")
            continue
        print("Processing ", current_letter)
        objects_to_add_to_file = []
        for object in current_letter_obects:
            objects_to_add_to_file.append(convert_checklist_object_to_row(object))
        write_to_csv_file("exports/player_names/" + category + "/" + current_letter + ".csv",
                          objects_to_add_to_file)
        print("Processed ", current_letter)

    '''
    running_count = 0

    for letter in all_letters:
        #print(letter[0])
        #print(letter[1])
        running_count += len(letter[1])
    
    print("I processed a total of ", len(category_objects))
    print("I counted a total in the letters of ", running_count)
    print("Theres a difference of ", len(category_objects) - running_count)
    '''

def create_variant_files_for_category(category_objects, category):
    unique_variant_values  = []

    for object in category_objects:
        if len(object.variantName) == 0:
            continue
        variant_matched = 0
        for variant in unique_variant_values:
            if variant[0] == object.variantName:
                if variant[1] == object.printRun:
                    variant_matched = 1
                    break
        if variant_matched == 0:
            unique_variant_values.append([object.variantName, object.printRun])

    unique_variant_values_object = []

    for variant in unique_variant_values:
        variant_objects = [variant[0], variant[1], []]
        for object in category_objects:
            if object.variantName == variant[0]:
                if object.printRun == variant[1]:
                    variant_objects[2].append(convert_checklist_object_to_row(object))
        write_to_csv_file("exports/variants/" + category + "/" + variant[0] + "_" + variant[1] + ".csv", variant_objects[2])


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
