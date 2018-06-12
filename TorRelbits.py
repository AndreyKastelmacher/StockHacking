__author__ = 'AKonline13'
#104.245.233.41:70 A8FCF1642AC074BB085596BF71FCD98C4CE0D1C3
#5.155.149.76:443 36CDEEFA645D131EF617029E10A6CB5E08881ACF
#192.36.27.82:30485 25F6A8E2A74CEDAAF21136A55F012505D522458E
#https://stem.torproject.org/tutorials/to_russia_with_love.html

import pycurl
import StringIO
import stem.process
from stem.util import term


from stem.control import Controller

with Controller.from_port(port = 9151) as controller:
  controller.authenticate()  # provide the password here if you set one

  bytes_read = controller.get_info("traffic/read")
  bytes_written = controller.get_info("traffic/written")

  print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))

import pycurl
import StringIO

import stem.process

from stem.util import term

SOCKS_PORT = 9150


def query(url):
  """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """

  output = StringIO.StringIO()

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
    return output.getvalue()
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)


# Start an instance of Tor configured to only exit through Russia. This prints
# Tor's bootstrap information as it starts. Note that this likely will not
# work if you have another Tor instance running.

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


print(term.format("Starting Tor:\n", term.Attr.BOLD))

tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{ru}',
  },
  init_msg_handler = print_bootstrap_lines,
)

print(term.format("\nChecking our endpoint:\n", term.Attr.BOLD))
print(term.format(query("https://www.atagar.com/echo.php"), term.Color.BLUE))

tor_process.kill()  # stops tor