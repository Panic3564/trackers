# qBittorrent Trackers List

This repository automatically aggregates tracker lists from multiple trusted sources, removes duplicates, and sorts them for optimal use with qBittorrent.

## Features

- Automatically updated every 24 hours
- Combines trackers from multiple reputable sources
- Removes duplicate entries
- Sorts by protocol (udp, http, https, ws, wss) then alphabetically
- Ready to use with qBittorrent

## Usage

1. Copy the contents of `trackers.txt`
2. In qBittorrent, go to Tools > Options > BitTorrent
3. Paste the trackers into the "Trackers" field (one per line)

## Adding Sources

To add more tracker sources, edit the `sources.txt` file and add one URL per line.

## Contributing

Pull requests are welcome. Please add new tracker sources to the `sources.txt` file.

## License

This project is open source and available under the MIT License.