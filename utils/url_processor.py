import re
import os
from urllib.parse import urlparse


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def categorize_urls(lines, exclude_400=False):
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

    # Remove duplicates and invalid URLs
    for category in categories:
        categories[category] = list(set(filter(is_valid_url, categories[category])))

    return categories


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
