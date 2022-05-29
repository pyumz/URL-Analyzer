def remove_none_values(dict):
    remove_keys = []

    for key, value in dict.items():
        if value is None:
            remove_keys.append(key)
    
    for key in remove_keys:
        del dict[key]
    
    return dict

def sort_pages(pages):
    sorted_pages = []

    for key, value in pages.items():
        sorted_pages.append((key, value))

    sorted_pages.sort(reverse=True)
    return sorted_pages

def print_report(pages):
    pages = remove_none_values(pages)
    page_list = sort_pages(pages)

    for page in page_list:
        url = page[0]
        count = page[1]
        print("Found {} internal links to {}".format(count, url))
