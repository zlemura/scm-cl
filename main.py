import checklist_object_export as checklist_object_export
import source as source
import source_to_checklist as source_to_checklist
import cloudflare_actions

'''
To extract data from source.
1. Create a variable called 'category' that has one of the following values - baseball-cards, basketball-cards, football-cards,
   hockey-cards, racing-cards, soccer-cards, ufc-cards, wrestling-cards.
2. Call source.fetch_set_results_for_category(category) - this will fetch all set names (source_set) for the category, save them and then
   loop through each set for the category and fetch the source results (source_product).
3. Call source_to_checklist.convert_set_products_to_checklist_objects_by_category(category) - this will convert all source_product results
   into checklist_object results. These results will then be saved.
4. Call checklist_object_export.export_category_checklist_objects(category) - this will convert the checklist_object values for each
   set in the category into CSV files in a structure that can be used for the website.
'''

def run():

    category = 'basketball-cards'
    #cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[a-d]")
    #cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[e-h]")
    #cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[i-o]")
    #cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[p-t]")
    #cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[u-z]")
    #cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[a-d]")
    #cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[e-h]")
    #cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[i-o]")
    #cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[p-t]")
    #cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[u-z]")
    #cloudflare_actions.upload_print_run_files_for_category_to_r2(category)
    #cloudflare_actions.upload_set_files_for_category_to_r2(category)



    '''
    category = ''
    # source.fetch_set_results_for_category(category)
    # source_to_checklist.convert_set_products_to_checklist_objects_by_category(category)
    checklist_object_export.export_category_checklist_objects(category)
    '''
if __name__ == '__main__':
    run()