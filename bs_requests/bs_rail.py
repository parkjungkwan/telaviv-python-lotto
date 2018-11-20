#!/usr/bin/env python

# from mechanize import Browser # 파이썬 3.4 지원
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class NationalRailBrowser(Browser):
    BASE = 'http://www.nationalrail.co.uk/'

    def search(self, _from, _to, via=None, outwardTime=datetime.now(), returnTime=datetime.now(), directTrainsOnly=False, includeOvertakenTrains=False):
        self.open(self.BASE)
        self.select_form('homepageQjp')
        self['from.searchTerm'] = _from
        self['to.searchTerm'] = _to
        if via: self['via.searchTerm'] = via

        outwardTime += timedelta(minutes = self._minute(outwardTime.minute)-outwardTime.minute)
        self['timeOfOutwardJourney.day'] = [outwardTime.strftime('%d')]
        self['timeOfOutwardJourney.month'] = [outwardTime.strftime('%B')]
        self['timeOfOutwardJourney.hour'] = [outwardTime.strftime('%H')]
        self['timeOfOutwardJourney.minute'] = [outwardTime.strftime('%M')]

        returnTime += timedelta(hours = 2)
        returnTime += timedelta(minutes = self._minute(returnTime.minute)-returnTime.minute)
        self['timeOfReturnJourney.day'] = [returnTime.strftime('%d')]
        self['timeOfReturnJourney.month'] = [returnTime.strftime('%B')]
        self['timeOfReturnJourney.hour'] = [returnTime.strftime('%H')]
        self['timeOfReturnJourney.minute'] = [returnTime.strftime('%M')]

        if directTrainsOnly: self['maxChanges'] = ['true']
        if includeOvertakenTrains: self['includeOvertakenTrains'] = ['true']
        r = self.submit()

        b = BeautifulSoup(r)
        table = b.find(attrs={'id':'ResultsTable'})
        tbody = table.find('tbody') # the first of many
        tr = tbody.findAll('tr')

        departure = [td.contents[0] for td in tr[3].findAll('td')]
        arrival = [td.contents[0] for td in tr[4].findAll('td')]
        duration = [td.contents[0] for td in tr[6].findAll('td')]
        changes = [td.contents[0] for td in tr[7].findAll('td')]
        return zip(departure, arrival, duration, changes)

    def _minute(self, m):
        res,rem = divmod(m,15)
        if rem == 0:
            return m
        else:
            return (res+1)*15

if __name__=='__main__':
    import sys
    if len(sys.argv) < 3:
        print( 'Usage: python nationalrail.py from to\nExample: python nationalrail.py SHF "Birmingham"')
        exit(1)
    _from, _to = sys.argv[1:3]
    b = NationalRailBrowser()
    for journey in b.search(_from, _to):
        print( 'departure: %s\narrival: %s\nduration: %s\nchanges: %s\n' % journey)
