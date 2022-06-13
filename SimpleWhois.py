#!/usr/bin/python
 #-*-coding: utf-8-*-
 # pip install python-whois

import whois 
import sys

domain = input("Digite o Domínio: ")
print (domain)
consulta = whois.whois(domain) 
print (consulta.email) 
print (consulta.text)
