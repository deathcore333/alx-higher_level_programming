#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function that prints basic info aboutpython lists
 * @p: pointer to a python object
 */

void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_size(p); i++)
	{
	printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
