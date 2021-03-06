import leancloud
import time

__author__ = 'Jayvee'

MapToolsVars = {'app_id': 'i13osrwxayxnaqsd3v0ikmqc0b1vndjnrgp6bp00p8iae6zc',
                'app_key': 'd9jubbw9fokmav8j0vqyxaccz8yokmyisk98orsnnu3o8kd4'}
ConfigVars = {'app_id': 'llir9y4gtqys053tivb4tildoan0hgj87kdd0j6ib5naye5e',
              'app_key': 'h5roibgrbtux2luasq1o9xwr218jebbsyuthv9ho4lced9rv'}


def get_context_menus():
    leancloud.init(app_id='llir9y4gtqys053tivb4tildoan0hgj87kdd0j6ib5naye5e',
                   app_key='h5roibgrbtux2luasq1o9xwr218jebbsyuthv9ho4lced9rv')
    Config = leancloud.Object.extend('Config')
    config_query = leancloud.Query(Config)
    config_query.equal_to('name', 'crf_event_prob_map')
    events_type = config_query.first()
    events = events_type.attributes
    menu = []
    for event in events['value'].keys():
        menu.append(event)
    return menu


def get_crf_newfeature():
    leancloud.init(app_id='llir9y4gtqys053tivb4tildoan0hgj87kdd0j6ib5naye5e',
                   app_key='h5roibgrbtux2luasq1o9xwr218jebbsyuthv9ho4lced9rv')
    Config = leancloud.Object.extend('Config')
    config_query = leancloud.Query(Config)
    config_query.equal_to('name', 'crf_new_features')
    new_feature = config_query.first().attributes
    return new_feature['value']


def get_crf_event_probmap():
    leancloud.init(app_id='llir9y4gtqys053tivb4tildoan0hgj87kdd0j6ib5naye5e',
                   app_key='h5roibgrbtux2luasq1o9xwr218jebbsyuthv9ho4lced9rv')
    Config = leancloud.Object.extend('Config')
    config_query = leancloud.Query(Config)
    config_query.equal_to('name', 'crf_event_prob_map')
    crf_event_probmap = config_query.first().attributes
    return crf_event_probmap


def save_to_leancloud(routeDatas):
    leancloud.init(app_id='i13osrwxayxnaqsd3v0ikmqc0b1vndjnrgp6bp00p8iae6zc',
                   app_key='d9jubbw9fokmav8j0vqyxaccz8yokmyisk98orsnnu3o8kd4')
    GeneratedData = leancloud.Object.extend('GeneratedData')
    gd = GeneratedData()
    try:
        gd.set('timestamp', int(time.time() * 1000))
        gd.set('senz_data', routeDatas)
        gd.save()
        return gd.id
    except leancloud.LeanCloudError, lce:
        # raise lce
        print 'save_to_leancloud error:' + lce
        return None


def get_recent_tracelist(limit=5):
    leancloud.init(MapToolsVars['app_id'], MapToolsVars['app_key'])
    GeneratedData = leancloud.Object.extend('GeneratedData')
    gd_query = leancloud.Query(GeneratedData)
    gd_query.limit(limit)
    gd_query.descending('createdAt')
    try:
        find_results = gd_query.find()
        return find_results
    except leancloud.LeanCloudError, lce:
        print 'get_recent_tracelist error:' + lce
        return None


def get_trace_by_id(trace_id):
    leancloud.init(MapToolsVars['app_id'], MapToolsVars['app_key'])
    GeneratedData = leancloud.Object.extend('GeneratedData')
    gd_query = leancloud.Query(GeneratedData)
    gd_query.equal_to('objectId', trace_id)
    try:
        find_results = gd_query.find()
        return find_results
    except leancloud.LeanCloudError, lce:
        print 'get_trace_by_id error:' + lce
        return None


if __name__ == '__main__':
    # pass

    print get_recent_tracelist()

    # print get_context_menus()

    # crf_prob = json.loads(
    #     open('D:\CS\Git\Jobs\senz.productivity.map.datagenerator\config\crf_prob_template.json', 'r').read())
    # leancloud.init(app_id='llir9y4gtqys053tivb4tildoan0hgj87kdd0j6ib5naye5e',
    #                app_key='h5roibgrbtux2luasq1o9xwr218jebbsyuthv9ho4lced9rv')
    # Config = leancloud.Object.extend('Config')
    # crf_event_prob_map = Config()
    # crf_event_prob_map.set('name', 'crf_new_features')
    # crf_event_prob_map.set('value',
    #                        {'time': ['early_morning', 'morning', 'noon', 'afternoon', 'evening', 'late_night'],
    #                         'day': ['weekday', 'weekend'],
    #                         'speed': ['still', 'low_speed', 'mid_speed', 'high_speed']})
    # crf_event_prob_map.save()
