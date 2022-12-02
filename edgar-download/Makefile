# path containing list of sector codes
codes := codes

# range of years
years := 2021-2021

# url output file
output := edgar_urls

# path to zip downloads
download_destination := downloads

# path to final unzipped files
unzip_destination := nc_files

# delay consecutive wget downloads to prevent bans from servers
delay := 5


all: generate download unzip

.PHONY: clean
clean:
	rm -rf $(unzip_destination) $(download_destination)
	rm edgar_urls

.PHONY: generate
generate:
	python edgar_downloader.py -c $(codes) -y $(years) > $(output)

.PHONY: download
download:
	mkdir -p $(download_destination)
	wget --input-file $(output) --directory-prefix $(download_destination) --wait=$(delay)

.PHONY: unzip
unzip:
	mkdir -p $(unzip_destination)
	unzip $(download_destination)/\*.zip -d $(unzip_destination)
