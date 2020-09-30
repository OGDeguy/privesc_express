def print_banner():
    """
    Prints the privesc express banner
    :return: None
    """
    banner = '''
   ___      _      ____          _____  _____  ___  ____________
  / _ \____(_)  __/ __/__ ____  / __/ |/_/ _ \/ _ \/ __/ __/ __/
 / ___/ __/ / |/ / _/(_-</ __/ / _/_>  </ ___/ , _/ _/_\ \_\ \  
/_/  /_/ /_/|___/___/___/\__/ /___/_/|_/_/  /_/|_/___/___/___/  


    '''
    print(banner)


class Plugin:
    """
    The base plugin class to be inherited by all plugins. Gives us a standard interface for working with plugins.
    """

    author = ''  # Name of author of the plugin
    contributors = []  # List of folks that contributed to the plugin
    version = '0.0.0'  # The semantic version of the plugin
    # A brief description of the plugin to display to the user
    short_description = 'A brief description of what the plugin does'
    # We set this to true if we find that the host is vulnerable to this plugin
    vulnerable = False

    capabilities = {
        'check': False,
        'exploit': False,
        'explain': False
    }
    options = None
    def __init__(self):
        pass

    def check(self):
        """
        Checks if the target is vulnerable to this plugin
        :return: Boolean() - True if we believe this privesc should work
        """
        pass

    def exploit(self, args=[]):
        """
        Exploit the vulnerability. Optional. If added set capabilities['exploit'] = True
        :param args: list() - List of arguments for the exploit function (optional)
        :return: None
        """
        pass

    def results(self):
        """
        Print / describe the result of the check to the user.
        :return:
        """
        pass

    def explain(self):
        """
        Print the README.md in the plugin dir.
        :return: None
        """
        pass