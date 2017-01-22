import argparse
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime as dt


def load_urls4check(path):
    with open(path, 'r') as f:
        return (f.readlines())


def get_server_respond_code(url):
    return requests.get(url).status_code


def paid_for_domain(domain_name):
    domain = whois.query(get_domain_name(domain_name))
    return domain and domain.expiration_date > dt.now()


def get_domain_name(url):
    domain_parts = urlparse(url).netloc.split('.')
    if len(domain_parts) > 2:
        return '.'.join(domain_parts[-1:-3])
    else:
        return urlparse(url).netloc


def print_status(server_response, domain_paid_response, url):
    if server_response == 200 and domain_paid_response:
        print('{} works and domain is paid!'.format(url))
    else:
        print(
            'Care! No information about {}'.format(url))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path', help="Path to file with urls", required=True)
    args = parser.parse_args()

    for url in load_urls4check(args.path):
        url = url.strip()
        print_status(get_server_respond_code(
            url), paid_for_domain(url), url)
