# Author Nam Nguyen Hoai
import commands
from control_iptable import ControlIptable


class ControllerIptableUbuntu(ControlIptable):
    def __init__(self, system):
        super(ControllerIptableUbuntu, self).__init__(system=system)

    def show_iptable(self):
        return commands.getstatusoutput('sudo iptables -L')[1]

    def status_iptable(self):
        return commands.getstatusoutput('sudo service ufw status')[1]

    def start_iptable(self):
        return commands.getstatusoutput('sudo service ufw start')[1]

    def stop_iptable(self):
        return commands.getstatusoutput('sudo service ufw stop')[1]

if __name__ == '__main__':
    x = ControllerIptableUbuntu('ubuntu')
    x.action('status')
