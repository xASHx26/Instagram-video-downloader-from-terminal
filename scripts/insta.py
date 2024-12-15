import instaloader
import os


download_path = r"D:\Downlowd"


os.makedirs(download_path, exist_ok=True)


loader = instaloader.Instaloader(
    download_comments=False,
    download_geotags=False,
    download_video_thumbnails=False,
    download_pictures=True,  
    save_metadata=False,
    post_metadata_txt_pattern="",  
)

def download_instagram_post(url):
    try:
        
        shortcode = url.split('/')[-2]
        
        
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
        
        os.chdir(download_path)

        
        print(f"Downloading post to: {download_path}")
        loader.download_post(post, target="Instagram Video")

        print("Download completed successfully!")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    
    url = input("Enter the Instagram post URL: ").strip()
    download_instagram_post(url)
