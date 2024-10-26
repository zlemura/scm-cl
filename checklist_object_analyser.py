

def analyse_variant_values_in_checklist_objects(checklist_objects, set_identifier, variant_master_list):
    variant_counter = []

    #print("Processing ", set_identifier)


    for object in checklist_objects:
        if len(object.variantName) == 0:
            continue
        variant_matched = 0
        #print("Going to try and match ", object.variantName, " PR ", object.printRun)
        for variant in variant_counter:
            if variant.variantName == object.variantName:
                if variant.printRun == object.printRun:
                    variant_matched = 1
                    #print("Matched to " ,variant.variantName)
                    #print("Value matched ", object.variantName)
                    variant.increase_total()
        if variant_matched == 0:
            variant_counter.append(variant_analysis(object.variantName, object.printRun))
            #print("added a new variant!")

    '''
    variant_counter_total = 0
    for variant in variant_counter:
        print(variant.variantName)
        print(variant.printRun)
        print(variant.total)
        if variant.total == 0:
            variant_counter_total += 1
        else:
            variant_counter_total += (variant.total + 1)
    '''

    variant_master_list += apppend_unique_variant_values_to_master(variant_counter, variant_master_list)
    return variant_master_list

def apppend_unique_variant_values_to_master(variant_list, variant_master_list):
    for variant in variant_list:
        variant_matched = 0
        for variant_master in variant_master_list:
            if variant.variantName == variant_master.variantName and variant.printRun == variant_master.printRun:
                variant_matched = 1
                break
        if variant_matched == 0:
            variant_master_list.append(variant)
    return variant_master_list

class variant_analysis:
    def __init__(self, variantName, printRun):
        self.variantName = variantName
        self.printRun = printRun
        self.total = 0

    def increase_total(self):
        self.total += 1
        #print("Total is now " + self.total.__str__())