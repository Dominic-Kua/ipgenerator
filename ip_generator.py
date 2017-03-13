# requires Python 3.6 or higher
import random

def generate_random_ip(one=(0,255), two=(0,255), three=(0,255), four=(0,255), string=True):
    """
    one,two,three,four are all tuples which define the range of an IPv4 octet
    The returned object can either be a string or list of IP octects as determined by 
    the string argument.
    """
    for octet in [one,two,three,four]:
        if True in [octet[0]>octet[1], octet[0] < 0, octet[1] < 0, octet[0] > 255, octet[1] > 255] :
            return "0.0.0.0"
    ip_address = [random.randint(ip[0], ip[1]) for ip in [one, two, three, four]]
    if string:
        return  f"{ip_address[0]}.{ip_address[1]}.{ip_address[2]}.{ip_address[3]}"
    else:
        return ip_address

if __name__ == "__main_":
    print(generate_random_ip())
