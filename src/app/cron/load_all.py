#!/usr/bin/env python3

from app.cron import load_balance
from app.cron import load_currencie
from app.cron import load_symbol


def loads():
    load_balance.do_load()
    load_currencie.do_load()
    load_symbol.do_load()


def main():
    do_loads()


if __name__ == '__main__':
    main()
