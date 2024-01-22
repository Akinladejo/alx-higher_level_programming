#include <stdlib.h>
#include <stdio.h>
#include <python3.8/Python.h>

/**
 * print_python_list_info - print info about python list.
 * @p: pointer to a list object
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t idx = 0;
	PyObject *item = NULL;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject*)(p))->allocated);
	for (; idx < PyList_Size(p); idx++)
	{
		item = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", (int)idx, item->ob_type->tp_name);
	}
}
