# coding: utf8
db.define_table(
                'point',
                Field('latitude', 'double'),
                Field('longitude', 'double'),
                Field('stationName'),
                Field('stationlocation'),
                Field('availableDocks','integer'),
                Field('totalDocks','integer'),
                Field('availableBikes','integer'),
                Field('statusValue'),
                Field('statusKey','integer')
                )

def insertData():
    #grid = SQLFORM.smartgrid(db.point)
    #or we can write a SQL procedure to insert data once
    #if db.point.empty()...db.insert...
    #pointList = ddata.get('stationBeanList')

    #db.point.insert(latitude=[], longitude=[], stationName=[])
    #db.commit()
    import urllib

    url = 'http://divvybikes.com/stations/json'
    page = urllib.urlopen(url)
    data = page.read()
    import gluon.contrib.simplejson
    ddata = gluon.contrib.simplejson.loads(data)

    station_list = ddata.get('stationBeanList')
    station_list_size = len (station_list)

    for x in range(0, station_list_size):
        db.point.insert(latitude = ddata.get('stationBeanList')[x].get('latitude'),
                        longitude = ddata.get('stationBeanList')[x].get('longitude'),
                        stationName = ddata.get('stationBeanList')[x].get('stationName'),
                        stationlocation = ddata.get('stationBeanList')[x].get('location'),
                        availableDocks = ddata.get('stationBeanList')[x].get('availableDocks'),
                        totalDocks = ddata.get('stationBeanList')[x].get('totalDocks'),
                        availableBikes = ddata.get('stationBeanList')[x].get('availableBikes'),
                        statusValue = ddata.get('stationBeanList')[x].get('statusValue'),
                        statusKey = ddata.get('stationBeanList')[x].get('statusKey'))
    pass
    #update all the data (inlcude the static and dynamic--whole table)


def initialData():
    #update the dynamic value from divvy api to model
    #availableDocks, availableBikes, statusValue, statusKey
    import urllib

    url = 'http://divvybikes.com/stations/json'
    page = urllib.urlopen(url)
    data = page.read()
    import gluon.contrib.simplejson
    ddata = gluon.contrib.simplejson.loads(data)

    station_list = ddata.get('stationBeanList')
    station_list_size = len (station_list)

    for x in range(0, station_list_size):
        station_name = ddata.get('stationBeanList')[x].get('stationName')
        db(db.point.stationName == station_name).update(availableDocks=ddata.get('stationBeanList')[x].get('availableDocks'),
                                                        availableBikes=ddata.get('stationBeanList')[x].get('availableBikes'),
                                                        statusValue = ddata.get('stationBeanList')[x].get('statusValue'),
                                                        statusKey = ddata.get('stationBeanList')[x].get('statusKey'))
    pass
