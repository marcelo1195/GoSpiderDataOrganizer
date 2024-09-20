import re
import os
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def categorize_urls_subset(lines, exclude_400=False):
    categories = {
        'subdomains': [],
        'href': [],
        'javascript': [],
        'form': [],
        'url': [],
        'others': []
    }

    url_pattern = re.compile(r'https?://\S+')

    for line in lines:
        line = line.strip()
        if exclude_400 and '[code-4' in line:
            continue

        if line.startswith('[subdomains]'):
            url = line.split(' - ', 1)[1]
            categories['subdomains'].append(url)
        elif line.startswith('[href]'):
            url = line.split(' - ', 1)[1]
            categories['href'].append(url)
        elif line.startswith('[javascript]'):
            url = line.split(' - ', 1)[1]
            categories['javascript'].append(url)
        elif line.startswith('[form]'):
            url = line.split(' - ', 1)[1]
            categories['form'].append(url)
        elif line.startswith('[url]'):
            match = url_pattern.search(line)
            if match:
                url = match.group(0)
                categories['url'].append(url)
        else:
            match = url_pattern.search(line)
            if match:
                url = match.group(0)
                categories['others'].append(url)

    for category in categories:
        categories[category] = list(set(filter(is_valid_url, categories[category])))

    return categories


def categorize_urls_threaded(lines, exclude_400=False, num_threads=10):
    chunk_size = len(lines) // num_threads
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    results = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_chunk = {executor.submit(categorize_urls_subset, chunk, exclude_400): chunk for chunk in chunks}
        for future in as_completed(future_to_chunk):
            results.append(future.result())

    # Combinar resultados
    combined_categories = {
        'subdomains': [],
        'href': [],
        'javascript': [],
        'form': [],
        'url': [],
        'others': []
    }

    for result in results:
        for category, urls in result.items():
            combined_categories[category].extend(urls)

    # Remove duplicates and invalid URLs
    for category in combined_categories:
        combined_categories[category] = list(set(filter(is_valid_url, combined_categories[category])))

    return combined_categories


def save_categorized_urls(categories, output_dir, args):
    # Cria o diretório de saída se ele não existir
    os.makedirs(output_dir, exist_ok=True)

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
        filename = os.path.join(output_dir, f"{category}.txt")
        with open(filename, 'w') as f:
            for url in categories[category]:
                f.write(f"{url}\n")

    print(f"Saved categorized URLs to {output_dir}")
