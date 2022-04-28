# Overview

Manchester City Coucil don't currnetly offer an API for querying bin collection dates. They *do* have a timetable querying service, for which I've made use of @maxhumber's [gazpacho](https://github.com/maxhumber/gazpacho) to scrape data from MCC.

## Usage

For development and testing, clone this repo, install dependencies using `python3 -m pip install -r requirements.txt`, and start the dev server using `python3 web_app.py`. One the server is running, get [your UPRN number](https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information) and you can request the next bin collections using http://localhost:5000/id/all/[UPRN]