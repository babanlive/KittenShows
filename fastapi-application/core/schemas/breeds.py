from pydantic import BaseModel, ConfigDict


class BreedBase(BaseModel):
    name: str


class BreedCreate(BreedBase):
    pass


class BreedUpdate(BreedBase):
    pass


class BreedRead(BreedBase):
    model_config: ConfigDict = ConfigDict(from_attributes=True)
    id: int
