"""
Scrapes Manchester City Council
bin collection dates and returns
a JSON object.
"""
from flask import Flask, jsonify
from gazpacho import Soup
import requests
APP = Flask(__name__)

def get_bins(uprn):
    """
    Scrapes the endpoint for bin dates based on UPRNs.
    UPRNs available:
    https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information
    """
    base_url = 'https://www.manchester.gov.uk/bincollections'
    form_data = {'mcc_bin_dates_uprn': f'{uprn}',
                 'mcc_bin_dates_submit': 'Go'}
    res = requests.post(base_url, data=form_data)
    if res.status_code == 200:
        soup = Soup(res.text)
        collections = soup.find(
            'div', {'class': 'collection'}, mode='all', partial=False)
        bins = [col.find('h3').text for col in collections]
        dates = []
        for col in collections:
            date_strings = []
            row = col.find('li', mode='all')
            for date in row:
                date_strings.append(date.text)
            dates.append(date_strings)
        json_bins = {}
        for i, name in enumerate(bins):
            json_bins.update({name: dates[i]})
    else:
        json_bins = {}
    return jsonify(results=json_bins)


@APP.route('/id/<which>/<uprn>')
def return_by_id(uprn, which = None):
    """
    GET request returns most recent bin times
    based on an UPRN and which bins.
    e.g. /id/blue/000012345678
    """
    print(which)
    bins = get_bins(uprn)
    return bins


if __name__ == '__main__':
    APP.run(host="0.0.0.0", debug=True)
