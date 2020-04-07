# -*- coding:utf-8 -*-
# !/usr/bin/python

import os

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
def simulation(attribute_number, eta):
    generate_key_slice(attribute_number, True)
    # test encryption
    encryption_abe(attribute_number, True)
    encryption_aes(True)
    abe_size = os.stat("encrypted.kpabe")
    aes_size = os.stat('encrypted.txt')
    return (abe_size.st_size + aes_size.st_size) * eta


def ps_simulation():
    simulation_results = []
    for attribute_number in range(6, 21):
        encrypted_size = simulation(attribute_number, attribute_number)
        simulation_results.append(
            "Simulation with {0} attributes, accumulated as {1} organizations, encrypted file size: {2}".format(
                attribute_number, attribute_number, encrypted_size))
    for result in simulation_results:
        print(result)


def fixa_simulation():
    simulation_results = []
    attribute_number = 22
    for eta in range(6, 21):
        encrypted_size = simulation(attribute_number, eta)
        simulation_results.append(
            "Simulation with {0} attributes, accumulated as {1} organizations, encrypted file size: {2}".format(
                attribute_number, eta, encrypted_size))
    for result in simulation_results:
        print(result)


def csl_simulation():
    simulation_results = []
    # Accumulate original data size
    for eta in range(6, 21):
        tx_size = os.stat("transaction_tau.txt")
        accumulated_size = tx_size.st_size * eta
        simulation_results.append(
            "Simulation CSL, accumulated as {0} organizations, encrypted file size: {1}".format(
                eta, accumulated_size))
    for result in simulation_results:
        print(result)


def pel_simulation():
    simulation_results = []
    for pel_share_with in range(3, 6):
        for eta in range(6, 21):
            # test encryption
            encryption_aes(True)
            encryption_rsa()
            aes_size = os.stat("encrypted.txt")
            rsa_size = os.stat("encrypted-rsa.txt")
            encrypted_size = eta * pel_share_with * (aes_size.st_size + rsa_size.st_size)
            simulation_results.append(
                "Simulation PEL shared with {0}, accumulated as {1} organizations, encrypted file size: {2}".format(
                    pel_share_with, eta, encrypted_size))
    for result in simulation_results:
        print(result)


if __name__ == "__main__":
    # change working directory to file location
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # ps_simulation()
    fixa_simulation()
    # csl_simulation()
    # pel_simulation()
