# Author Nguyen Hoai Nam
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class ControlIptable(object):
    def __init__(self, system):
        self.system = system

    def your_system(self):
        print 'Your system is: %s', self.system

    def action(self, name_action):
        foo = getattr(self, name_action + '_iptable')
        print foo()

    @abc.abstractmethod
    def show_iptable(self):
        """
        :return:
        """

    @abc.abstractmethod
    def stop_iptable(self):
        """

        :return:
        """

    @abc.abstractmethod
    def start_iptable(self):
        """

        :return:
        """

    @abc.abstractmethod
    def status_iptable(self):
        """

        :return:
        """

if __name__ == '__main__':
    x = ControlIptable('ubuntu')
    x.action('show')