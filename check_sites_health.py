import argparse
import requests
import whois
from urllib.parse import urlparse


def load_urls4check(path):
    with open(path, 'r') as f:
        return (f.readlines())


def is_server_respond_with_200(url):
    r = requests.get(url)
    return r.status_code


def get_domain_expiration_date(domain_name):
    return (whois.query(get_domain_name(domain_name)).__dict__['expiration_date'])


def get_domain_name(domain_name):
    # выглядит так страшно из-за того что, whois не работает с много уровневыми доменами типа ru.wiki.org
    # приходится если таковой налицо, возвращать один уровень домена.
    domain_list = urlparse(domain_name).netloc.split('.')
    if len(domain_list) > 2:
        return (domain_list[-2] + '.' + domain_list[-1])
    else:
        return urlparse(domain_name).netloc


def print_status(server_response, whois_response, url):
    if server_response != 200:
        print('Url:"{}" out of service'.format(url))
    if not whois_response:
        print(
            'Url:"{}" works, but no information about payment for domain'.format(url))
    else:
        print(
            'Url:"{}" works and domain is paid for a long time!'.format(url))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path', help="Path to file with urls", required=True)
    args = parser.parse_args()

    for url in load_urls4check(args.path):
        print_status(is_server_respond_with_200(
            url.strip()), get_domain_expiration_date(url.strip()), url.strip())
