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

### All Trackers
1. Copy the contents of `trackers-all.txt`
2. In qBittorrent, go to Tools > Options > BitTorrent
3. Paste the trackers into the "Trackers" field (one per line)

### Best Trackers Only
1. Copy the contents of `trackers-best.txt`
2. In qBittorrent, go to Tools > Options > BitTorrent
3. Paste the trackers into the "Trackers" field (one per line)

## Adding Sources

To add more tracker sources:
- Edit `sources-all.txt` for comprehensive list
- Edit `sources-best.txt` for curated best list

## Contributing

Pull requests are welcome. Please add new tracker sources to the `sources.txt` file. Generally, quality sources are preferred over quantity. If you find a source that is no longer valid, please remove it from the list.

## License

This project is open source and available under the MIT License.