from appannie.util import format_request_data, to_day


class App(object):
    DOWNLOADS_ENDPOINT = '/dashboard/{market}/item/{product_id}/downloads'

    def __init__(self, http_client, paginator, market, product_id):
        self.http_client = http_client
        self.paginator = paginator
        if(market == 'ios'):
            self.market = 35509
        elif(market == 'google-play'):
            self.market = 8215
        self.product_id = product_id

    def _format_uri(self, uri):
        return uri.format(market=self.market,
                          product_id=self.product_id)

    def _format_data(self, start_date, end_date, **kwargs):
        data = format_request_data(**kwargs)
        data['start_date'] = to_day(start_date)
        data['end_date'] = to_day(end_date)
        return data

    def downloads(self, start_date, end_date, **kwargs):
        data = self._format_data(start_date, end_date, **kwargs)
        uri = self._format_uri(self.DOWNLOADS_ENDPOINT)
        return self.paginator.make(uri, data=data, union_key='downloads')
