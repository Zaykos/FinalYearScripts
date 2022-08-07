import requestUtils
import json


def fuzzing_php_info(target_url, header):
    with open('dictionaryLists/phpList.json', 'r') as php_list_file:
        file_data = json.load(php_list_file)

    php_fuzzing_paths = file_data.phpInfoList.list
    found_paths = []

    for i in php_fuzzing_paths:
        new_url = "http://" + target_url + "/" + i
        response_code = requestUtils.request_code(new_url, header)
        if response_code == 200:
            found_paths.append(i)
        else:
            pass
    if len(found_paths) >= 1:
        print("We found a PHPInfo !")
        for t in found_paths:
            print("-> ", t)
