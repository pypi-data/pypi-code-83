#            AMX IP Address Import File Information

# Your IP Address data must be delimited by commas (",") or pipes ("|").

# You can have either a "#" or ";" in column one of your text file to designate
# comment lines. They will be ignored during the import process.

# The order of the data must be as follows:

#    IP Address,Description,Port,Ping Host Flag

# If no Port is specified, then the default is 1319.

# For the Ping Host Flag value, please specify either 1 for TRUE or 0 for FALSE.

# If no Ping Host Flag specified, then the default is TRUE.

# Example:
# ;----------------------------------
# ;  North Campus Meeting Rooms
# ;----------------------------------
# 10.24.94.24,First Floor-Ben Hogan Room,1319,1
# 10.24.94.37,Second Floor-Arnold Palmer Room,1319,1
# 10.24.94.44,Third Floor-Board Room,1319,1

# ^^ This is the file format we'll be creating, so it can be
# directly imported into AMX Firmware

# import json
from logging import debug, info, warning, error, critical

class MasterFirmware():

    def __init__(self, firmware_dir='firmware_lists/'):
        self.firware_dir = firmware_dir


    def set_systems(self, systems):
        self.systems = systems
        info(f"amxfirmware.py MasterFirmware() added {len(self.systems)} systems")        


    def set_versions(self, ni_700_current='4.1.419', ni_x100_current='4.1.419', nx_current='1.6.179'):
        self.legacy_ni = '3.60.453'
        self.interim_nx = '1.4.92'
        self.ni_700_current = ni_700_current
        self.ni_700_file_path = f"NI-700 Master v{self.ni_700_current}.csv"
        self.ni_700_64_legacy_file_path = f"NI-700 Master v{self.legacy_ni} 64MB.csv"
        self.ni_700_32_legacy_file_path = f"NI-700 Master v{self.legacy_ni} 32MB.csv"

        self.ni_x100_current = ni_x100_current
        self.ni_x100_file_path = f"NI-x100 Master v{self.ni_x100_current}.csv"

        self.ni_x000_current = self.legacy_ni
        self.ni_x000_file_path = f"NI-x000 Master v{self.ni_x000_current}.csv"

        self.nx_current = nx_current
        self.nx_file_path = f"NX Master v{self.nx_current}.csv"
        self.nx_interim_file_path = f"NX Master v{self.interim_nx}.csv"

        self.file_list = [
            self.ni_700_file_path,
            self.ni_700_64_legacy_file_path,
            self.ni_700_32_legacy_file_path,
            self.nx_interim_file_path,
            self.nx_file_path,
            self.ni_x100_file_path,
            self.ni_x000_file_path,
            'master fw up to date.csv',
            'master fw skipped.csv'
            ]


    def _write_list_to_file(self, info, name):
        from os import mkdir
        path = self.firware_dir
        try: mkdir(path)
        except FileExistsError: pass

        with open(f"{path}{name}", 'w+') as f: f.writelines(info)
        return


    def _generate_lists(self):
        # create a list of False then track if anyone needs to create that file
        using_list = [False for _ in range(len(self.file_list))]
        # create a separate list for each file_name[] object
        update_info = [[] for _ in range(len(self.file_list))]

        for system in self.systems:
            for i in range(len(self.file_list)):
                if system['master_update_list'] == self.file_list[i]:
                    update_info[i].append(system['master_update_info'] + '\n')
                    using_list[i] = True

        for n, _info in enumerate(update_info):
            if using_list[n]: self._write_list_to_file(_info, self.file_list[n])
        return


    def _compare_versions(self, current_ver, update_ver, current_file_name, update_file_name):
        for i in range(len(update_ver)):
            if current_ver[i] > update_ver[i]:
                return current_file_name
            if current_ver[i] < update_ver[i]:
                return update_file_name
            elif current_ver[i] == update_ver[i]:
                continue
        return current_file_name  # matched all the way through


    def _version_to_int(self, version): return [int(x) for x in version.split('.')]


    def _check_ver(self):
        for system in self.systems:
            if 'master_serial' in system:
                current_ver = self._version_to_int(system['master_firmware'])
                current_file_name = 'master fw up to date.csv'
                update_file_name = ''  # protect from None errors
                update_ver = self._version_to_int('0.0.0')  # protect from None errors

                # newer NI-700 can run v4 FW
                if 'NI-700' in system['master_model'] and '210507' in system['master_serial']:
                    update_ver = self._version_to_int(self.ni_700_current)
                    update_file_name = self.ni_700_file_path
                    # now try again to see if it needs the interim ver
                    update_ver = self._version_to_int(self.legacy_ni)
                    update_file_name = self.ni_700_32_legacy_file_path

                # old generation NI-700 top out at 3.60.453
                elif 'NI-700' in system['master_model'] and '210503' in system['master_serial']:
                    update_ver = self._version_to_int(self.legacy_ni)
                    update_file_name = self.ni_700_64_legacy_file_path

                elif 'NX' in system['master_model'] and (
                    self._version_to_int(system['master_firmware'])[1] < self._version_to_int(self.interim_nx)[1]
                    ):
                    # _.x._ < _.4._
                    update_ver = self._version_to_int(self.interim_nx)
                    update_file_name = self.nx_interim_file_path

                elif 'NX' in system['master_model']:
                    update_ver = self._version_to_int(self.nx_current)
                    update_file_name = self.nx_file_path

                elif 'NI-2100' in system['master_model'] or 'NI-3100' in system['master_model'] or 'NI-4100' in system['master_model']:
                    update_ver = self._version_to_int(self.ni_x100_current)
                    update_file_name = self.ni_x100_file_path

                elif 'NI-20' in system['master_model']:
                    update_ver = self._version_to_int(self.ni_x000_current)
                    update_file_name = self.ni_x000_file_path
                    
                system['master_update_list'] = self._compare_versions(
                    current_ver, update_ver,
                    current_file_name, update_file_name
                    )

            else:
                system['master_update_list'] = 'master fw skipped.csv'
                warning(f"{system['full_name']} {system['master_model']} {system['master_update_list']}")

            system['master_update_info'] = f"{system['master_ip']},{system['full_name']} {system['master_model']},1319,1"

        return self.systems


    def run(self):
        self.systems = self._check_ver()
        self._generate_lists()
        return self.systems


class DeviceFirmware():

    def __init__(self, firmware_dir='firmware_lists/'):
        self.firware_dir = firmware_dir


    def set_systems(self, systems):
        self.systems = systems
        info(f"amxfirmware.py DeviceFirmware() added {len(self.systems)} systems")        


    def set_versions(self, ni_current='1.30.10', nx_current='1.1.48'):
        self.ni_current = ni_current
        self.ni_700_file_path = f"NI-700 Device v{self.ni_current}.csv"
        self.ni_x000_file_path = f"NI-x000 Device v{self.ni_current}.csv"
        self.ni_x100_file_path = f"NI-x100 Device v{self.ni_current}.csv"

        self.nx_current = nx_current
        self.nx_file_path = f"NX Device v{self.nx_current}.csv"

        self.file_list = [
            self.ni_700_file_path,
            self.ni_x000_file_path,
            self.ni_x100_file_path,
            self.nx_file_path,
            'device fw up to date',
            'device fw skipped.csv',
            ]


    def _write_list_to_file(self, info, name):
        from os import mkdir
        path = self.firware_dir
        try: mkdir(path)
        except FileExistsError: pass

        with open(f"{path}{name}", 'w+') as f: f.writelines(info)
        return


    def _generate_lists(self):
        using_list = [False for _ in range(len(self.file_list))]
        update_info = [[] for _ in range(len(self.file_list))]

        for system in self.systems:
            for i in range(len(self.file_list)):
                if system['device_update_list'] == self.file_list[i]:
                    update_info[i].append(system['device_update_info'] + '\n')
                    using_list[i] = True

        for n, _info in enumerate(update_info):
            if using_list[n]: self._write_list_to_file(_info, self.file_list[n])
        return


    def _compare_versions(self, current_ver, update_ver, current_file_name, update_file_name):
        for i in range(len(update_ver)):
            if current_ver[i] > update_ver[i]:
                return current_file_name
            if current_ver[i] < update_ver[i]:
                return update_file_name
            elif current_ver[i] == update_ver[i]:
                continue
        return current_file_name  # matched all the way through


    def _version_to_int(self, version): return [int(x) for x in version.split('.')]


    def _check_ver(self):
        for system in self.systems:
            if 'master_serial' in system:
                current_ver = self._version_to_int(system['device_firmware'])
                current_file_name = 'device fw up to date.csv'
                update_file_name = ''  # protect from None errors
                update_ver = self._version_to_int('0.0.0')  # protect from None errors
            
                if 'NI-700' in system['master_model']:
                    update_ver = self._version_to_int(self.ni_current)
                    update_file_name = self.ni_700_file_path

                elif 'NX' in system['master_model']:
                    update_ver = self._version_to_int(self.nx_current)
                    update_file_name = self.nx_file_path

                elif 'NI-2100' in system['master_model'] or 'NI-3100' in system['master_model'] or 'NI-4100' in system['master_model']:
                    update_ver = self._version_to_int(self.ni_current)
                    update_file_name = self.ni_x100_file_path

                elif 'NI-20' in system['master_model']:
                    update_ver = self._version_to_int(self.ni_current)
                    update_file_name = self.ni_x000_file_path
                    
                system['device_update_list'] = self._compare_versions(
                    current_ver, update_ver,
                    current_file_name, update_file_name
                    )

            else:
                system['device_update_list'] = 'device fw skipped.csv'
                warning(f"{system['full_name']} {system['master_model']} {system['device_update_list']}")

            system['device_update_info'] = f"{system['master_ip']},{system['full_name']} {system['master_model']},1319,1"

        return self.systems


    def run(self):
        self.systems = self._check_ver()
        self._generate_lists()
        return self.systems

