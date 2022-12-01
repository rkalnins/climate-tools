from argparse import ArgumentTypeError, ArgumentParser
import re

def parseNumList(string):
    m = re.match(r'(\d+)(?:-(\d+))?$', string)
    if not m:
        raise ArgumentTypeError("'" + string + "' is not a range of number. Expected forms like '0-5' or '2'.")
    start = m.group(1)
    end = m.group(2) or start
    return list(range(int(start, 10), int(end, 10) + 1))

def edgar_generate_urls(years, sector_codes):

    for year in years:
        for sector in sector_codes:

            sector = sector.strip()

            url = f"https://cidportal.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v70_FT2021_GHG/CH4/{sector}/v7.0_FT2021_CH4_{year}_{sector}.0.1x0.1.zip"
    
            print(url)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--codes", required=True, type=str, help="path of file containing list of sector codes")
    parser.add_argument("-y", "--years", default="2021-2021", type=parseNumList, metavar="start-end", help="range of years to download in the format xxxx-yyyy")
    
    args = parser.parse_args()

    sector_codes = list()

    with open(args.codes, "r") as f:
        sector_codes = f.readlines()

    edgar_generate_urls(args.years, sector_codes)
