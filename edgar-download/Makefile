codes := codes
years := 2021-2021
output := edgar_urls
download_destination := downloads
unzip_destination := nc_files
delay := 5


all: generate download unzip

.PHONY: clean
clean:
	rm -rf $(download_destination)
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
