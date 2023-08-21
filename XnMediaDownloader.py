import streamlit as st
from pytube import YouTube
import instaloader
import os

def youtube_video_download(url, r, path):
    yt = YouTube(url)
    with st.spinner("Downloading.....") :
        filter_streams = yt.streams.filter(res=r, file_extension='mp4')
        if filter_streams:
            video = filter_streams.first()
            video.download(path)
            st.success(f"Youtube video is successfully downloaded and stored in {path}")
        else:
            st.error(f"Youtube video of {r} resolution is not available")

def instagram_video_download(url, path):
    insta_loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(insta_loader.context, url.split("/")[-2])
    with st.spinner("Downloading......") :
        insta_loader.download_post(post, target=path)
        st.success("Instagram video downloaded successfully!")

def main():
    st.title("XnMedia Downloader")
    media_choice = st.radio("Choose Media", ["YouTube", "Instagram"])

    if media_choice == "YouTube":
        url = st.text_input("Enter the video url")
        resolution = st.selectbox("Choose Resolution", ["144p", "240p", "360p", "480p", "720p", "1080p"])
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        if st.button("Download YouTube Video"):
            youtube_video_download(url, resolution, downloads_path)

    elif media_choice == "Instagram":
        url = st.text_input("Enter the Instagram reel's URL")
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        if st.button("Download Instagram Video"):
            instagram_video_download(url, downloads_path)

if __name__ == "__main__":
    main()
