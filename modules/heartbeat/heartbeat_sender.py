"""
Heartbeat sending logic.
"""

from pymavlink import mavutil


# =================================================================================================
#                            ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
# =================================================================================================
class HeartbeatSender:
    """
    HeartbeatSender class to send a heartbeat
    """

    __private_key = object()

    @classmethod
    def create(
        cls,
        connection: mavutil.mavfile,
        args: tuple,
    ) -> "tuple[True, HeartbeatSender] | tuple[False, None]":
        """
        Falliable create (instantiation) method to create a HeartbeatSender object.
        """
        return True, cls(cls.__private_key, connection, args)

    def __init__(
        self,
        key: object,
        connection: mavutil.mavfile,
        _args: tuple,  # Unused in __init__
    ) -> None:
        assert key is HeartbeatSender.__private_key, "Use create() method"
        self._connection = connection

    def run(
        self,
        _args: tuple,  # Unused (signature for interface)
    ) -> None:
        """
        Attempt to send a heartbeat message.
        """
        self._connection.mav.heartbeat_send(
            mavutil.mavlink.MAV_TYPE_GCS,
            mavutil.mavlink.MAV_AUTOPILOT_INVALID,
            0,
            0,
            0,
        )


# =================================================================================================
#                            ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
# =================================================================================================
