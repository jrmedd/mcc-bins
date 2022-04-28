# Overview

Manchester City Council don't currently offer an publicly available API for querying bin collection dates. They *do* have an undocumented API, which I've made use wrapped around here so I can add functionality to filter by bin type, next date etc.

## History

I previously committed (about 15 minutes before this one) a script that would scrape the HTML of the public facing page, before I realised that the API itself was hidden away in the PDF generator for a full time table.

## Usage

For development and testing, clone this repo, install dependencies using `python3 -m pip install -r requirements.txt`, and start the dev server using `python3 web_app.py`. One the server is running, get [your UPRN number](https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information) and you can request the next bin collections using http://localhost:5000/id/all/[UPRN]