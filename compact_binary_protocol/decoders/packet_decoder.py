class PacketDecoder:
    """Utility class for decoding compact-binary packets."""

    @staticmethod
    def parse_response_data(data_str):
        """
        Parse the response data string and extract the 4th parameter.
        Example input: "1,4,0,\"01410001\",\"52.59.84.1\",10104"
        Returns the 4th parameter (e.g., "01410001") or None if not found.
        """
        try:
            parts = []
            current_part = ""
            in_quotes = False
            for char in data_str:
                if char == '"':
                    in_quotes = not in_quotes
                    current_part += char
                elif char == ',' and not in_quotes:
                    parts.append(current_part)
                    current_part = ""
                else:
                    current_part += char
            if current_part:
                parts.append(current_part)
            if len(parts) >= 4:
                fourth_param = parts[3].strip('"')
                return fourth_param
            return None
        except Exception:
            return None

    @staticmethod
    def decode_packet_header(hex_str):
        """
        Decode the packet header from a hex string.
        Header format: <ver><cmd1><cmd2><txnId><imei(8 bytes)>
        Returns tuple: (version, command, transaction_id, remainder_bytes) or (None, None, None) on error.
        """
        try:
            data = bytes.fromhex(hex_str)
            version = data[0] if len(data) > 0 else None
            if len(data) > 2:
                cmd1 = chr(data[1])
                cmd2 = chr(data[2])
                command = cmd1 + cmd2
            else:
                command = None
            txn_id = int.from_bytes(data[3:5], byteorder='big') if len(data) > 4 else None
            remainder = data[5:]
            return (version, command, txn_id, remainder)
        except Exception:
            return (None, None, None)
