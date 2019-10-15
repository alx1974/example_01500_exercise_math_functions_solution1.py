#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# definierte 4 funktionen addieren , subtrahieren, dividieren und multiplizieren mit den jeweiligen
# rueckgabe werten und printe sie aus
# main function

def addieren(wert1, wert2):
    return wert1 + wert2


def subtrahieren(wert1, wert2):
    return wert1 - wert2


def dividieren(wert1, wert2):
    try:
        return wert1 / wert2
    except Exception:
        print("Fehler bei der Division!!")

def multiplizieren(wert1, wert2):
    return wert1 * wert2


if __name__ == "__main__":
    # print("Addition : " + str(addieren(5, 3)))
    # print("Subtraktion : " + str(subtrahieren(5, 3)))
    # print("Division : " + str(dividieren(5, 3)))
    # print("Multiplikation : " + str(multiplizieren(5, 3)))

    # b) mit input
    wert1 = int(input("Gib die erste Zahl ein : "))
    wert2 = int(input("Gin die zweite Zahl ein : "))
    print("Addition : " + str(addieren(wert1, wert2)))
    print("Subtraktion : " + str(subtrahieren(wert1, wert2)))
    print("Division : " + str(round(dividieren(wert1, wert2), 3)))
    print("Multiplikation : " + str(multiplizieren(wert1, wert2)))
