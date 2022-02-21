from urllib.error import HTTPError
from urllib.request import urlopen, Request


def call_proxy(name):
    url = "http://localhost:8012/proxy/{0}/".format(name)
    httprequest = Request(url, headers={"Accept": "application/json"})
    try:
        with urlopen(httprequest) as response:
            print('{0} - {1}'.format(response.status, response.read().decode()))
    except HTTPError as e:
        print(e)


def main():
    errors = ['key_error',
              'exception',
              'cancelled',
              'unknown',
              'invalid_argument',
              'deadline_exceeded',
              'not_found',
              'already_exists',
              'permission_denied',
              'resource_exhausted',
              'failed_precondition',
              'aborted',
              'out_of_range',
              'unimplemented',
              'internal',
              'unavailable',
              'data_loss',
              'unauthenticated']
    names = ['Rodrigo',
             'Pamela',
             'Davi',
             'Daniela',
             'Camila',
             'Leandro',
             'Nicolas',
             'Joao',
             'Paulo',
             'Fabio',
             ]
    for error in errors:
        call_proxy(error)
        for name in names:
            call_proxy(name)


if __name__ == '__main__':
    main()
