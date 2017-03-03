# coding: utf-8

import urllib

import requests

from config import *
from errcode import RETCODES

class Dnspod(object):

    def __init__(self, **kw):
        
        self.base_url = DNSPOD_BASE_URL
        self.params = dict(
            login_token=DNSPOD_API_TOKEN,
            format='json'
            
        )
        self.params.update(kw)
        self.path = None


    def _request(self, **kw):
        ret_doc = {}
        self.params.update(kw)
        self.path = '{0}/{1}'.format(self.base_url, kw['path'])
        self.params.pop('path')
        

        ret_doc = requests.post(
            url=self.path,
            data=self.params,
            headers=DNSPOD_HEADERS
        ).json()
        if 'code' in ret_doc['status']:
            ret_doc['status']['msg'] = RETCODES[ret_doc['status']['code']]


        return ret_doc

    def get_domain_list(self, **kw):
        return self._request(
            path='Domain.List'
        )

    def get_line_list(self, **kw):
        return self._request(
            path='Domain.Info',
            domain_id='233553491'
        )


if __name__ == '__main__':

    api = Dnspod()
    ret1 = api.get_domain_list()
    ret2 = api.get_line_list()
    print ret1

    print ret2
    # a = {u'status': {u'message': u'Action completed successful', u'code': u'1', u'created_at': u'2017-02-23 17:40:38'}, u'info': {u'mine_total': 5, u'share_total': 0, u'error_total': 0, u'vip_expire': 0, u'share_out_total': 0, u'vip_total': 0, u'lock_total': 0, u'pause_total': 0, u'domain_total': 5, u'spam_total': 0, u'ismark_total': 0, u'all_total': 5}, u'domains': [{u'status': u'enable', u'ext_status': u'', u'remark': u'', u'searchengine_push': u'yes', u'name': u'dipstar.net', u'grade_title': u'\u65b0\u514d\u8d39\u5957\u9910', u'grade': u'DP_Free', u'ttl': u'600', u'src_flag': u'DNSPOD', u'cname_speedup': u'disable', u'created_on': u'2015-08-08 21:10:40', u'punycode': u'dipstar.net', u'records': u'5', u'is_vip': u'no', u'is_mark': u'no', u'owner': u'tidewind@gmail.com', u'updated_on': u'2015-08-08 21:10:40', u'group_id': u'1', u'id': 24733733}, {u'status': u'enable', u'ext_status': u'', u'remark': u'', u'searchengine_push': u'yes', u'name': u'ipast.me', u'grade_title': u'\u65b0\u514d\u8d39\u5957\u9910', u'grade': u'DP_Free', u'ttl': u'600', u'src_flag': u'DNSPOD', u'cname_speedup': u'disable', u'created_on': u'2015-06-08 01:21:56', u'punycode': u'ipast.me', u'records': u'4', u'is_vip': u'no', u'is_mark': u'no', u'owner': u'tidewind@gmail.com', u'updated_on': u'2015-06-08 01:21:56', u'group_id': u'1', u'id': 23355349}, {u'status': u'enable', u'ext_status': u'', u'remark': u'', u'searchengine_push': u'yes', u'name': u'ipast.org', u'grade_title': u'\u514d\u8d39\u5957\u9910', u'grade': u'D_Free', u'ttl': u'600', u'src_flag': u'DNSPOD', u'cname_speedup': u'disable', u'created_on': u'2012-03-05 20:49:00', u'punycode': u'ipast.org', u'records': u'10', u'is_vip': u'no', u'is_mark': u'no', u'owner': u'tidewind@gmail.com', u'updated_on': u'2015-02-18 20:17:17', u'group_id': u'1', u'id': 1321392}, {u'status': u'enable', u'ext_status': u'', u'remark': u'', u'searchengine_push': u'yes', u'name': u'iaxi.net', u'grade_title': u'\u514d\u8d39\u5957\u9910', u'grade': u'D_Free', u'ttl': u'600', u'src_flag': u'DNSPOD', u'cname_speedup': u'disable', u'created_on': u'2011-09-06 10:18:28', u'punycode': u'iaxi.net', u'records': u'6', u'is_vip': u'no', u'is_mark': u'no', u'owner': u'tidewind@gmail.com', u'updated_on': u'2016-02-25 09:57:13', u'group_id': u'1', u'id': 902476}, {u'status': u'enable', u'ext_status': u'', u'remark': u'', u'searchengine_push': u'yes', u'name': u'icokou.com', u'grade_title': u'\u514d\u8d39\u5957\u9910', u'grade': u'D_Free', u'ttl': u'600', u'src_flag': u'DNSPOD', u'cname_speedup': u'disable', u'created_on': u'2011-09-06 01:17:49', u'punycode': u'icokou.com', u'records': u'4', u'is_vip': u'no', u'is_mark': u'no', u'owner': u'tidewind@gmail.com', u'updated_on': u'2014-11-20 00:02:21', u'group_id': u'1', u'id': 902139}]}
    # print a['status']['code']
    # print a['info']['domain_total']
    # domains =  a['domains']


    #print requests.get('http://ops.jumeird.com/api/squirrel/res/').json()