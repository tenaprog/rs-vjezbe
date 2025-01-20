from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, Field


class CCTVFrame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: Tuple[float, float] = Field(default=(0.0, 0.0))
