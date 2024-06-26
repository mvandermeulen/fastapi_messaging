#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright: Wilde Consulting
  License: Apache 2.0

VERSION INFO::

    $Repo: fastapi_messaging
  $Author: Anders Wiklund
    $Date: 2024-04-09 05:39:25
     $Rev: 4
"""

# BUILTIN modules
import json
import asyncio
import argparse
from pprint import pprint

# Third party modules
from redis.asyncio import from_url

# Local modules
from src.core.setup import config


# ---------------------------------------------------------
#
async def viewer(args: argparse.Namespace):
    """ Show cached Redis order.

    :param args: Command line arguments.
    """
    client = from_url(config.redis_url)

    if response := await client.get(args.order_id):
        pprint(json.loads(response.decode()), width=120)

    else:
        print(f'NOT CACHED: {args.order_id}')


# ---------------------------------------------------------

if __name__ == "__main__":
    Form = argparse.ArgumentDefaultsHelpFormatter
    description = 'A utility script that let you view cached order data.'
    parser = argparse.ArgumentParser(description=description, formatter_class=Form)
    parser.add_argument("order_id", type=str, help="Specify Order ID")
    arguments = parser.parse_args()

    asyncio.run(viewer(arguments))
