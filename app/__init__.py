from dotenv import load_dotenv
from app.services.main import Main

load_dotenv()

app = Main()