# ckt.py

# Copyright 2022 Matteo Alberici
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.

from .entity import Entity


class Ckt(Entity):
    """
    A circuit object with a set of inputs, a set of outputs, and a set of sub-circuits objects.
    A circuit consists of a set of sub-circuits connected through an input-output relationship.
    """

    def __init__(self):
        """
        Construct a "Ckt" object.

        :return: returns nothing
        """

        super().__init__()
        self._subckts = None

    @property
    def subckts(self):
        """
        Get the circuit sub-circuits.

        :return: returns the circuit sub-circuits
        """

        return self._subckts

    @subckts.setter
    def subckts(self, subckts):
        """
        Set the circuit sub-circuits.

        :param subckts: the circuit sub-circuits
        """

        self._subckts = subckts

    def generate(self, file_name=None):
        """
        Generates a circuit object by reading a blif file.

        :param file_name: the name of the blif file
        :return: returns the circuit object
        """

        # Opening the blif file
        blif_file = open(file_name, 'r')
        lines = blif_file.readlines()

        # Defining variables
        circuit_inputs = []
        circuit_outputs = []

        # Setting the circuit inputs and outputs
        for line in lines:
            # Setting the circuit inputs
            if line[0:7] == '.inputs':
                circuit_inputs = line[8:].split(' ')
            # Setting the circuit outputs
            if line[0:8] == '.outputs':
                circuit_outputs = line[9:].split(' ')

        # Removing '\n' from the end of inputs and outputs
        circuit_inputs[-1] = circuit_inputs[-1][:-1]
        circuit_outputs[-1] = circuit_outputs[-1][:-1]

        # Closing the blif file
        blif_file.close()

        # Assigning the circuit inputs and outputs
        self._inputs = circuit_inputs
        self._outputs = circuit_outputs

        return self
