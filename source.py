import requests
from bs4 import BeautifulSoup

from source_product import source_product
from source_set import source_set

def fetch_set_results(set_identifier):
    set_name = fetch_set_name(set_identifier)
    print("Got the set name for " + set_identifier)

    set_results = []

    initial_result_set = fetch_initial_set_results(set_identifier)
    print("Got the initial set results for " + set_identifier)
    products = extract_products_from_results(initial_result_set)
    print("Got the products  for " + set_identifier)
    set_results += convert_json_response_source_products(products)
    print("Got the set results for " + set_identifier)

    #'''
    counter = 1
    poll_set = True
    while poll_set == True:
        print("Fetch results with counter for " + set_identifier + " - " + counter.__str__())
        #print("Starting iteration for counter ", counter.__str__())
        counter_results = fetch_set_results_by_counter(set_identifier,counter)
        counter_results_products = extract_products_from_results(counter_results)
        if len(counter_results_products) == 0:
            print("No results found for counter ", counter.__str__())
            poll_set = False
            break
        set_results += convert_json_response_source_products(counter_results_products)
        #print("Finised iteration for counter ", counter.__str__())
        counter += 1
        print("Finished results with counter for " + set_identifier + " - " + counter.__str__())
    #'''
    return set_results, set_name

def fetch_initial_set_results(set_identifier):
    url = "https://www.sportscardspro.com/console/{set_identifier}?sort=model-number&model-number=&rookies-only=false&exclude-variants=false&format=json"
    url = url.replace("{set_identifier}", set_identifier)
    return requests.get(url)

def extract_products_from_results(response):
    response_json = response.json()
    return response_json.get('products')

def convert_json_response_source_products(products):
    source_products = []

    for product in products:
        source_products.append(source_product(product.get('printRun'), product.get('productName'), product.get('id')))

    return source_products

def fetch_set_results_by_counter(set_identifier, cursor):
    cursor_to_replace = cursor * 50
    url = "https://www.sportscardspro.com/console/{set_identifier}?sort=model-number&when=none&exclude-variants=false&rookies-only=false&cursor={cursor_value}&format=json"
    url = url.replace("{set_identifier}", set_identifier)
    url = url.replace("{cursor_value}", cursor_to_replace.__str__())
    return requests.get(url)

def fetch_set_name(set_identifier):
    url = f"https://www.sportscardspro.com/console/{set_identifier}"
    url = url.replace("{set_identifier}", set_identifier)
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    set_name = soup.find(id='console-header').find('h1').text.strip()
    set_name = set_name.replace("Prices for ","")
    set_name = set_name.replace("Cards", "")
    return set_name

def fetch_all_set_identifiers_for_category(category_identifier):
    response = fetch_category_page(category_identifier)
    return extract_set_identifier_list(response)

def fetch_category_page(category_identifier):
    url = f"https://www.sportscardspro.com/category/{category_identifier}"
    url = url.replace("{category_identifier}", category_identifier)
    return requests.get(url)

def extract_set_identifier_list(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    home_box_soup = soup.find(class_="home-box all")
    set_list_soup = home_box_soup.find_all("li")
    source_set_list = []
    for set_list_soup_item in set_list_soup:
        source_set_list.append(source_set(set_list_soup_item.text.strip(),
                                          set_list_soup_item.find("a").get("href").replace("/console/","")))

    return source_set_list