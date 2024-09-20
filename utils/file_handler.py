import os

def read_gospider_output(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()


def read_gospider_output(input_file):
    with open(input_file, 'r') as file:
        return file.readlines()


def save_categorized_urls(categories, output_directory, args):

    if not os.path.exists(output_directory):
        os.makedirs(output_directory, exist_ok=True)

    selected_categories = []
    if args.all:
        selected_categories = list(categories.keys())
    else:
        if args.subdomains:
            selected_categories.append('subdomains')
        if args.href:
            selected_categories.append('href')
        if args.js:
            selected_categories.append('javascript')
        if args.forms:
            selected_categories.append('form')
        if args.others:
            selected_categories.append('others')
        if not selected_categories:
            selected_categories.append('url')

    for category in selected_categories:
        filename = os.path.join(output_directory, f"{category}.txt")
        with open(filename, 'w') as f:
            for url in categories[category]:
                f.write(f"{url}\n")

    print(f"Saved categorized URLs to {output_directory}")
