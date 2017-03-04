from __future__ import print_function
from oslo_config import cfg


opt_group = cfg.OptGroup(name='simple',
                         title='A Simple Example')

simple_opts = [
    cfg.BoolOpt('enable', default=False,
                help=('True enables, False disables'))
]

nam_group = cfg.OptGroup(name='nam', title='A title for Nam')

nam_opts = [
    cfg.StrOpt('name', default='Hoai Nam')
]


CONF = cfg.CONF
CONF.register_group(opt_group)
CONF.register_group(nam_group)
CONF.register_opts(simple_opts, opt_group)
CONF.register_opts(nam_opts, nam_group)


if __name__ == "__main__":
    CONF(default_config_files=['app.conf'])
    print(CONF.simple.enable)
    print("=======")
    print(CONF.nam.name)
    print("====")
    print(dir(CONF.nam))
