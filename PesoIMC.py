#! /usr/bin/env python
#-*- coding: UTF-8 -*-

import os, sys

print( 'IMC')

peso = raw_input (' Digite seu peso e aperte enter: ')
altura = raw_input ('Digite a sua altura e aperte enter: ')
imc = float(peso)/(float(altura)*float(altura))

print 'Seu IMC é : ', imc