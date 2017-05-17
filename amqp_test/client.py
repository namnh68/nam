# Author Nam Nguyen Hoai
import config
import time
import oslo_messaging as om


CONF = config.CONF
transport = om.get_transport(CONF)
target = om.Target(topic='test-amqp')


def get_client():
    return om.RPCClient(transport, target)


class TargetClient(object):
    def __init__(self):
        self.client = get_client()

    def call_func1(self):
        cctx = self.client
        return cctx.call({}, 'test1')

    def call_func2(self):
        cctx = self.client
        return cctx.call({}, 'test2')


def main():
    test_rpc = TargetClient()
    for i in range(100):
        time.sleep(1)
        test_rpc.call_func1()
        test_rpc.call_func2()

if __name__ == '__main__':
    main()
