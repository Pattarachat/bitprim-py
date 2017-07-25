#include <Python.h>
#include <bitprim/nodecint.h>
#include "utils.h"

PyObject * bitprim_native_binary_construct(PyObject* self, PyObject* args);

PyObject * bitprim_native_binary_construct_string(PyObject* self, PyObject* args);

PyObject * bitprim_native_binary_construct_blocks(PyObject* self, PyObject* args);

PyObject * bitprim_native_binary_blocks(PyObject* self, PyObject* args);

PyObject * bitprim_native_binary_encoded(PyObject* self, PyObject* args);
