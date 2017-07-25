#include "chain_merkle_block.h"

PyObject * bitprim_native_chain_merkle_block_get_header(PyObject* self, PyObject* args){
    PyObject* py_merkle;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle)) {
        return NULL;
    }

    merkle_block_t merkle_block = (merkle_block_t)get_ptr(py_merkle);
    header_t header = merkle_block_header(merkle_block);

  
#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(header, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(header, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

}

PyObject * bitprim_native_chain_merkle_block_is_valid(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    int res = merkle_block_is_valid(block);

    return Py_BuildValue("i", res);   
}

PyObject * bitprim_native_chain_merkle_block_hash_count(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t res = merkle_block_hash_count(block);

    return Py_BuildValue("n", res);   
}


PyObject * bitprim_native_chain_merkle_block_total_transaction_count(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t res = merkle_block_total_transaction_count(block);

    return Py_BuildValue("n", res);   
}


PyObject * bitprim_native_chain_merkle_block_serialized_size(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_merkle_block, &py_version)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    uint64_t res = merkle_block_serialized_size(block, py_version);

    return Py_BuildValue("n", res);   
}

PyObject * bitprim_native_chain_merkle_block_reset(PyObject* self, PyObject* args){
    PyObject* py_merkle_block;

    if ( ! PyArg_ParseTuple(args, "O", &py_merkle_block)) {
        return NULL;
    }

    merkle_block_t block = (merkle_block_t)get_ptr(py_merkle_block);
    merkle_block_reset(block);

    Py_RETURN_NONE;   
}



