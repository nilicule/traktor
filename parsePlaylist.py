import re
import argparse
from bs4 import BeautifulSoup


def parse_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip the header row

    tracks = []
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 7:  # Ensure we have enough columns
            artist = columns[2].text.strip()
            title = columns[3].text.strip()
            label = columns[8].text.strip()

            # Remove the key and BPM information from the title
            title = re.sub(r' - \d+[A-Za-z]* - \d+(\.\d+)?$', '', title)

            tracks.append((artist, title, label))

    return tracks


def format_tracks(tracks):
    formatted_tracks = []
    for i, (artist, title, label) in enumerate(tracks, 1):
        formatted_track = f"{i}. {artist} - {title} [{label or 'N/A'}]"
        formatted_tracks.append(formatted_track)
    return formatted_tracks


def main():
    parser = argparse.ArgumentParser(description='Parse and format playlist from HTML file.')
    parser.add_argument('filename', type=str, help='The HTML file to parse')
    args = parser.parse_args()

    with open(args.filename, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    parsed_tracks = parse_html_content(html_content)

    # Format the tracks
    formatted_tracks = format_tracks(parsed_tracks)

    # Print the formatted tracks
    for track in formatted_tracks:
        print(track)


if __name__ == '__main__':
    main()