import argparse
import sys
import os
from utils.file_handler import read_gospider_output
from utils.url_processor import categorize_urls, save_categorized_urls

def main():
    parser = argparse.ArgumentParser(description="Gospider output processor")
    parser.add_argument("-I", "--input-file", required=True, help="Path to the gospider output file")
    parser.add_argument("-O", "--output-dir", required=True, help="Full path to the directory to save categorized URL lists")
    parser.add_argument("--exclude-400", action="store_true", help="Exclude URLs with 400-class codes")
    parser.add_argument("-J", "--js", action="store_true", help="Select only JavaScript URLs")
    parser.add_argument("-H", "--href", action="store_true", help="Select only href URLs")
    parser.add_argument("-S", "--subdomains", action="store_true", help="Select only subdomains")
    parser.add_argument("-F", "--forms", action="store_true", help="Select only form URLs")
    parser.add_argument("-U", "--others", action="store_true", help="Select other uncategorized URLs")
    parser.add_argument("-A", "--all", action="store_true", help="Select all types of URLs")
    parser.add_argument("-t", "--threads", type=int, default=1, help="Number of threads for parallel processing")

    args = parser.parse_args()

    if not any([args.js, args.href, args.subdomains, args.forms, args.others, args.all]):
        print("Error: Select at least one URL type")
        parser.print_help()
        sys.exit(1)

    # Verifica se o caminho do diretório de saída é válido
    if not os.path.isabs(args.output_dir):
        print("Error: Please provide a full path for the output directory")
        sys.exit(1)

    lines = read_gospider_output(args.input_file)
    categories = categorize_urls(lines, args.exclude_400)
    save_categorized_urls(categories, args.output_dir, args)

if __name__ == "__main__":
    main()