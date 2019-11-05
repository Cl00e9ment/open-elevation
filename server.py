import json, logging
from bottle import route, run, request, response, hook
from gdal_interfaces import GDALTileInterface

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def load_json_from_file(filepath):
    with open(filepath) as file:
        return (json.load(file))

CONFIG = load_json_from_file('config.json')


def is_key_valid(key):
    with open('data/keys.txt', 'r') as keys_file:
        line = keys_file.readline()
        while line:
            line = line.strip()
            if len(line) == 0: continue
            if line == key: return True
            line = keys_file.readline()
    return False


class InternalException(ValueError):
    """
    Utility exception class to handle errors internally and return error codes to the client
    """
    pass


"""
Initialize a global interface. This can grow quite large, because it has a cache.
"""
interface = GDALTileInterface('data/', 'data/summary.json')
interface.create_summary_json()

def get_elevation(lat, lng):
    """
    Get the elevation at point (lat,lng) using the currently opened interface
    :param lat: 
    :param lng: 
    :return:
    """
    try:
        elevation = interface.lookup(lat, lng)
    except:
        return {
            'latitude': lat,
            'longitude': lng,
            'error': 'No such coordinate (%s, %s)' % (lat, lng)
        }

    return {
        'latitude': lat,
        'longitude': lng,
        'elevation': elevation
    }


@hook('after_request')
def enable_cors():
    """
    Enable CORS support.
    :return: 
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


def lat_lng_from_location(location_with_comma):
    """
    Parse the latitude and longitude of a location in the format "xx.xxx,yy.yyy" (which we accept as a query string)
    :param location_with_comma: 
    :return: 
    """
    try:
        lat, lng = [float(i) for i in location_with_comma.split(',')]
        return lat, lng
    except:
        raise InternalException(400, 'Bad parameter format "%s".' % location_with_comma)


def query_to_locations():
    """
    Grab a list of locations from the query and turn them into [(lat,lng),(lat,lng),...]
    :return: 
    """
    locations = request.query.locations
    if not locations:
        raise InternalException(400, '"locations" is required.')

    return [lat_lng_from_location(l) for l in locations.split('|')]


def body_to_locations():
    """
    Grab a list of locations from the body and turn them into [(lat,lng),(lat,lng),...]
    :return: 
    """
    try:
        locations = request.json.get('locations', None)
    except Exception:
        raise InternalException(400, 'Invalid JSON.')

    if not locations:
        raise InternalException(400, '"locations" is required in the body.')

    latlng = []
    for l in locations:
        try:
            latlng += [ (l['latitude'],l['longitude']) ]
        except KeyError:
            raise InternalException(400, '"%s" is not in a valid format.' % l)

    return latlng

def check_key():
    if CONFIG['key_required']:
        key = request.query.key
        if not key:
            raise InternalException(400, '"key" is required.')
        if not is_key_valid(key):
            raise InternalException(400, '"%s" is not a valid key.' % key)


def do_lookup(get_locations_func):
    """
    Generic method which gets the locations in [(lat,lng),(lat,lng),...] format by calling get_locations_func
    and returns an answer ready to go to the client.
    :return: 
    """
    try:
        check_key()
        locations = get_locations_func()
        return {'results': [get_elevation(lat, lng) for (lat, lng) in locations]}
    except InternalException as e:
        response.status = e.args[0]
        return {'error': e.args[1]}

# Base Endpoint
URL_ENDPOINT = '/api/v1/lookup'

# For CORS
@route(URL_ENDPOINT, method=['OPTIONS'])
def cors_handler():
    return {}

@route(URL_ENDPOINT, method=['GET'])
def get_lookup():
    """
    GET method. Uses query_to_locations.
    :return: 
    """
    return do_lookup(query_to_locations)


@route(URL_ENDPOINT, method=['POST'])
def post_lookup():
    """
    GET method. Uses body_to_locations.
    :return: 
    """
    return do_lookup(body_to_locations)

#run(host='0.0.0.0', port=8080)
run(host='0.0.0.0', port=8080, server='gunicorn', workers=4)
