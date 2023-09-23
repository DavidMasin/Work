#   Ex. 2.7 template - protocol


LENGTH_FIELD_SIZE = 4
PORT = 8820


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """
    if ("DELETE" in data and len(data) > 8) or ("TAKE_SCREENSHOT" == data) or ("DIR" in data) or ("COPY" in data and len(data) > 5) or ("EXECUTE" in data and len(data) > 8) or ("EXIT" == data) or ("SEND_PHOTO" == data):
        # (3)
        return True
    return False


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    sending_string = str(len(str(data))).zfill(LENGTH_FIELD_SIZE) + str(data)

    # (4)
    return sending_string.encode()


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    length_field = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    print(length_field)
    if length_field.isdigit() is False:
        return False, "Error"
    msg_length = int(length_field)
    data = my_socket.recv(msg_length).decode()
    # (5)
    return True, data
