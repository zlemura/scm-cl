import pickle_actions as pickle

import csv
import os
import re
import uuid


def export_category_checklist_objects(category):
    '''
    print("Creating set files for category!")
    create_set_files_for_category(category)
    print("Created set files for category!")
    '''

    print("Fetching objects for category!")
    category_objects = fetch_all_objects_for_category(category)
    print("Fetched objects for category!")

    print("Creating player name files for category!")
    create_player_name_files_for_category_by_player_name(category_objects, category)
    print("Created player name files for category!")

    print("Creating variant files for category!")
    create_variant_files_for_category(category_objects, category, 1990)
    print("Created variant files for category!")

    print("Creating print run files for category!")
    create_print_run_files_for_category(category_objects, category)
    print("Created print run files for category!")

    print("Creating player names enum list for category!")
    create_player_names_enums_list(category)
    print("Created player names enum list for category!")

    print("Creating variant enum list for category!")
    create_variants_enums_list(category)
    print("Created variant enum list for category!")

    print("Creating set name enum list for category!")
    create_set_names_enum_list(category)
    print("Created set name enum list for category!")

    print("Creating print run enum list for category!")
    create_print_run_enum_list(category)
    print("Created print run enum list for category!")


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
        try:
            os.mkdir("exports/sets/" + category)
        except FileExistsError:
            print("Directory exists for ", category)

        write_to_csv_file("exports/sets/" + category + "/" + str(uuid.uuid4()) + ".csv",
                          objects_to_add_to_file)
        print("Processed ", file_name)


def create_player_name_files_for_category_by_player_name(category_objects, category):
    unique_player_name_values = []

    try:
        os.mkdir("exports/player_names/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    for object in category_objects:
        if len(object.playerName) == 0:
            continue
        '''
        if '2024 Topps Baseball' not in object.setName:
            continue
        '''
        print("Processing ", object.__dict__)
        player_name_matched = 0
        for player_name in unique_player_name_values:
            if player_name[0].lower() == object.playerName.lower():
                player_name_matched = 1
                player_name[1].append(convert_checklist_object_to_row(object))
                break
        if player_name_matched == 0:
            row_object = convert_checklist_object_to_row(object)
            unique_player_name_values.append([row_object[0], [row_object]])
        print("Processed ", object.__dict__)

    try:
        os.mkdir("exports/player_names/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    for player_name in unique_player_name_values:
        objects_to_add_to_file = []
        player_name_for_char = player_name[0]
        first_char_of_player_name = player_name_for_char[0].lower()
        try:
            os.mkdir("exports/player_names/" + category + "/" + first_char_of_player_name)
        except FileExistsError:
            pass
            #print("Directory exists for ", first_char_of_player_name)
        for object in player_name[1]:
            objects_to_add_to_file.append(object)
        if len(objects_to_add_to_file) == 0:
            print("Found an empty list!")
            print(player_name)
        write_to_csv_file("exports/player_names/" + category + "/" + first_char_of_player_name + "/" + str(uuid.uuid4()) + ".csv", objects_to_add_to_file)

    '''
    for player_name in unique_player_name_values:
        print(player_name[0])
        print(len(player_name[1]))
    '''


def create_player_name_files_for_category_by_letter(category_objects, category):
    a = ['a', []]
    b = ['b', []]
    c = ['c', []]
    d = ['d', []]
    e = ['e', []]
    f = ['f', []]
    g = ['g', []]
    h = ['h', []]
    i = ['i', []]
    j = ['j', []]
    k = ['k', []]
    l = ['l', []]
    m = ['m', []]
    n = ['n', []]
    o = ['o', []]
    p = ['p', []]
    q = ['q', []]
    r = ['r', []]
    s = ['s', []]
    t = ['t', []]
    u = ['u', []]
    v = ['v', []]
    w = ['w', []]
    x = ['x', []]
    y = ['y', []]
    z = ['z', []]

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

    all_letters = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

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
        try:
            os.mkdir("exports/player_names/" + category + "/" + current_letter)
        except FileExistsError:
            print("Directory exists for ", current_letter)
        write_to_csv_file("exports/player_names/" + category + "/" + current_letter + "/" + str(uuid.uuid4()) + ".csv",
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


def create_variant_files_for_category(category_objects, category,year_limit):
    unique_variant_values = []

    for object in category_objects:
        if len(object.variantName) == 0:
            continue
        if fetch_year_from_set_name(object.setName) < year_limit:
            continue
        variant_matched = 0
        for variant in unique_variant_values:
            if variant[0] == object.variantName:
                if variant[1] == object.printRun:
                    variant_matched = 1
                    variant[2].append(object)
                    print("Matched an existing variant!")
                    print(variant[0], variant[1])
                    break
        if variant_matched == 0:
            unique_variant_values.append([object.variantName, object.printRun, [object]])
            print("Added a new variant to the list!")
            print(object.variantName, object.printRun)

    try:
        os.mkdir("exports/variants/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    for variant in unique_variant_values:
        variant_name = variant[0].strip()
        variant_print_run = str(variant[1])
        variant_objects = variant[2]
        print("Processing ", variant_name, variant_print_run)
        objects_to_add_to_file = []
        first_char_of_variant_name = variant_name[0].lower()
        for object in variant_objects:
            objects_to_add_to_file.append(convert_checklist_object_to_row(object))
        try:
            os.mkdir("exports/variants/" + category + "/" + first_char_of_variant_name)
        except FileExistsError:
            print("Directory exists for ", first_char_of_variant_name)
        write_to_csv_file("exports/variants/" + category + "/" + first_char_of_variant_name + "/" + str(uuid.uuid4()) + ".csv", objects_to_add_to_file)
        print("Processed ", variant[0], variant[1])


def create_print_run_files_for_category(category_objects, category):
    print_run_values = []

    for object in category_objects:
        if object.printRun == None:
            continue
        if object.printRun < 1:
            continue
        print_run_matched = 0
        for print_run in print_run_values:
            if print_run[0] == object.printRun:
                print_run_matched = 1
                print_run[1].append(convert_checklist_object_to_row(object))
                continue
        if print_run_matched == 0:
            print_run_values.append([object.printRun, [convert_checklist_object_to_row(object)]])

    try:
        os.mkdir("exports/print_runs/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    for print_run in print_run_values:
        write_to_csv_file("exports/print_runs/" + category + "/" + str(uuid.uuid4()) + ".csv", print_run[1])

def create_player_names_enums_list(category):
    enum_list_values = []

    player_names_file_path = "exports/player_names/"
    category_letter_directory_names = os.listdir(player_names_file_path + category)
    for category_letter in category_letter_directory_names:
        print("Processing ", category_letter)
        category_letter_files = os.listdir(player_names_file_path + category + "/" + category_letter)
        for category_letter_file in category_letter_files:
            first_record = get_first_record_in_csv(player_names_file_path + category + "/" + category_letter + "/" + category_letter_file)
            if len(first_record) > 1:
                combined_first_record = ''
                for record in first_record:
                    combined_first_record += record
                first_record_split = combined_first_record.split("|")
            else:
                first_record_split = first_record[0].split("|")
            print(first_record_split)
            enum_list_values.append([first_record_split[0], category_letter_file.replace(".csv","")])
        print("Processed ", category_letter)

    enums_to_add_to_file = []
    for enum in enum_list_values:
        enums_to_add_to_file.append((enum[0],enum[1]))

    try:
        os.mkdir("exports/enums/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    write_to_csv_file("exports/enums/" + category + "/player_names.csv", enums_to_add_to_file)

def create_variants_enums_list(category):
    enum_list_values = []

    variants_file_path = "exports/variants/"
    category_variant_directory_names = os.listdir(variants_file_path + category)
    for category_directory in category_variant_directory_names:
        print("Processing ", category_directory)
        category_directory_files = os.listdir(variants_file_path + category + "/" + category_directory)
        for category_directory_file in category_directory_files:
            #print(category_directory_file)
            first_record = get_first_record_in_csv(variants_file_path + category + "/" + category_directory + "/" + category_directory_file)
            if len(first_record) > 1:
                combined_first_record = ''
                for record in first_record:
                    combined_first_record += record
                first_record_split = combined_first_record.split("|")
            else:
                first_record_split = first_record[0].split("|")
            #print(first_record_split)
            enum_list_values.append([first_record_split[1], category_directory_file.replace(".csv", "")])
        print("Processed ", category_directory)

    enums_to_add_to_file = []
    for enum in enum_list_values:
        enums_to_add_to_file.append((enum[0], enum[1]))

    try:
        os.mkdir("exports/enums/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    write_to_csv_file("exports/enums/" + category + "/variants.csv", enums_to_add_to_file)

def create_set_names_enum_list(category):
    enum_list_values = []

    set_names_file_path = "exports/sets/"
    category_set_names_directory_names = os.listdir(set_names_file_path + category)
    for category_set_file_name in category_set_names_directory_names:
        first_record = get_first_record_in_csv(set_names_file_path + category + "/" + category_set_file_name)
        if len(first_record) > 1:
            combined_first_record = ''
            for record in first_record:
                if len(record) == 0:
                    continue
                combined_first_record += record
            first_record_split = combined_first_record.split("|")
        else:
            first_record_split = first_record[0].split("|")
        if len(first_record_split[4]) > 0:
            enum_list_values.append([first_record_split[4], category_set_file_name.replace(".csv", "")])

    enums_to_add_to_file = []
    for enum in enum_list_values:
        enums_to_add_to_file.append((enum[0], enum[1]))

    try:
        os.mkdir("exports/enums/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    write_to_csv_file("exports/enums/" + category + "/sets.csv", enums_to_add_to_file)

def create_print_run_enum_list(category):
    enum_list_values = []

    print_run_file_path = "exports/print_runs/"

    category_print_runs_directory_names = os.listdir(print_run_file_path + category)

    for category_print_run_file_name in category_print_runs_directory_names:
        first_record = get_first_record_in_csv(print_run_file_path + category + "/" + category_print_run_file_name)
        if len(first_record) > 1:
            combined_first_record = ''
            for record in first_record:
                if len(record) == 0:
                    continue
                combined_first_record += record
            first_record_split = combined_first_record.split("|")
        else:
            first_record_split = first_record[0].split("|")
        enum_list_values.append([first_record_split[3], category_print_run_file_name.replace(".csv", "")])

    enums_to_add_to_file = []
    for enum in enum_list_values:
        enums_to_add_to_file.append((enum[0], enum[1]))

    try:
        os.mkdir("exports/enums/" + category)
    except FileExistsError:
        print("Directory exists for ", category)

    write_to_csv_file("exports/enums/" + category + "/print_runs.csv", enums_to_add_to_file)

def convert_checklist_object_to_row(checklist_object):
    year = fetch_year_from_set_name(checklist_object.setName)
    manufacturer = fetch_manufacturer_from_set_name(checklist_object.setName).strip()
    playerName = checklist_object.playerName.strip()
    variant_name = checklist_object.variantName.strip()
    card_number = checklist_object.cardNumber.strip()
    print_run = checklist_object.printRun
    set_name = checklist_object.setName.strip()

    # Replace entire player names if required.
    player_names_to_check_and_replace = [("?ukasz Piszczek", "Lukasz Piszczek"),
                                         ("Wojciech Szcz?sny", "Wojciech Szczesny"),
                                         ("Connor mcgregor","Conor McGregor")]

    for player_name in player_names_to_check_and_replace:
        if player_name[0] == playerName:
            playerName = player_name[1]

    characters_to_remove = [("ō", "o"), ("⁰", "o"), ("ć", "c"), ("Ş", "s"), ("⁸","8"), ("č","c"), ("Ś","S"), ("Č","C"),
                            ("ĺ","l"),("ϋ","u"),("і","i"), ("?",""), ("ę","e"),("ł","l")]
    for character in characters_to_remove:
        if character[0] in playerName:
            playerName = playerName.replace(character[0], character[1])
        if character[0] in variant_name:
            variant_name = variant_name.replace(character[0], character[1])
        if character[0] in card_number:
            card_number = card_number.replace(character[0], character[1])
        if character[0] in set_name:
            set_name = set_name.replace(character[0], character[1])

    '''
    print(playerName, variant_name , card_number, print_run, set_name, year, manufacturer)
    '''

    return playerName, variant_name , card_number, print_run, set_name, year, manufacturer


def fetch_year_from_set_name(setName):
    year = int(setName.split(" ")[0])
    return year


def fetch_manufacturer_from_set_name(setName):
    product_list = ["Bowman", "Donruss", "Finest", "Score", "Stadium Club",
                    "Upper Deck", "Hoops", "Skybox", "Ultra", "O-Pee-Chee", "Collector's Choice", "Metal", "Pro Set",
                    "Wild Card", "Select", "Pacific", "Prestige", "Playoffs", "Parkhurst", "St. Lawrence Sales",
                    "Pinnacle", "SP Authentic", "SP", "Ultimate Collection", "Parkside", "All Stars", "Monty Gum", "Scanlens",
                    "Wonderama", "Classic WWF", "Impel WCW", "Merlin WWF", "Cardz", "WWF Magazine", "TriStar"]

    manufacturer_list = ["Topps", "Panini", "Futera", "Leaf", "Fleer"]

    for product in product_list:
        if product in setName:
            return product

    for manufacturer in manufacturer_list:
        if manufacturer in setName:
            return manufacturer

    subs = [("O Pee Chee", "O-Pee-Chee")]

    for sub in subs:
        if sub[0] in setName:
            return sub[1]

    print("DIDNT FIND A MANUFACTURER OR PRODUCT IN ", setName)
    SystemExit.code(1)


def write_to_csv_file(file_name, objects_to_write):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(objects_to_write)

def get_first_record_in_csv(file_path):
    with open(file_path, mode='r') as file:
        csvFile = csv.reader(file)
        first_record = None
        for line in csvFile:
            if first_record == None:
                first_record = line
            else:
                break

    return first_record



class object_csv_structure:
    def __init__(self, playerName, variantName, cardNumber, printRun, setName, setYear, setManufacturer):
        self.playerName = playerName
        self.variantName = variantName
        self.cardNumber = cardNumber
        self.printRun = printRun
        self.setName = setName
        self.setYear = setYear
        self.setManufacturer = setManufacturer