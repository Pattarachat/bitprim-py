 # 
 # Copyright (c) 2017 Bitprim developers (see AUTHORS)
 # 
 # This file is part of Bitprim.
 # 
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Affero General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 # 
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU Affero General Public License for more details.
 # 
 # You should have received a copy of the GNU Affero General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 # 

import bitprim_native as bn

# ------------------------------------------------------

__title__ = "bitprim"
__summary__ = "Bitcoin development platform"
__uri__ = "https://github.com/bitprim/bitprim-py"
__version__ = "1.0.4"
__author__ = "Bitprim Inc"
__email__ = "dev@bitprim.org"
__license__ = "MIT"
__copyright__ = "Copyright 2017 Bitprim developers"


# ------------------------------------------------------
# Tools
# ------------------------------------------------------
def encode_hash(hash):
    return ''.join('{:02x}'.format(x) for x in hash[::-1])

def decode_hash(hash_str):
    hash = bytearray.fromhex(hash_str) 
    hash = hash[::-1] 
    return buffer(hash)


# ------------------------------------------------------
class Wallet:
    # def __init__(self, ptr):
    #     self._ptr = ptr

    @classmethod
    def mnemonics_to_seed(cls, mnemonics):
        wl = bn.word_list_construct()

        for m in mnemonics:
            bn.word_list_add_word(wl, m)

        # # seed = bn.wallet_mnemonics_to_seed(wl)[::-1].hex();
        # seed = bn.wallet_mnemonics_to_seed(wl).hex();

        seed_ptr = bn.wallet_mnemonics_to_seed(wl);
        print(seed_ptr)
        seed = bn.long_hash_t_to_str(seed_ptr).hex();
        print(seed)
        bn.long_hash_t_free(seed_ptr);

        bn.word_list_destruct(wl)
        # print('Wallet.mnemonics_to_seed')

        return seed;

# ------------------------------------------------------
class Header:

    def __init__(self, pointer, height):
        self._ptr = pointer
        self._height = height

    @property
    def height(self):
        return self._height

    @property
    def version(self):
        return bn.header_get_version(self._ptr)

    @version.setter
    def set_version(self, version):
        bn.header_set_version(self._ptr, version)

    @property
    def previous_block_hash(self):
        # print('previous_block_hash BEFORE')
        return bn.header_get_previous_block_hash(self._ptr)
    
    #def set_previous_block_hash(self,hash):        
        #return bn.header_set_previous_block_hash(self._ptr, hash)

    @property
    def merkle(self):
        return bn.header_get_merkle(self._ptr)

    #def set_merkle(self, merkle):
        #bn.header_set_merkle(self._ptr, merkle)
    
    @property
    def timestamp(self): 
        return bn.header_get_timestamp(self._ptr)

    @timestamp.setter
    def set_timestamp(self, timestamp):
        bn.header_set_timestamp(self._ptr, timestamp)

    @property
    def bits(self):
        return bn.header_get_bits(self._ptr)
    
    @bits.setter
    def set_bits(self, bits):
        bn.header_set_bits(self._ptr, bits)
   
    @property
    def nonce(self):
        return bn.header_get_nonce(self._ptr)
    
    @nonce.setter
    def set_nonce(self, nonce):
        bn.header_set_nonce(self._ptr, nonce)


# --------------------------------------------------------------------
class Block:
    def __init__(self, pointer, height):
        self._ptr = pointer
        self._height = height
    
    @property
    def height(self):
        return self._height

    @property
    def header(self):
        return Header(bn.block_get_header(self._ptr), self._height)

    @property
    def transaction_count(self):
        return bn.block_transaction_count(self._ptr)

    @property
    def hash(self):
        return bn.block_hash(self._ptr)

    @property
    def serialized_size(self, version):
        return bn.block_serialized_size(self._ptr, version)

    @property
    def fees(self):
        return bn.block_fees(self._ptr)

    @property
    def claim(self):
        return bn.block_claim(self._ptr)

    @property
    def reward(self, height):
        return bn.block_reward(self._ptr, height)

    def generate_merkle_root(self):
        return bn.block_generate_merkle_root(self._ptr)

# --------------------------------------------------------------------
class MerkleBlock:
    def __init__(self, pointer, height):
        self._ptr = pointer
        self._height = height

    @property
    def height(self):
        return self._height

    @property
    def header(self):
        return Header(bn.merkle_block_get_header(self._ptr), self._height)

    @property
    def is_valid(self):
        return bn.merkle_block_is_valid(self._ptr)

    @property
    def hash_count(self):
        return bn.merkle_block_hash_count(self._ptr)

    @property
    def serialized_size(self, version): 
        return bn.merkle_block_serialized_size(self._ptr, version)

    @property
    def total_transaction_count(self):
        return bn.merkle_block_total_transaction_count(self._ptr)

    def reset(self):
        return bn.merkle_block_reset(self._ptr)



# ------------------------------------------------------
class Point:
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def hash(self):
        # print('Point.hash')
        return bn.point_get_hash(self._ptr) #[::-1].hex()
    
    @property
    def is_valid(self):
        return bn.point_is_valid(self._ptr)

    @property
    def index(self):
        return bn.point_get_index(self._ptr)

    @property
    def get_checksum(self):
        return bn.point_get_checksum(self._ptr)

# ------------------------------------------------------
class History:
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def point_kind(self):
        return bn.history_compact_get_point_kind(self._ptr)

    @property
    def point(self):
        return Point(bn.history_compact_get_point(self._ptr))

    @property
    def height(self):
        return bn.history_compact_get_height(self._ptr)

    @property
    def value_or_previous_checksum(self):
        return bn.history_compact_get_value_or_previous_checksum(self._ptr)

# ------------------------------------------------------
class HistoryList:
    def __init__(self, ptr):
        self._ptr = ptr
        self.constructed = True

    def destroy(self):
        if self.constructed:
            bn.history_compact_list_destruct(self._ptr)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    @property
    def count(self):
        return bn.history_compact_list_count(self._ptr)

    def nth(self, n):
        return History(bn.history_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self.nth(key)

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     # print('__exit__')
    #     self.destroy()

# ------------------------------------------------------
class Stealth:
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def ephemeral_public_key_hash(self):
        return bn.stealth_compact_get_ephemeral_public_key_hash(self._ptr)

    @property
    def get_transaction_hash(self):
        return bn.stealth_compact_get_transaction_hash(self._ptr)
    
    @property
    def public_key_hash(self):
        return bn.stealth_compact_get_public_key_hash(self._ptr)

# ------------------------------------------------------
class StealthList:
    def __init__(self, ptr):
        self._ptr = ptr
        self.constructed = True

    def destroy(self):
        if self.constructed:
            bn.stealth_compact_list_destruct(self._ptr)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    @property
    def count(self):
        return bn.stealth_compact_list_count(self._ptr)

    def nth(self, n):
        return Stealth(bn.stealth_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self.nth(key)



# ------------------------------------------------------
class Chain:
    def __init__(self, chain):
        self.chain = chain

    def fetch_last_height(self, handler):
        bn.chain_fetch_last_height(self.chain, handler)

    def fetch_history(self, address, limit, from_height, handler):
        self.history_fetch_handler_ = handler
        bn.chain_fetch_history(self.chain, address, limit, from_height, self._history_fetch_handler_converter)

    # private members ... TODO: how to make private member functions in Python
    def _history_fetch_handler_converter(self, e, l):
        # print('history_fetch_handler_converter')
        if e == 0: 
            list = HistoryList(l)
        else:
            list = None

        self.history_fetch_handler_(e, list)

##### Stealth

    def stealth_fetch_handler_converter(self, e, l):
        if e == 0: 
            list = StealthList(l)
        else:
            list = None

        self.stealth_fetch_handler_(e, list)

    def fetch_stealth(self, binary_filter_str, from_height, handler):
        self.stealth_fetch_handler_ = handler
        binary_filter = bn.binary_construct_string(binary_filter_str)
        bn.fetch_stealth(self.executor, binary_filter, from_height, self.stealth_fetch_handler_converter)
        #bn.binary_destruct(binary_filter)

    def fetch_block_height(self, hash, handler):
        bn.fetch_block_height(self.chain, hash, handler)


    def _fetch_block_header_converter(self, e, header, height):
        print('_fetch_block_header_converter')

        if e == 0: 
            header = Header(header, height)
        else:
            header = None

        self.fetch_block_header_handler_(e, header)

    def fetch_block_header_by_height(self, height, handler):
        self.fetch_block_header_handler_ = handler
        bn.chain_fetch_block_header_by_height(self.chain, height, self._fetch_block_header_converter)

    def fetch_block_header_by_hash(self, hash, handler):
        self.fetch_block_header_handler_ = handler
        bn.chain_fetch_block_header_by_hash(self.chain, hash, self._fetch_block_header_converter)



    def fetch_block_by_height(self, height, handler):
        bn.chain_fetch_block_by_height(self.chain, height, handler)

    def fetch_block_by_hash(self, hash, handler):
        bn.chain_fetch_block_by_hash(self.chain, hash, handler)

    def fetch_merkle_block_by_height(self, height, handler):
        bn.chain_fetch_merkle_block_by_height(self.chain, height, handler)

    def fetch_merkle_block_by_hash(self, hash, handler):
        bn.chain_fetch_merkle_block_by_hash(self.chain, hash, handler)


class Binary:

    def construct(self):
        return bn.binary_construct()

    def construct_string(self, string_filter):
        return bn.binary_construct_string(string_filter)

    def construct_blocks(self, size, blocks):
        return bn.binary_construct_blocks(size, len(blocks), blocks)

    def blocks(self, binary):
        return bn.binary_blocks(binary)

    def encoded(self, binary):
        return bn.binary_encoded(binary)


# ------------------------------------------------------
class Executor:
    def __init__(self, path, sout = None, serr = None):
        self.executor = bn.construct(path, sout, serr)
        self.constructed = True
        self.running = False

    def destroy(self):
        # print('destroy')

        if self.constructed:
            if self.running:
                self.stop()

            bn.destruct(self.executor)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def run(self):
        ret = bn.run(self.executor)

        if ret:
            self.running = True

        return ret

    def run_wait(self):
        ret = bn.run_wait(self.executor)

        if ret:
            self.running = True

        return ret

    def stop(self):
        # precondition: self.running
        ret = bn.stop(self.executor)

        if ret:
            self.running = False

        return ret

    def init_chain(self):
        return bn.initchain(self.executor)

    @property
    def chain(self):
        return Chain(bn.get_chain(self.executor))

## fetch_stealth(executor_t exec, binary_t filter, size_t from_height, stealth_fetch_handler_t handler){


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print('__exit__')
        self.destroy()





# ------------------------------------------------------

# class ExecutorResource:
#     def __enter__(self):
#         class Executor:
#             ...
#         self.package_obj = Package()
#         return self.package_obj
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.package_obj.cleanup()




# # ------------------------------------------------------
# # 
# # ------------------------------------------------------
# def signal_handler(signal, frame):
#     # signal.signal(signal.SIGINT, signal_handler)
#     # signal.signal(signal.SIGTERM, signal_handler)
#     print('You pressed Ctrl-C')
#     sys.exit(0)

# def history_fetch_handler(e, l): 
#     # print('history_fetch_handler: {0:d}'.format(e))
#     # print(l)
#     # if (e == 0):
#     #     print('history_fetch_handler: {0:d}'.format(e))

#     count = l.count()
#     print('history_fetch_handler count: {0:d}'.format(count))

#     for n in range(count):
#         h = l.nth(n)
#         # print(h)
#         print(h.point_kind())
#         print(h.height())
#         print(h.value_or_spend())

#         # print(h.point())
#         print(h.point().hash())
#         print(h.point().is_valid())
#         print(h.point().index())
#         print(h.point().get_checksum())



# def last_height_fetch_handler(e, h): 
#     if (e == 0):
#         print('Last Height is: {0:d}'.format(h))
#         # if h > 1000:
#         #     # executor.fetch_history('134HfD2fdeBTohfx8YANxEpsYXsv5UoWyz', 0, 0, history_fetch_handler)
#         #     executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
#         #     # executor.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Es la de Juan




# # ------------------------------------------------------
# # Main Real
# # ------------------------------------------------------
# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

# with Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as executor:
# # with Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as executor:
#     # res = executor.initchain()
#     res = executor.run()
#     # print(res)
    
#     time.sleep(3)

#     # executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler)

#     # time.sleep(5)

#     while True:
#         executor.fetch_last_height(last_height_fetch_handler)
#         # executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
#         executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler)
#         time.sleep(10)

#     # print('Press Ctrl-C')
#     # signal.pause()

# # bx fetch-history [-h] [--config VALUE] [--format VALUE] [PAYMENT_ADDRESS]
