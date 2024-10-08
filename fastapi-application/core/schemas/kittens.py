from pydantic import BaseModel, ConfigDict


class KittenBase(BaseModel):
    name: str
    color: str
    age: int
    description: str | None = None
    breed_id: int


class KittenCreate(KittenBase):
    pass


class KittenUpdate(KittenBase):
    pass


class KittenRead(KittenBase):
    model_config: ConfigDict = ConfigDict(from_attributes=True)
    id: int
