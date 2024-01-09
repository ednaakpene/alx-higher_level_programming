#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that prints list
 * @PyObject: function parameter
 *@p: function parameter
 * Return: return void
 **/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int e;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	
	for (e = 0; e < size; e++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[e])->tp_name);
}
