from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    email: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    phone_number: str | None = None
    sex: str | None = None
    birthdate: date | None = None
    country: str | None = None
    region: str | None = None
    city: str | None = None
    updated_at: datetime
    created_at: datetime
    is_active: bool
    is_deleted: bool


class BoxerProfile(BaseModel):
    first_name: str
    last_name: str
    sex: str
    birthday: date
    country: str
    region: str
    weight: float
    height: float
    athletic_distinction: str
    photo_name: str

    def to_dict(self):
        d = self.model_dump(exclude={'photo_name'})
        if self.birthday:
            d['birthday'] = self.birthday.isoformat()
        return d

class Boxer(BaseModel):
    first_name: str
    last_name: str
    country: str
    region: str
    weight: float
    birthday: date
    athletic_distinction: str
    photo_name: str

    def to_dict(self):
        d = self.model_dump(exclude={'photo_name'})
        if self.birthday:
            d['birthday'] = self.birthday.isoformat()
        return d
