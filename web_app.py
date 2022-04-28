"""
Calls Manchester City Council
bin collection dates API and returns
a JSON object.
"""
from flask import Flask, jsonify
import requests
APP = Flask(__name__)

def get_bins(uprn):
    """
    Scrapes the endpoint for bin dates based on UPRNs.
    UPRNs available:
    https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information
    """
    base_url = 'https://www.manchester.gov.uk/site/custom_scripts/bin_dates_gazops/'
    res = requests.get(f'{base_url}?uprn={uprn}')
    if res.status_code == 200:
        bins = res.json()
    else:
        bins = {}
    return jsonify(results = bins)

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
