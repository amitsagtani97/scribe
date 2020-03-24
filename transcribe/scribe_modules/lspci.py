from . import ScribeModuleBaseClass

import sys


class Lspci(ScribeModuleBaseClass):

    def __init__(self, input_dict=None, module_name=None, host_name=None,
                 input_type=None, scribe_uuid=None):
        ScribeModuleBaseClass.__init__(self, module_name=module_name,
                                       input_dict=input_dict,
                                       host_name=host_name,
                                       input_type=input_type,
                                       scribe_uuid=scribe_uuid)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def parse(self):
        lspci_data = self._input_dict
        lspci_lines = lspci_data.split('\n\n')

        if len(lspci_lines) <= 1:
            print("No data is available to process.")
            sys.exit(1)

        # lspci_lines contains a list of slots and its information.
        # We are yielding a dict of these individual slots.
        for i in range(len(lspci_lines)):
            slot_data = lspci_lines[i].split('\n')
            # sample - ['Slot:\t00:00.0', 'Class:\tHost bridge', 'Vendor:\tIntel Corporation' ..... ]
            slot_dict = {}
            for slot_info in slot_data:
                key = slot_info.split(':\t')[0].strip()
                value = slot_info.split(':\t')[1].strip()
                slot_dict[key] = value
            yield slot_dict
