# Import python packages
from dataplane import s3_upload
import os
import boto3
from botocore.client import Config
import json

import boto3
import os
from botocore.exceptions import ClientError
import re
import asyncio
import awswrangler as wr

account_id = '9c9562992189c11df6189a83f16e8229'
access_key_id = '3527846a86da1b2f883ff56278fa75ec'
access_key_secret = 'f265d9c69d7d121c2c4c87050c0a99710e0428cb062e60bddf9d5ddb98e08b44'

r2 = boto3.client('s3',
                  endpoint_url=f'https://{account_id}.r2.cloudflarestorage.com',
                  aws_access_key_id=access_key_id,
                  aws_secret_access_key=access_key_secret
                  )

def get_objects_in_bucket(bucket_name):
    s3 = boto3.resource('s3',
                        endpoint_url=f'https://{account_id}.r2.cloudflarestorage.com',
                        aws_access_key_id=access_key_id,
                        aws_secret_access_key=access_key_secret
                        )
    my_bucket = s3.Bucket(bucket_name)
    object_summary = my_bucket.objects.all()
    counter = 0
    for obj in object_summary:
        counter+= 1

    print("There are " + str(counter)  + " objects in the bucket - " + bucket_name)

def upload_files_for_category(category):
    '''
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit functions for execution
        futures = [executor.submit(upload_player_name_files_for_category_to_r2,category, "[a-d]"),
                   executor.submit(upload_player_name_files_for_category_to_r2,category, "[e-h]"),
                   executor.submit(upload_player_name_files_for_category_to_r2, category, "[i-o]"),
                   executor.submit(upload_player_name_files_for_category_to_r2, category, "[p-t]"),
                   executor.submit(upload_player_name_files_for_category_to_r2, category, "[u-z]"),
                   executor.submit(upload_variant_files_for_category_to_r2, category, "[a-d]"),
                   executor.submit(upload_variant_files_for_category_to_r2, category, "[e-h]"),
                   executor.submit(upload_variant_files_for_category_to_r2, category, "[i-o]"),
                   executor.submit(upload_variant_files_for_category_to_r2, category, "[p-t]"),
                   executor.submit(upload_variant_files_for_category_to_r2, category, "[u-z]"),
                   executor.submit(upload_print_run_files_for_category_to_r2, category),
                   executor.submit(upload_set_files_for_category_to_r2, category)]

        print("Staring futures.")
        concurrent.futures.wait(futures)
        print("Finished futures.")
    '''
    '''
        Thread(target = cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[a-d]")).start()
        Thread(target = cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[e-h]")).start()
        Thread(target = cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[i-o]")).start()
        Thread(target = cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[p-t]")).start()
        Thread(target = cloudflare_actions.upload_player_name_files_for_category_to_r2(category, "[u-z]")).start()
        Thread(target = cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[a-d]")).start()
        Thread(target = cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[e-h]")).start()
        Thread(target = cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[i-o]")).start()
        Thread(target = cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[p-t]")).start()
        Thread(target = cloudflare_actions.upload_variant_files_for_category_to_r2(category, "[u-z]")).start()
        Thread(target = cloudflare_actions.upload_print_run_files_for_category_to_r2(category)).start()
        Thread(target = cloudflare_actions.upload_set_files_for_category_to_r2(category)).start()
        '''



def upload_file(file_name, bucket_name, object_name):
    try:
        r2.upload_file(file_name, bucket_name, object_name)
        print(file_name + " upload complete!")
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False
    return True

def delete_object(bucket_name, object_id):
    try:
        r2.delete_object(Bucket= bucket_name, Key = object_id)
        print(object_id + " delete complete!")
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False
    return True

def get_bucket_objects(bucket_name):
    try:
        response = r2.list_objects_v2(Bucket=bucket_name)
        response_content = response.get('Contents')
        #print(object_id + " delete complete!")
    except ClientError as e:
        print(f"An error occurred: {e}")
        return None
    key_list = []
    for item in response_content:
        key_list.append(item.get("Key"))
    return key_list

def delete_objects_in_bucket(bucket_name):
    objects_detected = True
    increment_counter = 1
    while objects_detected:

        try:
            bucket_objects = get_bucket_objects(bucket_name)
        except:
            objects_detected = False
            break

        number_of_objects = len(bucket_objects) + 1
        counter = 1

        for object in bucket_objects:
            print("Deleting object " + str(counter) + " of " + str(number_of_objects) + " for " + bucket_name)
            delete_object(bucket_name, object)
            counter += 1
        print("Finished the " + str(increment_counter) + " increment.")
        print("Deleted a total of " + str(increment_counter * 1000) + " objects so far.")
        increment_counter += 1

def upload_files_for_category(category):
    async def upload_files_for_category_coroutine():
        # sleep for a moment
        await asyncio.sleep(1)
        upload_player_name_files_for_category_to_r2(category, "[a-d]")
        print("a-d player name upload started async.")
        upload_player_name_files_for_category_to_r2(category, "[e-h]")
        print("e-h player name upload started async.")
        upload_player_name_files_for_category_to_r2(category, "[i-o]")
        print("i-o player name upload started async.")
        upload_player_name_files_for_category_to_r2(category, "[p-t]")
        print("p-t player name upload started async.")
        upload_player_name_files_for_category_to_r2(category, "[u-z]")
        print("u-z player name upload started async.")
        upload_variant_files_for_category_to_r2(category)
        print("Variant upload started async.")
        upload_print_run_files_for_category_to_r2(category)
        print("Print run upload started async.")
        upload_set_files_for_category_to_r2(category)
        print("Set upload started async.")
    asyncio.run(upload_files_for_category_coroutine())


def upload_player_name_files_for_category_to_r2(category, character_range):
    player_name_directory_for_category = 'exports/player_names/' + category

    print("Now uploading player name files in range ", character_range)

    player_name_category_folders = os.listdir(player_name_directory_for_category)

    for folder in player_name_category_folders:
        if character_range != None:
            if bool(re.search(character_range,folder)) == 0:
                continue
        if character_range == None:
            if folder.isalpha() == True:
                continue
        folder_path = player_name_directory_for_category + "/" + folder
        folder_files = os.listdir(folder_path)
        for file in folder_files:
            file_path = folder_path + "/" + file
            upload_file(file_path, 'scm-cl-' + category, file)

def upload_variant_files_for_category_to_r2(category, character_range):
    variant_directory_for_category = 'exports/variants/' + category

    variant_category_folders = os.listdir(variant_directory_for_category)

    for folder in variant_category_folders:
        if character_range != None:
            if bool(re.search(character_range, folder)) == 0:
                continue
        if character_range == None:
            if folder.isalpha() == True:
                continue
        folder_path = variant_directory_for_category + "/" + folder
        folder_files = os.listdir(folder_path)
        for file in folder_files:
            file_path = folder_path + "/" + file
            upload_file(file_path, 'scm-cl-' + category, file)

def upload_print_run_files_for_category_to_r2(category):
    print_run_directory_for_category = 'exports/print_runs/' + category

    print_run_category_files = os.listdir(print_run_directory_for_category)

    for file in print_run_category_files:
        file_path = print_run_directory_for_category + "/" + file
        upload_file(file_path, 'scm-cl-' + category, file)

def upload_set_files_for_category_to_r2(category):
    set_directory_for_category = 'exports/sets/' + category

    set_category_files = os.listdir(set_directory_for_category)

    for file in set_category_files:
        file_path = set_directory_for_category + "/" + file
        upload_file(file_path, 'scm-cl-' + category, file)
