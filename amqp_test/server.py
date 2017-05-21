#!/usr/bin/python
# Author: Nam Nguyen Hoai
import oslo_messaging as om
import config

CONF = config.CONF
transport = om.get_transport(CONF)
target = om.Target(topic='test-amqp', server='test_amqp')


class ServerListen(object):
    """
    Sever side
    """
    def test1(self, cctx):
        print "The test1 function was called"
        return "Here is function 1"

    def test2(self, cctx):
        print "The test2 function was called"
        return "Here is function 2"


def main():
    endpoints = [ServerListen()]
    server_rpc = om.get_rpc_server(transport, target,
                                   endpoints, executor='blocking')
    server_rpc.start()
    server_rpc.wait()


if __name__ == '__main__':
    main()

