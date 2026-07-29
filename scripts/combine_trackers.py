import requests
import os
from urllib.parse import urlparse

# File containing source URLs, one per line
SOURCES_FILE = "sources.txt"
OUTPUT_FILE = "trackers.txt"


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


def read_sources_file():
    """Read source URLs from the sources.txt file."""
    try:
        with open(SOURCES_FILE, "r") as f:
            sources = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
        return sources
    except FileNotFoundError:
        print(f"Error: {SOURCES_FILE} not found. Please create it with one URL per line.")
        return []


def main():
    # Read source URLs from file
    source_urls = read_sources_file()
    
    if not source_urls:
        print("No source URLs found. Exiting.")
        return

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
    with open(OUTPUT_FILE, "w") as f:
        for tracker in processed_trackers:
            f.write(tracker + "\n")

    print(f"Successfully updated {OUTPUT_FILE} with {len(processed_trackers)} unique trackers")


if __name__ == "__main__":
    main()