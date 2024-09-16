def search_json(json_data, search_string):
    # Place your search code here
    for i in json_data:
        for j in i:
            if i[j] == search_string:
                return i

