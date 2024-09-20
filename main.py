import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Gospider output processor")
    parser.add_argument("input_file", help="Path to the gospider output file")
    parser.add_argument("output_directory", help="Directory to save categorized URL lists")
    parser.add_argument("--exclude-400", action="store_true", help="Exclude URLs with 400-class codes")
    parser.add_argument("-J", "--js", action="store_true", help="Select only JavaScript URLs")
    parser.add_argument("-H", "--href", action="store_true", help="Select only href URLs")
    parser.add_argument("-S", "--subdomains", action="store_true", help="Select only subdomains")
    parser.add_argument("-F", "--forms", action="store_true", help="Select only form URLs")
    parser.add_argument("-O", "--others", action="store_true", help="Select other uncategorized URLs")
    parser.add_argument("-A", "--all", action="store_true", help="Select all types of URLs")
    parser.add_argument("-t", "--threads", type=int, default=1, help="Number of threads for parallel processing")

    args = parser.parse_args()

    #verify args

    if not any ([args.js, args.herf, args.subdomain, args.forms, args.others, args.all]):
        print("Erro: insert at less one arg")
        parser.print_help()
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Gospider output processor")
    parser.add_argument("input_file", help="Path to the gospider output file")
    parser.add_argument("output_directory", help="Directory to save categorized URL lists")
    parser.add_argument("--exclude-400", action="store_true", help="Exclude URLs with 400-class codes")
    parser.add_argument("-J", "--js", action="store_true", help="Select only JavaScript URLs")
    parser.add_argument("-H", "--href", action="store_true", help="Select only href URLs")
    parser.add_argument("-S", "--subdomains", action="store_true", help="Select only subdomains")
    parser.add_argument("-F", "--forms", action="store_true", help="Select only form URLs")
    parser.add_argument("-O", "--others", action="store_true", help="Select other uncategorized URLs")
    parser.add_argument("-A", "--all", action="store_true", help="Select all types of URLs")
    parser.add_argument("-t", "--threads", type=int, default=1, help="Number of threads for parallel processing")

    if __name__ == "_main_":
        main()