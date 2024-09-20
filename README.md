# Gospider Output Processor

This is an output processor for Gospider, a web crawling tool. It categorizes and filters URLs according to different criteria, supporting multi-threaded processing for better performance.

## Features

- Categorization of URLs into subdomains, href, javascript, forms, and others
- Filtering of URLs with 400 response codes
- Support for multi-threaded processing
- Flexible selection of URL types for output
- Output in separate text files by category

## Requirements

- Python 3.6+

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/gospider-output-processor.git
   ```

2. Navigate to the project directory:
   ```
   cd gospider-output-processor
   ```

## Usage

Run the main script with the necessary arguments:

```
python main.py -I <input_file> -O <output_directory> [options]
```

### Required arguments:

- `-I` or `--input-file`: Path to the Gospider output file
- `-O` or `--output-dir`: Full path to the directory where categorized files will be saved

### Options:

- `--exclude-400`: Excludes URLs with 400 response codes
- `-J` or `--js`: Selects only JavaScript URLs
- `-H` or `--href`: Selects only href URLs
- `-S` or `--subdomains`: Selects only subdomains
- `-F` or `--forms`: Selects only form URLs
- `-L` or `--linkfinder`: Selects only linkfinder URLs
- `-R` or `--robots`: Selects only robots.txt URLs
- `-U` or `--others`: Selects other uncategorized URLs
- `-A` or `--all`: Selects all URL types
- `-t` or `--threads`: Number of threads for parallel processing (default: 10)

## Usage Examples

1. Process all URLs using 4 threads:
   ```
   python main.py -I input.txt -O /full/path/output -A -t 4
   ```

2. Process only subdomains and JavaScript URLs, excluding 400 codes:
   ```
   python main.py -I input.txt -O /full/path/output -S -J --exclude-400
   ```

3. Process href and form URLs:
   ```
   python main.py -I input.txt -O /full/path/output -H -F
   ```

## Output Structure

The program will create a text file for each selected category in the specified output directory. The file names will be:

- `subdomains.txt`
- `href.txt`
- `javascript.txt`
- `form.txt`
- `linkfinder.txt`
- `robots.txt`
- `url.txt` (for uncategorized URLs)
- `others.txt`

Each file will contain one URL per line.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
.
