#!/bin/bash/python3
import time
import collections
import dns
import dns.resolver
import dns.zone
import socket


class DBCName(object):
    desflow_request = None
    comments = None

    def __init__(self, logger=None, log_message=None):
        self.logger = logger
        self.log_message = log_message

    def get_pointing_cnames(self, hostname):
        """
            Method to Get pointing cnames
            :parameter hostname
        """
        hostname = hostname.lower().replace('.win.ia55.net', '') + '.win.ia55.net'
        cnames_to_target, target_to_cnames = self.get_all_cnames_as_dict()
        return cnames_to_target.get(hostname.lower(), list())

    def get_all_cnames_as_dict(self):
        retry_count = 0
        retry_count_limit = 15
        while retry_count < retry_count_limit:
            try:
                IN = dns.rdataclass.from_text('IN')
                CNAME = dns.rdatatype.from_text('CNAME')
                core_elb_ip_addr = socket.gethostbyname('core.i.ia55.net')
                xfr = dns.query.xfr(core_elb_ip_addr, 'ia55.net', relativize=False)
                zone = dns.zone.from_xfr(xfr, relativize=False)
                names_to_cnames = collections.OrderedDict()
                cnames_to_names = collections.OrderedDict()

                for name in sorted(zone.nodes.keys(), key=lambda x: x.to_text().lower()):
                    try:
                        canon_name = name.to_text().lower()[0:-1]
                        for cname in zone[name].find_rdataset(IN, CNAME):
                            canon_cname = cname.to_text().lower()[0:-1]
                            cnames_to_names.setdefault(canon_cname, []).append(canon_name)
                            names_to_cnames.setdefault(canon_name, []).append(canon_cname)
                    except:
                        pass

                return cnames_to_names, names_to_cnames
            except Exception as ex:
                self.log_message(
                    "Error while fetching cname from core.i.ia55.net {}, trying again {}".format(str(ex), retry_count))
                time.sleep(5)
            retry_count += 1
        return {}, {}


dbc = DBCName()
print("Find the CName for: dbmonitor5b.win.ia55.net" )
cname = dbc.get_pointing_cnames('dbmonitor5b.win.ia55.net')
print("CName is", cname)
