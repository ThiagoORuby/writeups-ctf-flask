
URL = https://drive.google.com/drive/u/1/folders/1lkparSRMIx2Jrs458plSY655iZvP_j5P
OUTPUT = ./writeups/static/markdown

update:
	gdown $(URL) -O $(OUTPUT) --folder

server:
	flask run --debug