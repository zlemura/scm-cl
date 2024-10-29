import os

import pickle_actions as pickle

def analyse_variants_in_category_checklist_objects(category_identifier):
    checklist_files = os.listdir("checklists/" + category_identifier)
    total_checklist_files = len(checklist_files)
    checklist_files = reversed(checklist_files)

    variant_master_list = []
    processed_file_counter = 0
    for file in checklist_files:
        print("Processing ", file, "(", processed_file_counter.__str__(), "/", total_checklist_files.__str__(), ")")
        file_checklist_objects = pickle.open_dump_file(
            "checklists/" + category_identifier + "/" + file.replace(".pkl", ""))
        variant_master_list = analyse_variant_values_in_checklist_objects(
            file_checklist_objects,
            file.replace(".pkl", ""),
            variant_master_list)

        print("Processed file ", file, "(", processed_file_counter.__str__(), "/", total_checklist_files.__str__(), ")")
        processed_file_counter += 1

    '''
    print("Found a total of ", len(variant_master_list).__str__(), " unique variant values in category.")

    for variant_master in variant_master_list:
        print(variant_master.variantName)
        print(variant_master.printRun)
    '''
    pickle.write_to_dump_file(variant_master_list, "checklists/variants/" + category_identifier)


def analyse_variant_values_in_checklist_objects(checklist_objects, set_identifier, variant_master_list):
    objects_with_variant_counter = 0
    objects_with_print_run_counter = 0
    variants_to_add_to_master_list = []

    #print("Processing ", set_identifier)

    for object in checklist_objects:
        # If no variantName, skip iteration.
        if len(object.variantName) == 0:
            continue
        if object.printRun != None:
            if object.printRun > 0:
                objects_with_print_run_counter += 1
        objects_with_variant_counter += 1
        variants_to_add_to_master_list.append(variant_analysis(object.variantName, object.printRun))
        variant_matched = 0
        for variant in variants_to_add_to_master_list:
            if variant.variantName == object.variantName:
                if (variant.printRun == object.printRun) or (variant.printRun == None and object.printRun == None):
                    variant_matched = 1
                    break
        if variant_matched == 0:
            variants_to_add_to_master_list.append(variant_analysis(object.variantName, object.printRun))

    existing_master_list = variant_master_list
    for variant in variants_to_add_to_master_list:
        if determine_if_variant_in_variant_master_list(variant, existing_master_list) == False:
            variant_master_list.append(variant)

    return variant_master_list

def determine_if_variant_in_variant_master_list(variant, variant_master_list):
    variant_matched_in_master_list = False
    for variant_master_list_object in variant_master_list:
        if variant.variantName == variant_master_list_object.variantName:
            if (variant.printRun == variant_master_list_object.printRun) or (variant.printRun == None and variant_master_list_object.printRun == None):
                variant_matched_in_master_list = True
                break

    return variant_matched_in_master_list

def apppend_unique_variant_values_to_master(variant_list, variant_master_list):
    unique_variants_found = 0
    for variant in variant_list:
        variant_matched = 0
        for variant_master in variant_master_list:
            if variant.variantName == variant_master.variantName and variant.printRun == variant_master.printRun:
                variant_matched = 1
                break
        if variant_matched == 0:
            variant_master_list.append(variant)
            unique_variants_found += 1

    print("Added a total of ", unique_variants_found.__str__(), " variants to the master variant list!")
    return variant_master_list

def determine_if_variant_exists_in_master_list(variant_to_check, variant_master_list):
    #print(type(variant_master_list))
    variant_matched = 0
    for variant_master_record in variant_master_list:
        variant_master_variantName = variant_master_record.variantName.__str__
        variant_master_printRun = variant_master_record.printRun
        #print("About to try and match ", type(variant_master_record))
        if variant_to_check.variantName == variant_master_variantName:
            if variant_to_check.printRun == variant_master_printRun:
                variant_matched = 1
                break

    return variant_matched

def validate_checklist_objects_against_variants_per_category():
    category_identifiers = ["baseball-cards", "basketball-cards", "football-cards", "hockey-cards", "soccer-cards",
                            "racing-cards", "wrestling-cards", "ufc-cards"]

    processing_errors = []

    for category in category_identifiers:
        print("Processing ", category)
        checklist_object_files = os.listdir("checklists/" + category)
        category_variants = pickle.open_dump_file("checklists/variants/" + category)
        for file in checklist_object_files:
            print("Processing ", file)
            file_checklist_objects = pickle.open_dump_file("checklists/" + category + "/" + file.replace(".pkl", ""))
            for object in file_checklist_objects:
                if len(object.variantName) > 0:
                    variant_matched = 0
                    for variant in category_variants:
                        if variant.variantName == object.variantName:
                            if variant.printRun == object.printRun:
                                variant_matched = 1
                                break
                    if variant_matched == 0:
                        print("Wasn't able to find this object's variant in variant list!")
                        print(object.__dict__)
                        processing_errors.append(object)
            print("Processed ", file)
        print("Processed ", category)

    for object in processing_errors:
        print("Couldn't match this object to a variant.")
        print(object.__dict__)

class variant_analysis:
    def __init__(self, variantName, printRun):
        self.variantName = variantName
        self.printRun = printRun
        self.total = 0

    def increase_total(self):
        self.total += 1
        #print("Total is now " + self.total.__str__())