#include "chain.h"

// -------------------------------------------------------------------
// header
// -------------------------------------------------------------------



PyObject * bitprim_native_chain_header_get_version(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = header_version(header);

    return Py_BuildValue("n", res);   
}


PyObject * bitprim_native_chain_header_set_version(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_version;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_version)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    header_set_version(header, py_version);

    Py_RETURN_NONE;   
}


PyObject * bitprim_native_chain_header_get_previous_block_hash(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    hash_t res = header_previous_block_hash(header);

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(res, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(res, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

}
/*

PyObject * bitprim_native_chain_header_set_previous_block_hash(PyObject* self, PyObject* args){
    PyObject* py_header;
    Py_ssize_t py_hash;

    if ( ! PyArg_ParseTuple(args, "OO", &py_header, &py_hash)) {
        return NULL;
    }

    char* s = PyString_AsString(py_hash);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    header_t header = (header_t)get_ptr(py_header);
    header_set_previous_block_hash(header, hash);

    Py_RETURN_NONE;   
}


PyObject * bitprim_native_chain_header_set_merkle(PyObject* self, PyObject* args){
    PyObject* py_header;
    Py_ssize_t py_merkle;

    if ( ! PyArg_ParseTuple(args, "OO", &py_header, &py_merkle)) {
        return NULL;
    }

    char* s = PyString_AsString(py_merkle);
    uint8_t * hash = (uint8_t*) malloc (sizeof(uint8_t[32]));
    hex2bin(s,&hash[31]);

    header_t header = (header_t)get_ptr(py_header);
    header_set_merkle(header, hash);

    Py_RETURN_NONE;   
}

*/

PyObject * bitprim_native_chain_header_get_merkle(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    hash_t res = header_merkle(header);

#if PY_MAJOR_VERSION >= 3
    return PyCapsule_New(res, NULL, NULL);
#else /* PY_MAJOR_VERSION >= 3 */
    return PyCObject_FromVoidPtr(res, NULL);
#endif /* PY_MAJOR_VERSION >= 3 */

}


PyObject * bitprim_native_chain_header_get_timestamp(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = header_timestamp(header);

    return Py_BuildValue("n", res);   
}


PyObject * bitprim_native_chain_header_set_timestamp(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_timestamp;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_timestamp)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    header_set_timestamp(header, py_timestamp);

    Py_RETURN_NONE;   
}



PyObject * bitprim_native_chain_header_get_bits(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = header_bits(header);

    return Py_BuildValue("n", res);   
}


PyObject * bitprim_native_chain_header_set_bits(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_bits;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_bits)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    header_set_bits(header, py_bits);

    Py_RETURN_NONE;   
}


PyObject * bitprim_native_chain_header_get_nonce(PyObject* self, PyObject* args){
    PyObject* py_header;

    if ( ! PyArg_ParseTuple(args, "O", &py_header)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    uint32_t res = header_nonce(header);

    return Py_BuildValue("n", res);  
}


PyObject * bitprim_native_chain_header_set_nonce(PyObject* self, PyObject* args){
    PyObject* py_header;
    uint32_t py_nonce;

    if ( ! PyArg_ParseTuple(args, "OI", &py_header, &py_nonce)) {
        return NULL;
    }

    header_t header = (header_t)get_ptr(py_header);
    header_set_nonce(header, py_nonce);

    Py_RETURN_NONE;   
}

