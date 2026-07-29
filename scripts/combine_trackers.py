import requests
from urllib.parse import urlparse

# Configuration
SOURCES_ALL_FILE = "sources-all.txt"
SOURCES_BEST_FILE = "sources-best.txt"
OUTPUT_ALL_FILE = "trackers-all.txt"
OUTPUT_BEST_FILE = "trackers-best.txt"


def extract_protocol(url):
    """Extract protocol from URL for sorting purposes."""
    try:
        parsed = urlparse(url.strip())
        return parsed.scheme
    except:
        return ""


def process_urls(urls):
    """Process list of URLs: remove duplicates, sort by protocol then alphabetically."""
    # Remove empty lines and whitespace
    urls = [url.strip() for url in urls if url.strip()]

    # Remove duplicates while preserving order for now
    seen = set()
    unique_urls = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)

    # Sort by protocol first, then by full URL
    unique_urls.sort(key=lambda x: (extract_protocol(x), x.lower()))

    return unique_urls


def fetch_remote_file(url):
    """Fetch content from a remote URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""


def read_sources_file(filename):
    """Read source URLs from a file."""
    try:
        with open(filename, "r") as f:
            sources = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
        return sources
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it with one URL per line.")
        return []


def process_trackers_from_sources(sources_file, output_file):
    """Process trackers from a sources file and write to output file."""
    source_urls = read_sources_file(sources_file)
    
    if not source_urls:
        print(f"No source URLs found in {sources_file}. Skipping.")
        return 0

    all_trackers = []

    # Fetch trackers from all sources
    for source_url in source_urls:
        print(f"Fetching trackers from: {source_url}")
        content = fetch_remote_file(source_url)
        if content:
            trackers = content.splitlines()
            all_trackers.extend(trackers)

    # Process all trackers
    processed_trackers = process_urls(all_trackers)

    # Write to output file
    with open(output_file, "w") as f:
        for tracker in processed_trackers:
            f.write(tracker + "\n")

    print(f"Successfully updated {output_file} with {len(processed_trackers)} unique trackers")
    return len(processed_trackers)


def main():
    # Process all trackers
    all_count = process_trackers_from_sources(SOURCES_ALL_FILE, OUTPUT_ALL_FILE)
    
    # Process best trackers
    best_count = process_trackers_from_sources(SOURCES_BEST_FILE, OUTPUT_BEST_FILE)
    
    print(f"\nSummary:")
    print(f"  All trackers: {all_count}")
    print(f"  Best trackers: {best_count}")


if __name__ == "__main__":
    main()