from ConfigParser import SafeConfigParser as SCP


def get_conf_args(arg):

    config_parser = SCP()
    config_path = '/opt/openstack_env/etc/openstack_cloud.ini'
    config_parser.read(config_path)

    return dict(config_parser.items(arg))


DEFAULT = get_conf_args('default')
TEAMS = get_conf_args('teams')