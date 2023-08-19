#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %lu\n", Py_SIZE(list));
    printf("[*] Allocated = %lu\n", list->allocated);

    for (Py_ssize_t i = 0; i < Py_SIZE(list); ++i) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, typeName);
    }
}
