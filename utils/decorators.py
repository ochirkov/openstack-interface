import os
import sys
from openstack_auth.auth import OpenstackAuth
from utils.config import DEFAULT


def check_ips(func):

    def wrapper():

        conn = OpenstackAuth().get_nova_conn()
        if len(conn.floating_ips.findall()) >= int(DEFAULT.get('allowed_ips_number')):
            print "ip addresses are limited."
            sys.exit(1)
        else:
            func()

    return wrapper


def check_lock(func):

    def wrapper():

        lock_file = '/tmp/openstack.lock'

        if os.path.exists(lock_file):
            print "Process is locked. Try later."
            sys.exit(1)
        else:
            f = open(lock_file, 'w+')
            f.write('#')
            f.close

            func()

            os.remove(lock_file)

    return wrapper
