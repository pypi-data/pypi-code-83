#!/bin/env python3

import socket
import os
from pathlib import Path  # requires python 3.5
import sys
import yaml
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
import unicodedata


def setup_parser():

    parser = argparse.ArgumentParser(
        prog="Epgnotify",
        description="Parses EPG data from VDR, checks against search config and sends mail. Already sent programs are stored in a cache to avoid multiple notifications on same program.",
    )

    parser.add_argument(
        "--config",
        type=str,
        metavar="file",
        help="Config file. If not given ~/epgnotify.yml is used.",
    )

    parser.add_argument(
        "--stdout",
        action="store_true",
        default=False,
        help="Additionally print result to stdout",
    )

    parser.add_argument(
        "--cache-file",
        type=str,
        metavar="file",
        help="Optionally, cache file location, default epgnotfiy.cache.yaml in home directory is used. Use /dev/null to disable caching.",
    )

    parser.add_argument(
        "--epg-dst-file",
        type=str,
        default=None,
        metavar="file",
        help="Store received EPG data to a file",
    )

    parser.add_argument(
        "--no-cache-write",
        action="store_true",
        default=False,
        help="If given, cache is not written, which is usefull for reproducible test-cases.",
    )

    return parser


def norm_str(s):
    """
    Normalizes UTF-8 string for case-insensitive string comparison.
    See: https://docs.python.org/3/howto/unicode.html
    """

    def NFD(s):
        return unicodedata.normalize("NFD", s)

    try:
        return NFD(NFD(s).casefold())
    except TypeError as ex:
        # unparseable data is often caused by errors in config file
        # print unparseable data so users can see where the error is
        print('Cannot normalize %s' % str(s), file=sys.stderr)
        raise ex


def str_in(s1, s2):
    """
    Checks if string s1 is in s2. Check is done after normalization and casefolding.

    Returns
    -------
    bool:
        True if string s1 can be found in s2
    """

    return norm_str(s1) in norm_str(s2)


def str_eq(s1, s2):
    """
    Checks if string s1 and s2 are equal. Check is done after normalization and casefolding.

    Returns
    ------
    bool:
        True if strings are equal after normalization and casefolding.
    """

    return norm_str(s1) == norm_str(s2)


def read_till_msg(sock, msg):
    """
    Reads from socket until stream ends in msg.

    Parameter
    ---------
    sock : socket
        Socket to read from

    msg : bytearray
        bytearray

    Returns
    ------
    str

    """
    d = b""
    while True:
        data = sock.recv(4096)
        d += data
        if d.endswith(msg):
            break

    return d.decode("utf-8", "backslashreplace")


def get_epg_data(config):
    """
    Reads EPG data via SVDRP from VDR using the command 'LSTE'.

    Returns
    -------
    str:
        VDR's output to the'LSTE' command as string.

    """
    # make socket connection to VDR
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = config["vdrhost"]
    port = config["vdrport"]
    sock.connect((host, port))
    sock.settimeout(10)

    # get and check VDR's greeting message
    data = read_till_msg(sock, "\n".encode())
    if not data.startswith("220 "):
        raise Exception("Got unexpected greeting message: " + data)
    if not data.endswith("UTF-8\r\n"):
        raise Exception("Encoding does not seem to be UTF-8")

    # request EPG data
    sock.send("LSTE\n".encode("utf-8"))
    data = read_till_msg(sock, b"215 End of EPG data\r\n")

    # close connection
    sock.send("QUIT\n".encode("utf-8"))

    return data


def parse_epg_data(data):
    """
    Parses EPG data and store interesting programs in a list.
    Each program will become a dictionary containg the keys from VDR's epg.data
    file definition http://www.vdr-wiki.de/wiki/index.php/Epg.data
    'TableID' and 'Version' from key 'E' are left out since their rapid changes
    for no apparent reason will cause unintended cache misses.
    """
    all_programs = []
    for line in data.split("\n"):
        if len(line) < 5:
            continue
        # print(len(line), line[4:])
        hdr = line[4]
        if hdr == "C":  # start of a new channel section
            channel = line[6:]
        elif hdr == "c":  # end of a channel secion
            pass
        elif hdr == "E":  # start of a new program
            # last two values are database IDs which might change without an
            # actual change of the program. Thus strip the last two values.
            program = {"E": line[6:].rsplit(" ", 2)[0]}
        elif hdr in "TSDGRV":  # program description
            program[hdr] = line[6:]
        elif hdr == "X":  # streams (can occur many times)
            if "X" not in program:
                program["X"] = []
            program["X"].append(line[6:])
        elif hdr == "e":  # end of a program description
            program["C"] = channel
            all_programs.append(program)
        else:
            raise Exception("Got unexpected line: " + line)
    return all_programs


def programlist_to_html(program_list, link_base=None):
    """
    Generates nicely formatted HTML file from list of programs.
    """

    HTML_hdr = """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style>
ul {padding-left:2em;}
table {width: 100%}
td {text-align: center;}
td.lft {text-align: left;}
table, th, td { border: 1px solid black; }
</style>
<title>epgnotify list</title>
</head>
<body>
<table>
<tr>
<th><b>Channel</b></th>
<th><b>Program</b></th>
<th><b>Description</b></th>
<th><b>Match</b></th>
<th><b>Streams</b></th>
</tr>
"""

    HTML_ftr = """</table>
</body>
</html>
"""

    lst = []
    for p in program_list:
        lst.append("<tr>")

        eid, starttime, duration = p["E"].split(" ")

        duration = float(duration)
        starttime = int(starttime)
        # starttime=time.strftime('%Y-%m-%d %H:%M:%S',  time.gmtime(starttime))
        # starttime=time.strftime('%a %b %d %H:%M:%S %Z %Y',
        #                        time.localtime(starttime))

        starttime = time.asctime(time.localtime(starttime))
        # add channel info
        cid, cname = p["C"].split(" ", 1)
        s = "<td>{}<br><b>{}</b><br>{}</td>".format(cid, cname, eid)
        lst.append(s)

        # add program info
        s = "<td>{}<br><b>{}</b><br>".format(starttime, p["T"])
        if "G" in p:
            s += "Genre: {}<br>".format(p["G"])
        s += "Duration (min): {}".format(int(duration // 60))

        s += '<br><a href="{}/vdradmin.pl?aktion=timer_new_form&epg_id={}&channel_id={}&referer={}">Link to vdradmin-am</a>'.format(
            link_base, int(eid), cid, "Li92ZHJhZG1pbi5wbD9ha3Rpb249dGltZXJfbGlzdA=="
        )
        # Li92ZHJhZG1pbi5wbD9ha3Rpb249dGltZXJfbGlzdA== is base64 encoded
        # for "./vdradmin.pl?aktion=timer_list"

        s += "</td>"
        lst.append(s)

        # add description
        s = "<td>"
        if "S" in p:
            s += "<b>S: </b>" + p["S"]
        if "D" in p:
            if "S" in p:
                s += "<br>"
            s += "<b>D: </b>" + p["D"]
        s += "</td>"
        lst.append(s)

        # add matches
        s = '<td class="lft"><ul><li>{}</li></ul></td>'.format(p["hit"])
        lst.append(s)

        # add streams
        s = "<td><ul>"
        if "X" in p:
            for x in p["X"]:
                s += "<li>{}</li>".format(x)
        s += "</ul></td>"
        lst.append(s)

        lst.append("</tr>")

    return HTML_hdr + "\n".join(lst) + HTML_ftr


# search_config={
#    'title': [ {'title': 'Moderne Wunder',
#                'nosubtitle': ['Episode 24',
#                         'Hubschrauber',
#                         'Retrotechnik',
#                         'Groß & Klein',
#                         'Handwerk']
#                },
#                'Abenteuer Erde',
#                'Avengers',
#               'Auf Enteckungsreise',
#               ],
#    'notitle': ['Ö3',],
#    'nochannel': ['Sky Cinema', 'SYFY HD', 'Discovery HD'],
#    }


def _check_blacklist(program, t, T):
    """
    Helper function to check_program()
    """
    # if search has subtitle blacklist and program has subtitle
    if "notintitle" in t:
        for notintitle in t["notintitle"]:
            if str_in(notintitle, T):
                return False
    if "notinsubtitle" in t and "S" in program:
        for nosub in t["notinsubtitle"]:
            if str_in(nosub, program["S"]):
                return False
    if "nosubtitle" in t and "S" in program:
        for nosub in t["nosubtitle"]:
            if str_eq(nosub, program["S"]):
                return False
    if "notitle" in t:
        for notitle in t["notitle"]:
            if str_eq(notitle, T):
                return False
    if "notinchannel" in t:
        for nochannel in t["notinchannel"]:
            if str_in(nochannel, program["C"]):
                return False
    return True


def check_program(program, search_config):

    # TODO: keys in program and search config are normalized every time a str_*
    # function is called. Maybe caching the normalized strings will enhance
    # execution speed.

    try:
        T = program["T"]
    except KeyError as e:
        # print('Program has no "T":', program)
        # channel with no title is valid EPG but has no futher usage
        return False

    # title blacklist
    if "notitle" in search_config:
        for t in search_config["notitle"]:
            if str_eq(t, T):
                return False

    # channel blacklist
    if "nochannel" in search_config:
        for noC in search_config["nochannel"]:
            if str_eq(noC, program["C"]):
                return False

    # inchannel blacklist
    if "notinchannel" in search_config:
        for noC in search_config["notinchannel"]:
            if str_in(noC, program["C"]):
                return False

    # title match
    for t in search_config["title"]:
        # just detect title
        if type(t) == str and str_eq(t, T):
            program["hit"] = "title " + t
            return True

        # title detection with blacklist
        if type(t) == dict and str_eq(t['title'], T):
            if _check_blacklist(program, t, T):
                program["hit"] = "title " + t["intitle"]
                return True

    # in title
    for t in search_config["intitle"]:
        # just detect title
        if type(t) == str and str_in(t, T):
            program["hit"] = "intitle " + t
            return True

        # title detection with blacklist
        if type(t) == dict and str_in(t["intitle"], T):
            # if search has subtitle blacklist and program has subtitle
            if _check_blacklist(program, t, T):
                program["hit"] = "title " + t["intitle"]
                return True

    # in subtitle
    if "insubtitle" in search_config and "S" in program:
        for t in search_config["insubtitle"]:
            if str_in(t, program["S"]):
                program["hit"] = "insubtitle"
                return True

    # in description
    if "indescription" in search_config and "D" in program:
        for t in search_config["indescription"]:
            # detect string in description
            if str_in(t, program["D"]):
                program["hit"] = "indescription " + t
                return True

    return False


def send_email(HTML_string, subject_string, config):
    # send email

    if "from_email" in config:
        sender = config["from_email"]
    else:
        sender = config["email"]

    receiver = config["email"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject_string
    msg["From"] = sender
    msg["To"] = receiver

    # text='See HTML'
    # part1=MIMEText(text,'plain')
    # msg.attach(part1)

    # html mail
    part2 = MIMEText(HTML_string, "html")
    msg.attach(part2)

    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.close()


def in_ignore_hit(c, all_programs):
    """
    Checks a cache item c if it is present in list of all programs.
    Cache item will have key 'hit' that might not be present in a program.
    Thus, `c['hit']` is ignored in check.

    Parameters
    ----------
    c : dict
        Program from cache (including a key 'hit')

    all_programs : list
        List of programs from EPG data. Must not include a key 'hit'.

    Returns
    -------
    bool :
        True if cache item 'c' is in EPG data 'all_programs'.
    """

    # exclude 'hit' from comparison as it is in cache but not in list
    # of programs
    c_no_hit = {}
    for key in c.keys():
        if key != 'hit':
            c_no_hit[key] = c[key]

    return c in all_programs


def purge_cache(cache, all_programs):
    """
    Checks cache against list of programs and removes entries from cache that
    are not in list of programs any more.

    Parameters
    ----------
    cache : list
        List of programs from cache

    all_programs : list
        List of all programs from epg data.

    Returns
    -------
    cache_new : list
        New cache, bar old programs that have already been aired.
    """

    # TODO: some TV stations send epg-data erratically, i.e. in consecutive
    # EPG scans a program might be missing at one point and delete from cache.
    # Once the program reapperas it will look as new since it was purged from
    # the cache in the previous run and the user will be notified multiple
    # times. Thus, a cache retention of a few days might be required.

    cache_new = []
    for c in cache:
        if in_ignore_hit(c, all_programs):
            cache_new.append(c)

    return cache_new


def main():
    parser = setup_parser()
    args = parser.parse_args()

    # with open('search_config.yml', 'w') as outfile:
    #    yaml.dump(search_config, outfile, default_flow_style=False, allow_unicode=True)

    # load config
    if not args.config:
        filename = os.path.join(str(Path.home()), "epgnotify.yml")
    else:
        filename = args.config
    with open(filename, "r") as f:
        config = yaml.safe_load(f)

    # load cache (already sent notifications)
    if not args.cache_file:
        cache_file = os.path.join(str(Path.home()), "epgnotify.cache.yml")
    else:
        cache_file = args.cache_file
    if os.path.isfile(cache_file):
        with open(cache_file, "r") as f:
            cache = yaml.safe_load(f)
    else:
        cache = []

    # get EPG data
    data = get_epg_data(config)

    # write EPG data to file if requested
    if args.epg_dst_file:
        with open(args.epg_dst_file, "w") as f:
            f.write(data)

    # parse EPG data to list of programms
    all_programs = parse_epg_data(data)

    # check for interesting programs
    program_list = []
    for program in all_programs:
        # Hint: check_programm adds new key 'hit' to relevant programs, which
        # is also in cache.
        if check_program(program, config) and program not in cache:
            # print(program)
            program_list.append(program)

    # convert to nice HTML table
    if "vdradmin_link" in config:
        link_base = config["vdradmin_link"]
    else:
        link_base = None
    HTML_string = programlist_to_html(program_list, link_base)

    # print to stdout
    if args.stdout:
        print(HTML_string)

    # send via mail
    if "email" in config:
        subject_string = "epgnotify found {} new programs for you".format(
            len(program_list)
        )

        send_email(HTML_string, subject_string, config)

    # prevent infinitely growing cache by purging
    # programs from cache that are not in EPG data any more
    cache = purge_cache(cache, all_programs)

    # add currently found programs to cache
    cache.extend(program_list)

    # sort cache (makes it much easier to debug)
    cache = sorted(cache, key=lambda k: k["E"])

    if not args.no_cache_write:
        # write cache
        with open(cache_file, "w") as f:
            yaml.dump(cache, f, allow_unicode=True)


if __name__ == "__main__":
    main()
