import novaclient.v1_1.client as nvclient
from openstack_auth import CREDS


class OpenstackAuth(object):

    def __init__(self):
        self.creds = CREDS

    def get_nova_conn(self):
        """
        Returns nova client object.
        """

        nova = nvclient.Client(**self.creds)

        return nova