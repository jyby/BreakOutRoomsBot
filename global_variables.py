import os
import dotenv

dotenv.load_dotenv()
# GUILD = os.getenv('DISCORD_GUILD')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
PROFESSOR_ROLE_NAME = os.getenv('PROFESSOR_ROLE_NAME')
HEAD_TA_ROLE_NAME = os.getenv('AUXILIAR_ROLE_NAME')
TA_ROLE_NAME = os.getenv('ASSISTANT_ROLE_NAME')
STUDENT_ROLE_NAME = os.getenv('STUDENT_ROLE_NAME')
GENERAL_CHANNEL_NAME = os.getenv('GENERAL_CHANNEL_NAME')
MAX_STUDENTS_PER_GROUP = 3
TT_ROLES = [PROFESSOR_ROLE_NAME, HEAD_TA_ROLE_NAME, TA_ROLE_NAME]