# Programming Assignment 1: All about DNS
# CSE 310, Spring 2023
# Instructor: Aruna Balasubramanian
# Due date: 02/21/2023, 9.00pm

import dns
import datetime
import time
from datetime import date
from dns import query

rootIPv4 = ["198.41.0.4", "199.9.14.201", "192.33.4.12", "199.7.91.13", "192.203.230.10", "192.5.5.241", "192.112.36.4",
            "198.97.190.53", "192.36.148.17", "192.58.128.30", "193.0.14.129", "199.7.83.42", "202.12.27.33"]

n = input()


def myDig(name, ip):
    # print("start")
    # print(ip)

    # Query DNS and Return UDP Object
    domain = dns.name.from_text(name)
    req = dns.message.make_query(domain, dns.rdatatype.A)
    udpData = dns.query.udp(req, ip, timeout=20)

    # print(udpData)

    # Handle DNS Error
    if dns.rcode.from_flags(udpData.flags, udpData.ednsflags) != dns.rcode.NOERROR:
        if rootIPv4.count(ip) > 0:
            if rootIPv4.index(ip) == 12:
                raise Exception("DNS ERROR")
            else:
                print("Switching Root")
                return myDig(name, rootIPv4[rootIPv4.index(ip) + 1])

    # Handle CNAME Not Found
    if udpData.answer != [] and "CNAME" not in udpData.answer[0].to_text():
        return udpData.answer[0].to_text()

    # Handle CNAME Found
    if udpData.answer != [] and "CNAME" in udpData.answer[0].to_text():
        if len(udpData.answer) > 0:
            for i in udpData.answer:
                # print(udpData.answer[i].to_text())
                edit_cname = (myDig(udpData.answer[i].to_text().split()[-1], rootIPv4[0]).split())
                edit_cname[0] = name + "."
                return " ".join(edit_cname)
        else:
            edit_cname = (myDig(udpData.answer[0].to_text().split()[-1], rootIPv4[0]).split())
            edit_cname[0] = name + "."
            return " ".join(edit_cname)

    # Handle Additional Information
    elif udpData.additional:
        for i in range(len(udpData.additional)):
            if ":" not in udpData.additional[i].to_text().split()[-1]:
                newIp = udpData.additional[i].to_text().split()[-1]
                return myDig(name, newIp)

    # Handle Authority Information
    elif udpData.authority:
        newDomain = udpData.authority[0].to_text().split()[-1]
        newIp = myDig(newDomain, rootIPv4[0]).split()[-1]
        return myDig(name, newIp)
    else:
        raise Exception("Shovel Broken")


# Start Dig
start = time.time()
dug = myDig(n, rootIPv4[0]).split('\n')[0]
end = time.time()
query_time = int(round((end - start) * 1000))

# Print Information
print('QUESTION SECTION: \n' + n + '.   IN A\n\nANSWER SECTION: \n' + dug + "\n\nQuery time: " + str(
    query_time) + " msec" + "\nWHEN: " + datetime.datetime.now().strftime(
    '%A') + " " + datetime.datetime.now().strftime("%B") + " " + datetime.datetime.now().strftime(
    "%d") + " " + datetime.datetime.now().strftime("%H:%M:%S") + " 2023")
