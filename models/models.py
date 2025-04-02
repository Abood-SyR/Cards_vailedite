from pydantic import BaseModel
class card(BaseModel):
    have_access: bool
    count: int

