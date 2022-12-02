# Climate Tools

Roberts Kalnins

## Edgar downloader

There 3 stages to the downloader:
1. URL generation
2. Downloading
3. Unzipping

Run `make` to generate URLs, download, and unzip using all default options.

Default settings are found at the top of `Makefile`:

- `codes`: path containing list of sector codes (leave default)
- `years`: range of years
- `output`: url output file name (leave default)
- `download_destination`: zip file download path (leave default)
- `unzip_destination`: destination of unzipped `.nc` files
- `delay`: delay between consecutive `wget` downloads to prevent server bans

```bash
codes := codes
years := 2021-2021
output := edgar_urls
download_destination := downloads
unzip_destination := nc_files
delay := 5
```

Specifying custom paths:
```bash
# use defaults when generating urls and downloading
make generate download

# unzip downloaded files to custom directory
make unzip unzip_destination=</path/to/put/nc/files>
```
