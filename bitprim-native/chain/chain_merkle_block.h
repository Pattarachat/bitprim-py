#include <Python.h>
#include <bitprim/nodecint.h>
#include "../utils.h"

PyObject * bitprim_native_chain_merkle_block_get_header(PyObject* self, PyObject* args);

PyObject * bitprim_native_chain_merkle_block_is_valid(PyObject* self, PyObject* args);

PyObject * bitprim_native_chain_merkle_block_hash_count(PyObject* self, PyObject* args);

PyObject * bitprim_native_chain_merkle_block_total_transaction_count(PyObject* self, PyObject* args);

PyObject * bitprim_native_chain_merkle_block_serialized_size(PyObject* self, PyObject* args);

PyObject * bitprim_native_chain_merkle_block_reset(PyObject* self, PyObject* args);
