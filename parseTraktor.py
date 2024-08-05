import xml.etree.ElementTree as ET
import re
import argparse


# Function to clean the title by removing the key and bpm information
def clean_title(title):
    return re.sub(r' - \d+[A-Z] - \d+', '', title)


def main():
    parser = argparse.ArgumentParser(description='Parse and format playlist from NML file.')
    parser.add_argument('filename', type=str, help='The NML file to parse')
    args = parser.parse_args()

    # Load and parse the XML file
    tree = ET.parse(args.filename)
    root = tree.getroot()

    # Extract relevant data: tracknumber, artist, title, and label from attributes
    tracks = []
    for i, entry in enumerate(root.findall('.//ENTRY'), start=1):
        artist = entry.attrib.get('ARTIST', 'Unknown Artist')
        title = clean_title(entry.attrib.get('TITLE', 'Unknown Title'))
        label = entry.find('.//INFO').attrib.get('LABEL', 'Unknown Label') if entry.find(
            './/INFO') is not None else 'Unknown Label'

        # Only add the track if it has meaningful data
        if artist != 'Unknown Artist' or title != 'Unknown Title':
            track_info = {
                'tracknumber': i,
                'artist': artist,
                'title': title,
                'label': label
            }
            tracks.append(track_info)

    # Format the output as requested: tracknumber, artist, title, and label in square brackets
    formatted_tracks = [
        f"{track['tracknumber']}. {track['artist']} - {track['title']} [{track['label']}]"
        for track in tracks
    ]

    # Display the formatted tracks
    for track in formatted_tracks:
        print(track)


if __name__ == '__main__':
    main()