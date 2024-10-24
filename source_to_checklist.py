
def convert_source_products_to_checklist_objects(source_products, set_name):
    checklist_objects = []
    for product in source_products:

# Check if source_product.productName contains [].
## If so, get all text before [ and strip() = Player name.
## Get all values between [] and strip() = Variant name.
# Get values connected to # and strip() = card number.
# source_product.printRun = print run.
# set_name = set name.