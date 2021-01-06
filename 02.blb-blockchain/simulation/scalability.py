# -*- coding: UTF-8 -*-
import datetime
import math
import random
from numpy import random as nprandom
import string
from hashlib import sha256


##############################
# Proof of Work
##############################


def pow(participants, tx_speed, total_tx_time, ddos_target_number, batch_size, block_size, network_speed,
        network_avg_delay, network_delay_std, propagation_rate):
    total_transactions = tx_speed * total_tx_time
    node_useless_probability = float(ddos_target_number) / participants

    batch_round = math.ceil(total_transactions / batch_size)
    round_period = total_tx_time / batch_round

    pow_sum_time = datetime.timedelta(0)
    for _ in range(batch_round):
        start_time = datetime.datetime.now()
        while True:
            pow_calculate_hash()
            generate_block(block_size)
            if random.uniform(0.0, 1.0) > node_useless_probability:
                # if DDoS attack at the miner, then recalculate the hash by other nodes.
                break
        end_time = datetime.datetime.now()
        propagation_time_ms = propagation_time_in_network(block_size, network_speed, participants, network_avg_delay,
                                                          network_delay_std, propagation_rate)
        pow_sum_time += end_time - start_time + datetime.timedelta(milliseconds=propagation_time_ms) + \
                        datetime.timedelta(seconds=round_period)
    pow_sum_time_ms = pow_sum_time.seconds * 1000 + pow_sum_time.microseconds / 1000
    print("PoW:\t" + str(pow_sum_time_ms))


def pow_calculate_hash():
    # difficulty_1_target = 0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    difficulty_01_target = 0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    while True:
        seed_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        magic_number = int.from_bytes(sha256(seed_string.encode('utf-8')).digest(), 'big')
        if magic_number < difficulty_01_target:
            break


# block size is defined as the size of the new block in KB
def generate_block(block_size):
    with open("new_block", "wb") as out:
        out.truncate(block_size * 1024)


# simulate new block propagation in network, return propagation time
# block_size: 5KB, network_speed: 200KB/s, participants: 200,
# network_avg_delay: 200ms, network_delay_std: 100, propagation_rate: 2
# return: sum_time (ms)
def propagation_time_in_network(block_size, network_speed, participants, network_avg_delay, network_delay_std,
                                propagation_rate):
    propagation_round = round(math.log(participants, propagation_rate))
    propagation_round_time = abs(nprandom.normal(loc=network_avg_delay, scale=network_delay_std,
                                                 size=(propagation_round,)))
    transmit_block_time = float(block_size) / network_speed
    sum_time = 0
    for index in range(propagation_round):
        sum_time += transmit_block_time + propagation_round_time[index]
    return sum_time


##############################
# Proof of Stake
##############################


def pos(participants, tx_speed, total_tx_time, ddos_target_number, batch_size, block_size, network_speed,
        network_avg_delay, network_delay_std, propagation_rate, stake_std, stake_avg):
    total_transactions = tx_speed * total_tx_time
    participants_stake_list = list(nprandom.normal(loc=stake_avg, scale=stake_std, size=(participants, )))
    # set those who takes minus stakes to 0
    participants_stake_list_arranged = [item if item >= 0 else 0 for item in participants_stake_list]
    participants_stake_list_arranged.sort(reverse=True)  # sort based on stakes, the first one is the largest one
    attack_stake_sum = 0.0
    for index in range(ddos_target_number):
        attack_stake_sum += participants_stake_list_arranged[index]
    # if random.uniform(0.0, 1.0) greater than attack_stake_portion, then this participant is not under ddos attack.
    attack_stake_portion = attack_stake_sum / sum(participants_stake_list_arranged)

    batch_round = math.ceil(total_transactions / batch_size)
    round_period = total_tx_time / batch_round

    pos_sum_time = datetime.timedelta(0)
    for _ in range(batch_round):
        start_time = datetime.datetime.now()
        while True:
            pos_calculate_hash()
            generate_block(block_size)
            if random.uniform(0.0, 1.0) > attack_stake_portion:
                # if DDoS attack at the miner, then recalculate the hash by other nodes.
                break
        end_time = datetime.datetime.now()
        propagation_time_ms = propagation_time_in_network(block_size, network_speed, participants, network_avg_delay,
                                                          network_delay_std, propagation_rate)
        pos_sum_time += end_time - start_time + datetime.timedelta(milliseconds=propagation_time_ms) + \
                        datetime.timedelta(seconds=round_period)
    pos_sum_time_ms = pos_sum_time.seconds * 1000 + pos_sum_time.microseconds / 1000
    print("PoS:\t" + str(pos_sum_time_ms))


# The difference between pow & pos: only generate a new sha256 based on seed_string
def pos_calculate_hash():
    seed_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    # generate new hash based on seed_string
    int.from_bytes(sha256(seed_string.encode('utf-8')).digest(), 'big')


##############################
# Committee Members Auction
##############################

def cma(participants, tx_speed, total_tx_time, ddos_target_number, batch_size, block_size, network_speed,
        network_avg_delay, network_delay_std, propagation_rate, round_period):
    # if random.uniform(0.0, 1.0) greater than attack_stake_portion, then this participant is not under ddos attack.
    attack_stake_portion = float(ddos_target_number) / participants

    batch_round = math.ceil(total_tx_time / round_period)
    # total_transactions = tx_speed * total_tx_time
    # batch_round = math.ceil(total_transactions / batch_size)

    cma_sum_time = datetime.timedelta(0)
    for _ in range(batch_round):
        start_time = datetime.datetime.now()
        while True:
            cma_calculate_hash()  # elect committee member
            cma_calculate_hash()  # calculate hash_prev
            cma_calculate_hash()  # calculate hash_next
            generate_block(block_size)
            if random.uniform(0.0, 1.0) > attack_stake_portion:
                # if DDoS attack at the miner, then recalculate the hash by other nodes.
                break
        end_time = datetime.datetime.now()
        propagation_time_ms = propagation_time_in_network(block_size, network_speed, participants, network_avg_delay,
                                                          network_delay_std, propagation_rate)
        cma_sum_time += end_time - start_time + datetime.timedelta(milliseconds=propagation_time_ms) + \
                        datetime.timedelta(seconds=round_period)
    cma_sum_time_ms = cma_sum_time.seconds * 1000 + cma_sum_time.microseconds / 1000
    print("CMA:\t" + str(cma_sum_time_ms))


# There is no difference between cma & pos. This can be used as
# "Elect committee member" / "calculate hash_prev" / "calculate hash_next""
def cma_calculate_hash():
    seed_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    # generate new hash based on seed_string
    int.from_bytes(sha256(seed_string.encode('utf-8')).digest(), 'big')


def main():
    ##############################
    # Global Parameters Set Start
    ##############################
    participants = 200
    # transaction speed is defined as tx number in a second (tx/s)
    tx_speed = 50
    # total transaction time is defined as tx seconds
    total_tx_time = 30
    # DDoS attack at target number of nodes
    ddos_target_number = 20
    # transaction number included in a block
    batch_size = 20
    # block size in KB
    block_size = 5
    # network speed in KB/s
    network_speed = 200
    # network delay in ms
    network_avg_delay = 100
    network_delay_std = 100
    propagation_rate = 2

    # standard deviation of stakes for pos
    stake_std = 15
    stake_avg = 0

    # round period in seconds for cma
    round_period = 2
    ##############################
    # Global Parameters Set End
    ##############################

    # start experiment with iterated parameters
    # for participants in [100, 150, 200, 400, 800]:
    # for tx_speed in [10, 20, 30, 40, 50]:
    # for total_tx_time in [10, 20, 30, 40, 50, 60]:
    for ddos_target_number in [0, 20, 40, 60, 80, 100]:
        pow(participants, tx_speed, total_tx_time, ddos_target_number, batch_size, block_size, network_speed,
            network_avg_delay, network_delay_std, propagation_rate)
        pos(participants, tx_speed, total_tx_time, ddos_target_number, batch_size, block_size, network_speed,
            network_avg_delay, network_delay_std, propagation_rate, stake_std, stake_avg)
        cma(participants, tx_speed, total_tx_time, ddos_target_number, batch_size, block_size, network_speed,
            network_avg_delay, network_delay_std, propagation_rate, round_period)


if __name__ == "__main__":
    main()
