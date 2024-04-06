import requests
import shutil
import tempfile
import os
import subprocess


import subprocess


def download_m3u8(url):
    output_file = "video.mp4"
    """
    Download an m3u8 file using ffmpeg.

    Parameters:
    - url (str): The URL of the m3u8 file.

    Returns:
    - str: The path to the downloaded video file if successful, None otherwise.
    """
    try:
        # Run ffmpeg command to download the m3u8 file
        subprocess.run(["ffmpeg", "-i", url, "-c",
                        "copy", output_file], check=True)
        return output_file
    except subprocess.CalledProcessError:
        print("Error: Failed to download m3u8 file.")
        return None


def upload_to_gofile(file_path):
    url = 'https://api.gofile.io/servers'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        first_server_name = data['data']['servers'][0]['name']
        url = f'https://{first_server_name}.gofile.io/contents/uploadfile'
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        data = response.json()
        return data['data']['downloadPage']
    else:
        raise Exception(f"Error: {response.status_code}")


def handle_download_upload(video_url):
    downloaded_video_path = download_m3u8(video_url)
    if downloaded_video_path:
        print("Video downloaded successfully!")
        upload_link = upload_to_gofile(downloaded_video_path)
        print("Direct download link:", upload_link)
    else:
        print("Failed to download the video.")
