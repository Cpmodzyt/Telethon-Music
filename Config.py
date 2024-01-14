import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25812247"))
    API_HASH = os.environ.get("API_HASH", "00a50dc03d5b63a0eabfca83fa02c4ca")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6771845775:AAGCpeoqDXh-b56IPKjDhh_m90gPqftD1k0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCU7IDPsFxE0kvPPVhAQU-j0CmTnxe8Zv4nZrM1UK3DOir-22wKIs0d6BnFZEo6TmcBC6Mlb9vavO_ErrO6eof1YVHNVjk6dms3SqIFQ4GTMqM4ooO5hIlVwN6nJsXGQ2d5Ndx8nS_jusLUJAexH7Oke2EP-GrOii3zQI7asaMwHHyUIpNPDMk_p3xMe3dHOAvbvOFw1FbfBZP3YIOxT02fyryDjA_fbiQXd9LYoX-rU5wT9T_lhAqzosDvpCn-bJFylIfOWNhv_1kcaFEoCHjvff6kbkAlbv-rnubwuMDA0hS3zZqTm9xrmPcbiUU2Ui_87iq9fTvF2Sh9iHAZV8PmAAAAAYqPAugA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musiccpbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6619595496")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
