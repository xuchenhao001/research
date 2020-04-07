# -*- coding:utf-8 -*-
# !/usr/bin/python

import os
import time

LD_LIBRARY = "LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib"


def exec_cmd(cmd):
    os.system(cmd)


def encryption_aes(keep_output):
    if keep_output:
        cmd_str = LD_LIBRARY + \
                  " openssl aes-256-cbc -a -salt -in transaction_tau.txt -k secret_password -out encrypted.txt"
    else:
        cmd_str = LD_LIBRARY + " openssl aes-256-cbc -a -salt -in transaction_tau.txt -k secret_password"
    exec_cmd(cmd_str)


def decryption_aes(keep_output):
    if keep_output:
        cmd_str = LD_LIBRARY + " openssl aes-256-cbc -d -a -in encrypted.txt -k secret_password -out decrypted.txt"
    else:
        cmd_str = LD_LIBRARY + " openssl aes-256-cbc -d -a -in encrypted.txt -k secret_password"
    exec_cmd(cmd_str)


def encryption_rsa():
    cmd_str = LD_LIBRARY + " openssl rsautl -encrypt -pubin -inkey public.key -in input.txt -out encrypted-rsa.txt"
    exec_cmd(cmd_str)


def decryption_rsa():
    cmd_str = LD_LIBRARY + " openssl rsautl -decrypt -inkey private.key -in encrypted-rsa.txt -out decrypted-rsa.txt"
    exec_cmd(cmd_str)


def encryption_abe(attribute_number, keep_output):
    attribute_list = ""
    for attribute in range(attribute_number):
        if attribute == 0:
            attribute_list += "Attribute:0000"
        else:
            attribute_list += "|Attribute:{0:05d}".format(attribute)
    if keep_output:
        cmd_str = LD_LIBRARY + " oabe_enc -s KP -e \"{0}\" " \
                           "-i input.txt " \
                           "-o encrypted.kpabe".format(attribute_list)
    else:
        cmd_str = LD_LIBRARY + " oabe_enc -s KP -e \"{0}\" " \
                               "-i input.txt " \
                               "-o /dev/null".format(attribute_list)
    # print(cmd_str)
    exec_cmd(cmd_str)


def generate_key_slice(attribute_number, keep_output):
    attribute_policy = "("
    for attribute in range(attribute_number):
        if attribute == 0:
            attribute_policy += "Attribute:0000"
        else:
            attribute_policy += " and Attribute:{0:05d}".format(attribute)
    attribute_policy += ")"
    if keep_output:
        cmd_str = LD_LIBRARY + " oabe_keygen -s KP " \
                               "-i \"{0}\" " \
                               "-o analystKP".format(attribute_policy)
    else:
        cmd_str = LD_LIBRARY + " oabe_keygen -s KP " \
                               "-i \"{0}\" " \
                               "-o /dev/null".format(attribute_policy)
    # print(cmd_str)
    exec_cmd(cmd_str)


def decryption_abe(keep_output):
    if keep_output:
        cmd_str = LD_LIBRARY + " oabe_dec -s KP -k analystKP.key -i encrypted.kpabe -o decrypted.txt"
    else:
        cmd_str = LD_LIBRARY + " oabe_dec -s KP -k analystKP.key -i encrypted.kpabe -o /dev/null"
    exec_cmd(cmd_str)


# do simulation here
def simulation(attribute_number, loop_number):
    generate_key_slice(attribute_number, True)
    encryption_abe(attribute_number, True)
    # test encryption
    start = time.time()
    for i in range(loop_number):
        encryption_abe(attribute_number, False)
        encryption_aes(True)
    end = time.time()
    encryption_time = end - start

    # test decryption
    start = time.time()
    for i in range(loop_number):
        decryption_abe(False)
        decryption_aes(True)
    end = time.time()
    decryption_time = end - start
    return encryption_time, decryption_time


def ps_simulation():
    simulation_results = []
    loop_number = 100
    for attribute_number in range(6, 21):
        encryption_time, decryption_time = simulation(attribute_number, loop_number)
        simulation_results.append(
            "Simulation with {0} attributes for {1} times, encryption time: {2}, decryption time: {3}".format(
                attribute_number, loop_number, encryption_time, decryption_time))
    for result in simulation_results:
        print(result)


def fixa_simulation():
    simulation_results = []
    attribute_number = 18
    loop_number = 100
    for i in range(6, 21):
        encryption_time, decryption_time = simulation(attribute_number, loop_number)
        simulation_results.append(
            "Simulation with {0} attributes for {1} times, encryption time: {2}, decryption time: {3}".format(
                attribute_number, loop_number, encryption_time, decryption_time))
    for result in simulation_results:
        print(result)


def pel_simulation():
    simulation_results = []
    loop_number = 100
    for pel_share_with in range(3, 6):
        for _ in range(6, 21):
            encryption_aes(True)
            # test encryption
            start = time.time()
            for i in range(loop_number):
                for j in range(pel_share_with):
                    encryption_aes(True)
                    encryption_rsa()
            end = time.time()
            encryption_time = end - start

            # test decryption
            start = time.time()
            for i in range(loop_number):
                decryption_aes(False)
                decryption_rsa()
            end = time.time()
            decryption_time = end - start
            simulation_results.append(
                "PEL Simulation shared with {0} peers for {1} times, encryption time: {2}, decryption time: {3}".format(
                    pel_share_with, loop_number, encryption_time, decryption_time))
    print(simulation_results)
    for result in simulation_results:
        print(result)


if __name__ == "__main__":
    # change working directory to file location
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # ps_simulation()
    fixa_simulation()
    # pel_simulation()

