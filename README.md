# qBittorrent Trackers List

This repository automatically aggregates tracker lists from multiple  sources, removes duplicates, and sorts them for optimal use with qBittorrent.

## Disclaimer
This project is not affiliated with or endorsed by qBittorrent. Use at your own risk. The maintainers of this repository are not responsible for any issues that may arise from using the provided tracker lists, including but not limited to, potential bans, blocks, or other restrictions imposed by torrent sites or ISPs. Always ensure that you are complying with local laws and regulations when using torrent trackers. Malware or malicious trackers may be present in the lists, so use caution and verify the sources before adding them to your torrent client.

## Features

- Automatically updated every 24 hours
- Generates two separate files:
  - `trackers-all.txt`: Comprehensive list from all sources
  - `trackers-best.txt`: Curated list from best sources only
- Combines trackers from multiple reputable sources
- Removes duplicate entries
- Sorts by protocol (udp, http, https, ws, wss) then alphabetically
- Ready to use with qBittorrent
## Usage

### Method 1: Automatically Append Trackers from URL (Recommended)

This method automatically adds trackers to all new downloads:

1. Get the raw URL of the tracker file you want to use:
   - For all trackers: `https://raw.githubusercontent.com/Panic3564/trackers/refs/heads/main/trackers-all.txt`
   - For best trackers: `https://raw.githubusercontent.com/Panic3564/trackers/refs/heads/main/trackers-best.txt`

2. In qBittorrent, go to **Tools > Options > BitTorrent**

3. In the "Automatically append trackers from URL to new downloads" field, paste the raw URL

4. Click **Apply** and **OK**

Now all new downloads will automatically have these trackers appended.

### Method 2: Manual Trackers List

If you prefer to manually add trackers to the global list:

1. Copy the contents of `trackers-all.txt` or `trackers-best.txt`
2. In qBittorrent, go to **Tools > Options > BitTorrent**
3. Paste the trackers into the "Trackers" field (one per line)
4. Click **Apply** and **OK**

## Adding Sources

To add more tracker sources:
- Edit `sources-all.txt` for comprehensive list
- Edit `sources-best.txt` for curated best list

## Contributing

Pull requests are welcome. Please add new tracker sources to the `sources.txt` file. Generally, quality sources are preferred over quantity. If you find a source that is no longer valid, please remove it from the list.
