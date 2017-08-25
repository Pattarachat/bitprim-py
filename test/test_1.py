import unittest
import os
import signal
import sys
import time
import threading
import bitprim
from datetime import datetime

def encode_hash(h):
    if (sys.version_info > (3, 0)):
        return ''.join('{:02x}'.format(x) for x in h[::-1])
    else:
        return h[::-1].encode('hex')

def decode_hash(hash_str):
    h = bytearray.fromhex(hash_str) 
    h = h[::-1] 
    return bytes(h)

class TestBitprim(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Preparing Tests ...')
        # cls._exec = bitprim.Executor("", sys.stdout, sys.stderr)
        cls._exec = bitprim.Executor("", None, None)
        res = cls._exec.init_chain()

        # if not res:
        #     raise RuntimeError('init_chain() failed')

        res = cls._exec.run_wait()
        if not res:
            raise RuntimeError('run_wait() failed')

        cls.chain = cls._exec.chain

    @classmethod
    def tearDownClass(cls):
        print('Finishing')
        # bn.destruct(cls._exec)
        cls._exec.stop()
        cls._exec._destroy()
        

    def test_fetch_last_height(self):
        evt = threading.Event()

        _error = [None]
        _height = [None]

        def handler(error, height):
            _error[0] = error
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_last_height(handler)
        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)



    def test_fetch_block_header_by_height(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _header = [None]

        def handler(error, header):
            _error[0] = error
            _header[0] = header
            evt.set()

        self.__class__.chain.fetch_block_header_by_height(0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_header[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_header[0].height, 0)
        self.assertEqual(encode_hash(_header[0].hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header[0].merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header[0].previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header[0].version, 1)
        self.assertEqual(_header[0].bits, 486604799)
        self.assertEqual(_header[0].nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_header[0].timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def test_fetch_block_header_by_hash(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _header = [None]

        def handler(error, header):
            _error[0] = error
            _header[0] = header
            evt.set()

        hash = decode_hash('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.__class__.chain.fetch_block_header_by_hash(hash, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_header[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_header[0].height, 0)
        self.assertEqual(encode_hash(_header[0].hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header[0].merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header[0].previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header[0].version, 1)
        self.assertEqual(_header[0].bits, 486604799)
        self.assertEqual(_header[0].nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_header[0].timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def test_fetch_block_by_height(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _block = [None]

        def handler(error, block):
            _error[0] = error
            _block[0] = block
            evt.set()

        self.__class__.chain.fetch_block_by_height(0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_block[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_block[0].header.height, 0)
        self.assertEqual(encode_hash(_block[0].header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_block[0].header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_block[0].header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_block[0].header.version, 1)
        self.assertEqual(_block[0].header.bits, 486604799)
        self.assertEqual(_block[0].header.nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_block[0].header.timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def test_fetch_block_by_hash(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _block = [None]

        def handler(error, block):
            _error[0] = error
            _block[0] = block
            evt.set()

        hash = decode_hash('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.__class__.chain.fetch_block_by_hash(hash, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_block[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_block[0].header.height, 0)
        self.assertEqual(encode_hash(_block[0].header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_block[0].header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_block[0].header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_block[0].header.version, 1)
        self.assertEqual(_block[0].header.bits, 486604799)
        self.assertEqual(_block[0].header.nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_block[0].header.timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def wait_until_block(self, desired_height):

        _error = [0]
        _block_fetched = [False]        

        def handler(error, height):
            print("Handler invoked, height %d" % height)
            _error[0] = error
            _block_fetched[0] = (height >= desired_height)

        while not _block_fetched[0] and _error[0] == 0:
            self.__class__.chain.fetch_last_height(handler)
            if not _block_fetched[0]:
                time.sleep(30)

    def test_fetch_block_height(self):
        evt = threading.Event()

        _error = [None]
        _height = [None]

        def handler(error, height):
            _error[0] = error
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_block_height(decode_hash("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"), handler)
        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_height[0], 0)

#TODO NEEDS TO WAIT_UNTIL_BLOCK(170) TO WORK
    # def test_fetch_spend(self):       
    #     evt = threading.Event()

    #     _error = [None]
    #     _point = [None]

    #     def handler(error, point):
    #         _error[0] = error
    #         _point[0] = point
    #         evt.set()

    #     output_point = bitprim.OutputPoint.construct_from_hash_index(decode_hash("0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9"),0)
    #     self.__class__.chain.fetch_spend(output_point, handler)
    #     evt.wait()

    #     self.assertNotEqual(_error[0], None)
    #     self.assertNotEqual(_point[0], None)
    #     self.assertEqual(_error[0], 0)

    #     hashresult = _point[0].hash
    #     self.assertEqual(encode_hash(hashresult), "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16")
    #     self.assertEqual(_point[0].index, 0)

    def test_fetch_merkle_block_by_hash(self):
        evt = threading.Event()

        _error = [None]
        _merkle = [None]
        _height = [None]

        def handler(error, merkle, height):
            _error[0] = error
            _merkle[0] = merkle
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_merkle_block_by_hash(decode_hash("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"), handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_merkle[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)

        self.assertEqual(_merkle[0].height, 0)
        self.assertEqual(_merkle[0].total_transaction_count, 1)
        _header = _merkle[0].header
        self.assertEqual(encode_hash(_header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header.version, 1)
        self.assertEqual(_header.bits, 486604799)
        self.assertEqual(_header.nonce, 2083236893)

    def test_fetch_merkle_block_by_height(self):
        evt = threading.Event()

        _error = [None]
        _merkle = [None]
        _height = [None]

        def handler(error, merkle, height):
            _error[0] = error
            _merkle[0] = merkle
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_merkle_block_by_height(0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_merkle[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)

        self.assertEqual(_merkle[0].height, 0)
        self.assertEqual(_merkle[0].total_transaction_count, 1)
        _header = _merkle[0].header
        self.assertEqual(encode_hash(_header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header.version, 1)
        self.assertEqual(_header.bits, 486604799)
        self.assertEqual(_header.nonce, 2083236893)

    #  def test_fetch_compact_block_by_height(self):
    #     evt = threading.Event()

    #     _error = [None]
    #     _compact = [None]
    #     _height = [None]

    #     def handler(error, compact):
    #         _error[0] = error
    #         _compact[0] = compact
    #         #_height[0] = height
    #         evt.set()

    #     self.__class__.chain.fetch_compact_block_by_height(0, handler)

    #     evt.wait()

    #     self.assertNotEqual(_error[0], None)
    #     self.assertNotEqual(_compact[0], None)
    #     #self.assertNotEqual(_height[0], None)
    #     self.assertEqual(_error[0], 0)

    #     #self.assertEqual(_compact[0].height, 0)
    #     #self.assertEqual(_compact[0].total_transaction_count, 1)

    # def test_fetch_compact_block_by_hash(self):
    #     evt = threading.Event()

    #     _error = [None]
    #     _compact = [None]
    #     _height = [None]

    #     def handler(error, compact, height):
    #         _error[0] = error
    #         _compact[0] = compact
    #         _height[0] = height
    #         evt.set()

    #     self.__class__.chain.fetch_compact_block_by_hash(decode_hash("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"), handler)

    #     evt.wait()

    #     self.assertNotEqual(_error[0], None)
    #     self.assertNotEqual(_compact[0], None)
    #     self.assertEqual(_error[0], 0)

    #     #self.assertEqual(_compact[0].height, 0)
    #     #self.assertEqual(_compact[0].total_transaction_count, 1)

    def test_fetch_stealth(self):
        evt = threading.Event()

        _error = [None]
        _list = [None]

        def handler(error, list):
            _error[0] = error
            _list[0] = list
            evt.set()

        self.__class__.chain.fetch_stealth("1111", 0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        #self.assertNotEqual(_list[0], None)
        self.assertEqual(_error[0], 0)

        self.assertEqual(_list[0].count, 0)

    # def test_fetch_stealth_complete_chain(self):
    #     evt = threading.Event()

    #     _error = [None]
    #     _list = [None]

    #     def handler(error, list):
    #         _error[0] = error
    #         _list[0] = list
    #         evt.set()

    #     self.__class__.chain.fetch_stealth("01", 325500, handler)

    #     evt.wait()

    #     self.assertNotEqual(_error[0], None)
    #     self.assertNotEqual(_list[0], None)
    #     self.assertEqual(_error[0], 0)

        #     _stealthlist = _list[0]
    #     stealth = _stealthlist.nth(0)

    #     self.assertEqual(_list[0].count, 4)
    #     self.assertEqual(decode_hash(stealth.ephemeral_public_key_hash), "022ec7cd1d0697e746c4044a4582db99ac85e9158ebd2c0fb2a797759ca418dd8d")


    def test_fetch_transaction(self):
        evt = threading.Event()

        _error = [None]
        _transaction = [None]
        _height = [None]
        _index = [None]

        tx_block_height = 170 #First non-coinbase tx belongs to this block
        self.wait_until_block(tx_block_height)

        def handler(error, transaction, height, index):
            _error[0] = error
            _transaction[0] = transaction
            _height[0] = height
            _index[0] = index
            evt.set()

        hash_hex_str = 'f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16'
        hash = decode_hash(hash_hex_str)
        self.__class__.chain.fetch_transaction(hash, True, handler)

        evt.wait()
        #No error
        self.assertEqual(_error[0], 0)
        #Tx from block zero, must have height zero
        self.assertEqual(_height[0], tx_block_height)
        #It's the only non-coinbase tx from the block, so index should be 1
        self.assertEqual(_index[0], 1)
        #Validate Tx contents
        tx = _transaction[0]
        self.assertEqual(tx.version, 1)
        self.assertEqual(encode_hash(tx.hash), hash_hex_str)
        self.assertEqual(tx.locktime, 0)
        self.assertEqual(tx.serialized_size(wire=True), 275)
        self.assertEqual(tx.serialized_size(wire=False), 275) #TODO(dario) Does it make sense that it's the same value?
        self.assertEqual(tx.fees, 0)
        self.assertTrue(0 <= tx.signature_operations <= 2 ** 64)
        self.assertEqual(tx.signature_operations_bip16_active(True), 2)
        self.assertEqual(tx.signature_operations_bip16_active(False), 2) #TODO(dario) Does it make sense that it's the same value?
        self.assertEqual(tx.total_input_value, 0)
        self.assertEqual(tx.total_output_value, 5000000000L) #50 BTC = 5 M Satoshi
        self.assertEqual(tx.is_coinbase, False)
        self.assertEqual(tx.is_null_non_coinbase, False)
        self.assertEqual(tx.is_oversized_coinbase, False)
        self.assertEqual(tx.is_overspent, True)
        self.assertEqual(tx.is_double_spend(True), False)
        self.assertEqual(tx.is_double_spend(False), False)
        self.assertEqual(tx.is_missing_previous_outputs, True)
        self.assertEqual(tx.is_final(tx_block_height, 0), True)
        self.assertEqual(tx.is_locktime_conflict, False)

# -----------------------------------------------------------------------------------------------
        
if __name__ == '__main__':
    unittest.main()
