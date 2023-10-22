import gdown


url = "https://drive.google.com/drive/u/1/folders/1lkparSRMIx2Jrs458plSY655iZvP_j5P"
output = "./static/markdown"

gdown.download_folder(url=url, output=output, use_cookies=True)
