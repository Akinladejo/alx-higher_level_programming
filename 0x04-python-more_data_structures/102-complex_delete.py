#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted_k = [k for k, v in a_dictionary.items() if v == value]
    for k in deleted_k:
        del a_dictionary[k]
    return a_dictionary
