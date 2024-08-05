# Playlist Parser

## Overview

This project contains scripts to parse and format playlists from HTML and NML files. The scripts extract relevant track information and display it in a formatted manner.

## Files

- `parsePlaylist.py`: Parses and formats playlists from HTML files.
- `parseTraktor.py`: Parses and formats playlists from NML files.

## Requirements

- Python 3.x
- `argparse` module
- `re` module
- `BeautifulSoup` module (for `parsePlaylist.py`)
- `xml.etree.ElementTree` module (for `parseTraktor.py`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nilicule/traktor.git
    cd traktor
    ```

2. Install the required Python packages:
    ```sh
    pip install beautifulsoup4
    ```

## Usage

### Parsing HTML Playlists

To parse and format a playlist from an HTML file, use the `parsePlaylist.py` script:

```sh
python parsePlaylist.py <filename>
```

Replace <filename> with the path to your HTML file.

### Parsing NML Playlists

To parse and format a playlist from an NML file, use the `parseTraktor.py` script:

```sh
python parseTraktor.py <filename>
```

Replace <filename> with the path to your NML file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```
