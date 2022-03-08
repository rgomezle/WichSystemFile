#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess

# python3 WichWithFile.py Archivo_ip.txt 

if len(sys.argv) != 2:
    print("\n[!] Uso: python3 " + sys.argv[0] + "Archivo_ip.txt\n")
    sys.exit(1)

def get_ttl(line):

    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % line, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()

    out = out.split()
    out = out[12].decode('utf-8')

    ttl_value = re.findall(r"\d{1,3}", out)[0]

    return ttl_value

def get_os(ttl):

    ttl = int(ttl)

    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    else:
        return "Not Found"

if _name_ == '_main_':

    filename = sys.argv[1]

    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
      
     ttl = get_ttl(line)

     os_name = get_os(ttl)

     print("%s (ttl -> %s): %s" % (line, ttl, os_name))
