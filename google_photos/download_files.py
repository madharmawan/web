import os
import flask
import requests
import io
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

def download_file(service, media_item, download_directory):
    request = service.mediaItems().get(mediaItemId=media_item['id'])
    response = request.execute()

    filename = response['filename']
    media_url = response['baseUrl']
    download_url = media_url + "=d"

    # Specify the file path where the file will be saved
    file_path = os.path.join(download_directory, filename)

    # Make a GET request to download the file content
    response = requests.get(download_url)
    if response.status_code == 200:
        # Save the file to the specified file path
        with io.open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {file_path}")
    else:
        print(f"Failed to download: {filename}")