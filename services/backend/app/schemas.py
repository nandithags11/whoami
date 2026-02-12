#schema
from pydantic import BaseModel

class UserProfile(BaseModel):
    name : str
    user_id :str