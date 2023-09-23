"""EX 2.6 protocol implementation
   Author:
   Date:
"""

LENGTH_FIELD_SIZE = 2
PORT = 8820


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    return data == "RAND" or data == "WHORU" or data == "TIME" or data == "EXIT"


def create_msg(data):
    """Create a valid protocol message, with length field"""
    sending_string = str(len(data)).zfill(LENGTH_FIELD_SIZE) + data
    return sending_string


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    length_field = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    if length_field.isdigit() is False:
        return False, "Error"
    msg_length = int(length_field)
    data = my_socket.recv(msg_length).decode()
    return True, data
