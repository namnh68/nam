from oslo_config import cfg

CONF = cfg.CONF
CONF(['--config-file', 'amqp.conf'])
