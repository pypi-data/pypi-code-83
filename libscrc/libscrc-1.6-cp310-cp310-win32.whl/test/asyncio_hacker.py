# -*- coding:utf-8 -*-
""" ASYNCIO HACKER """
# !/usr/bin/python
# Python:   3.5.2+
# Platform: Windows/Linux/MacOS/ARMv7
# Author:   Heyn (heyunhuan@gmail.com)
# Program:  ASYNCIO HACKER.
# Package:  pip install libscrc psutil.
# History:  2021-03-23 Wheel Ver:0.1 [Heyn] Initialize

import struct
import psutil
import libscrc
import asyncio
import logging

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor, as_completed

# logging.basicConfig( format='%(asctime)s - %(message)s', level=print, filename='libscrc.log', filemode='a' )

print( 'START' )
# from numba import cuda
# from numba import jit, prange, vectorize

PROCESS_POOL_MAX_WORKERS = psutil.cpu_count() - 2
THREAD_POOL_MAX_WORKERS  = 20

#\xE1\x7C\x90\x64
DATA1 = b'\x9F\x49\xD3\x60\xCD\x3A\xBD\x2D\x6D\xB8\xDA'
CRC1H, CRC1L = 0x58, 0x4A

DATA2 = b'\x57\xA0\x47\xD2\xBC\x8C\x86\x9E\x44\xB9\x20'
CRC2H, CRC2L = 0xE8, 0x11

DATA3 = b'\x05\x00\xBA\x68\x60\x94\x30\x7B\xA7\x81\x24'
CRC3H, CRC3L = 0x69, 0xA7


def __crc16( poly=0x8005, init=0, refin=False, refout=False  ):
    crc_1 = libscrc.hacker16( data=DATA1, poly=poly, init=init, xorout=0x0000, refin=refin, refout=refout )
    value = struct.pack( '>H', crc_1 )
    if ( CRC1H not in value ) or ( CRC1L not in value ):
        return

    crc_2 = libscrc.hacker16( data=DATA2, poly=poly, init=init, xorout=0x0000, refin=refin, refout=refout )
    value = struct.pack( '>H', crc_2 )
    if ( CRC2H not in value ) or ( CRC2L not in value ):
        return

    crc_3 = libscrc.hacker16( data=DATA3, poly=poly, init=init, xorout=0x0000, refin=refin, refout=refout )
    value = struct.pack( '>H', crc_3 )
    if ( CRC3H not in value ) or ( CRC3L not in value ):
        return

    print( 'POLY=0x{:04X}, INIT=0x{:04X}, VALUE=0x{:04X}'.format( poly, init, crc_1 ) )
    print( 'POLY=0x{:04X}, INIT=0x{:04X}, VALUE=0x{:04X}'.format( poly, init, crc_2 ) )
    print( 'POLY=0x{:04X}, INIT=0x{:04X}, VALUE=0x{:04X}'.format( poly, init, crc_3 ) )
    print( 'SUCCESS!!!!' )
    print( 'POLY=0x{:04X}, INIT=0x{:04X}, VALUE=0x{:04X}'.format( poly, init, crc_3 ) )

# @jit( parallel=True, nogil=True )
def crack_crc16( poly=0x8005 ):
    with ThreadPoolExecutor( max_workers=THREAD_POOL_MAX_WORKERS ) as executor:
        tasks = [ executor.submit( __crc16, poly, init ) for init in range( 65536 ) ]
        for _ in as_completed( tasks ):
            pass
    # for init in range( 65536 ):
    #     __crc16( poly, init )


def main( ):
    with ProcessPoolExecutor( max_workers=PROCESS_POOL_MAX_WORKERS ) as executor:
        tasks = [ executor.submit( crack_crc16, poly ) for poly in range( 65536 ) ]
        for _ in as_completed( tasks ):
            pass

    print( 'OVER' )

if __name__ == '__main__':
    main()
