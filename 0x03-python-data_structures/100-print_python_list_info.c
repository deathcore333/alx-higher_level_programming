#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that prints basic info about
 * python lists
 * @p: pointer to a python object
 */

void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, PyUnicode_AsUTF8(PyList_GetItem(p, i)));
	}
}
