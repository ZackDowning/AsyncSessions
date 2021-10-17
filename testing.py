# from net_async import AsyncSessions, ForceSessionRetry
# from pprint import pp
# from os import getenv
# from net_async import Connection, BugCheck
# from time import sleep
# from gui import ManagementFileBrowseWindow, ConfigFileBrowseWindow
# from getpass import getpass
from logging import basicConfig, exception


def main():
    basicConfig(filename='error_log.txt')
    try:
        raise Exception
    except Exception as e:
        exception(e)
    # # config_file = ConfigFileBrowseWindow().config_file
    #
    # def test_function(session):
    #     # Example command input options
    #     # cmd = session.send_config_file(config_file)
    #     # cmd = session.send_config_set(['interface vlan 1', 'no ip address', 'shutdown'])
    #     cmd = session.send_command('show ip int bri')
    #
    #     # This forces thread to retry session
    #     if cmd.__contains__('Authorization failed'):
    #         raise ForceSessionRetry
    #
    #     # Return whatever output of device that you'd like to use after all
    #     # asyncronous sessions are finished
    #     return cmd
    #
    # # username = getenv('USER')
    # # password = getenv('PASSWORD')
    # username, password = 'admin', 'admin'
    # # mgmt_ips = ManagementFileBrowseWindow().mgmt_ips
    # mgmt_ips = ['192.168.3.11']
    # sessions = AsyncSessions(username, password, mgmt_ips, test_function, verbose=True)
    # pp(sessions.outputs)
    # pp(sessions.failed_devices)


if __name__ == '__main__':
    main()
