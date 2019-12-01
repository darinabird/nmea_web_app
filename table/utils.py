import re

from .models import GPSData

nmea_regular = r'(?P<source>[!$A-Z]{6}),(?P<time>[0-9\.]{,10}),(?P<status>[AV]{0,1}),(?P<latitude>[0-9\.]{0,}),(?P<NS>[NS]{,1}),(?P<longitude>[0-9\.]{0,}),(?P<EW>[EW]{,1}),(?P<speed>[0-9\.]{0,}),(?P<path_angel>[0-9\.]{0,}),((?P<date>[0-9]{6})|),(?P<mdec>[0-9\.]{0,}),(?P<n>[EW]{,1}),(?P<m>[ADEN]{,1})\*(?P<hh>[0-9ABCDEF]+)'


def load_nmea():
    with open('tmp/gps_all', mode='rb') as f_obj:
        for line in f_obj:
            line = str(line)
            result = re.search(nmea_regular, line)

            if result is not None:
                # Проверяем контрольную сумму
                _end = line.find('*')
                l = len(line[1:_end])
                hh = hex(l)

                if hh[2:] != result.group('hh'):
                    continue

                data = {}

                data['source'] = result.group('source')
                data['time'] = result.group('time')
                data['status_valid'] = result.group('status')
                data['latitude'] = result.group('latitude')
                data['n_s'] = result.group('NS')
                data['longitude'] = result.group('longitude')
                data['e_w'] = result.group('EW')
                if result.group('speed') != '':
                    data['speed'] = result.group('speed')
                data['path_agele'] = result.group('path_angel')
                data['date'] = result.group('date')
                if result.group('mdec') != '':
                    data['height'] = result.group('mdec')
                data['direction_magnetic_declination'] = result.group('n')
                data['mode'] = result.group('m')
                data['checksum'] = result.group('hh')

                GPSData.objects.create(**data)
