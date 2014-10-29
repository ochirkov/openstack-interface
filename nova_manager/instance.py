from openstack_auth.auth import OpenstackAuth
from utils.config import DEFAULT
import json
import time


class Instance(OpenstackAuth):

    def __init__(self):
        super(Instance, self).__init__()
        self.conn = self.get_nova_conn()


    def instance_list(self):

        return self.conn.servers.list()


    def env_list(self, env=None):

        with open(DEFAULT['env_obj_storage_path']) as f:
            lines = f.readlines()
            output = json.loads(''.join(lines))

        if env is None:
            return output
        else:
            return output.get(env)


    def get_instance(self, id):

        server = self.conn.servers.get(id)
        return server.name


    def build_instance(self, name=None, flavor_name=None):

        name = name
        key = DEFAULT.get('ssh_key')

        image = self.conn.images.find(name=DEFAULT.get('image'))
        flavor = self.conn.flavors.find(name=flavor_name)

        server = self.conn.servers.create(name=name,
                                          image=image,
                                          flavor=flavor,
                                          key_name=key)

        status = server.status
        while status == 'BUILD':
            time.sleep(5)
            server = self.conn.servers.get(server.id)
            status = server.status

        return server


    def attach_ip(self, ip, instance):

        try:
            instance.add_floating_ip(ip)
            return True
        except Exception:
            return False


    def get_sec_group(self, id):

        sec_group = self.conn.security_groups.get(id)
        return sec_group.name


    def build_floating_ip(self):

        ip = self.conn.floating_ips.create()

        return ip