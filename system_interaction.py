import platform,notifypy,os
from strenum import StrEnum
# For Mac, try pync
icon_folder = "system_components/system_icon"
sound_file = "system_components/system_sound/notification_sound.wav"

class UrgencyType(StrEnum):
    LOW = "low",
    NORMAL = "NORMAL",
    CRITICAL = "CRITICAL"

class SystemIcon(StrEnum):
    SUCCESS = os.path.join(icon_folder,"success.png")
    ERROR = os.path.join(icon_folder, "error.png")
    INFORMATIVE = os.path.join(icon_folder, "informative.png")

class BaseInteraction():
    def __init__(self):
        # Get os info
        os_info = self.get_info_os()
        if os_info["name"] != "Linux":
            raise Exception("Currently only support Linux Operation")

    def get_info_os(self):
        return {
            "name": platform.system(),
            "release": platform.release(),
            "architecture": platform.processor(),
        }

class SystemNotification(BaseInteraction):
    def __init__(self,logging=False):
        super().__init__()
        self.logging = logging

    def send_notification(self,title="New Message",message=str,urgency=UrgencyType.NORMAL,icon=SystemIcon.INFORMATIVE,no_sound=False):
        # Setup infor
        notification = notifypy.Notify(enable_logging=self.logging)
        notification.application_name = "NotificationApp"
        notification.title = title
        notification.message = message
        notification.urgency = urgency   # 'low', 'normal' or 'critical'
        notification.icon = icon
        if no_sound == True: notification.audio = sound_file

        # Send notification
        notification.send(block=False)