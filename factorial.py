# Factorial Computation
# Copyright (C) 2020 Richard Ricardo

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Computes the factorial of a number"""
import math
import os
import random
import sys

import matplotlib
import numpy as np

__author__ = "Richard Ricardo"
__version__ = "0.0.1"

np.random.seed(42)


class Model(object):
	def __init__(self):
		pass

def factorial(number):
	if number == 0 or number == 1:
		return 1
	else:
		return number * factorial(number - 1)

def main():
	models = Model()
	answer = factorial(4)
