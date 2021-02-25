#!/usr/bin/env python

import psutil
import datetime
import time
import json
import argparse


class Snapshot:
    """A simple class to make and contain snapshots

        Attributes
        ----------
        name : str
            name of the snapshot
        time: str
            time of snapshot
        cpu_info : scpustats
            scpustats with information about cpu
        cpu_percents : list
            array with load in percent per each cpu
        disk_usage: sdiskusage
            sdiskusage with information about current disk
        vm_usage: svmem
            svmem with information about virtual memory
        io_usage: sdiskio
            sdiskio with io information
        net_usage: snetio
            snetio with information about network
    """

    snap_id = 1

    def __init__(self):
        self.name = "SNAPSHOT %d" % Snapshot.snap_id
        Snapshot.snap_id += 1

        self.time = str(datetime.datetime.now())
        self.cpu_info = psutil.cpu_stats()
        self.cpu_percents = psutil.cpu_percent(interval=1, percpu=True)
        self.disk_usage = psutil.disk_usage("E:")
        self.vm_usage = psutil.virtual_memory()
        self.io_usage = psutil.disk_io_counters()
        self.net_usage = psutil.net_io_counters()

    def __str__(self):
        return '%s: %s: %s, cpu_percents(%s) %s, %s, %s, %s' % \
               (self.name, self.time, self.cpu_info, self.cpu_percents, self.disk_usage,
                self.vm_usage, self.io_usage, self.net_usage)


def write_to_file(line: str, file_name: str):
    file_txt = open(file_name, "a")
    print(line, file=file_txt)
    file_txt.close()


def write_to_json(line: str, file_name: str):
    file_json = open(file_name, "a")
    print(line, file=file_json)
    file_json.close()


parser = argparse.ArgumentParser(description='Time of sleep.')
parser.add_argument('minutes', metavar='N', type=int, nargs='?',
                    help='an integer for sleep', default=5)
parser.add_argument("type", type=str, help="type of output file: txt or json")


args = parser.parse_args()
sleep_time = args.minutes
out_type = args.type

while True:
    time.sleep(sleep_time)

    a = Snapshot()

    if out_type == "txt":
        write_to_file(a.__str__(), "out.txt")
    if out_type == "json":
        write_to_json(json.dumps(a.__dict__), "out.json")
