""" Funtion to download the Google Docs, Sheets with its shared link/url. """

import os

from requests import get


def download_project_doc(url: str, filename: str) -> None:
    """Download the files saved in Google Drive by their shared link/url.
    Prefer file type : `[sheets, docs, pdf, image]`

    Args:
        url (str): Shared url of the file.
        filename (str): Filename to save with. Provide `extension` of the file as well.

    Returns:
        None: Saves the file at `./projects_docs/<filename_with_ext>`
    """

    FOLDER_PATH = './docs'
    FILE_PATH = f'./docs/' + filename.replace('/', ' ')

    # Check if document already downloaded
    if os.path.exists(FILE_PATH):
        return None

    # Get the ID of the file
    url = url.split('/')[-2]

    # Prefix for download url
    dl_prefix = 'https://docs.google.com/uc?export=download&id='

    # Make a directory to save the file
    if not os.path.exists(FOLDER_PATH):
        os.mkdir(FOLDER_PATH)

    # Request the file with its download url
    r = get(dl_prefix + url)

    # Write the file with chunks
    with open(FILE_PATH, 'wb') as doc:
        for chunk in r.iter_content(2560):
            doc.write(chunk)


def main():
    # This file works with '.pdf' extension
    url = 'https://drive.google.com/file/d/1vnq-YmAsd5vMFqOMe4Ytz0TRpBOZJD9Q/view?usp=share_link'

    # This file works with '.docx' extension
    url = 'https://docs.google.com/document/d/1U6CUuWGVJKaxWeYV5JPzJsJuWDdH3j30/edit?usp=share_link&ouid=110827767954182979203&rtpof=true&sd=true'

    # Decide the file extension
    file_ext = '.docx' if 'docs.google.com' in url else '.pdf'

    filename = 'Project 3' + file_ext

    download_project_doc(url, filename)


if __name__ == '__main__':
    main()
