# Programming Assignment 1: All about DNS
# CSE 310, Spring 2023
# Instructor: Aruna Balasubramanian
# Due date: 02/21/2023, 9.00pm

import dns
import datetime
import time
from datetime import date
import calendar
from dns import query
input = input()

rootIPv4 = ["198.41.0.4", "199.9.14.201", "192.33.4.12", "199.7.91.13", "192.203.230.10", "192.5.5.241", "192.112.36.4", "198.97.190.53", "192.36.148.17", "192.58.128.30", "193.0.14.129", "199.7.83.42", "202.12.27.33"]

rootIPv6 = ["2001:503:ba3e::2:30", "2001:500:200::b", "2001:500:2::c", "2001:500:2d::d", "2001:500:a8::e", "2001:500:2f::f", "2001:500:12::d0d", "2001:500:1::53", "2001:7fe::53", "2001:503:c27::2:30", "2001:7fd::1", "2001:500:9f::42", "2001:dc3::35"]