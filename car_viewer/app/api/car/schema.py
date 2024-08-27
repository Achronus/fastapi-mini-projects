from enum import Enum
from pydantic import BaseModel, ConfigDict, Field


class CountryCodes(Enum):
    AN = "AN"
    AF = "AF"
    AS = "AS"
    EU = "EU"
    NA = "NA"
    OC = "OC"
    SA = "SA"


class Car(BaseModel):
    """Car schema."""

    make: str = Field(..., description="Car make.")
    model: str = Field(..., description="Car model.")
    year: int = Field(..., ge=1970, description="Year the car was made.")
    price: float
    engine: str | None = "V4"
    autonomous: bool
    sold: list[CountryCodes]

    model_config = ConfigDict(use_enum_values=True)


class CarUpdate(BaseModel):
    make: str = Field(None, description="Car make.")
    model: str = Field(None, description="Car model.")
    year: int = Field(None, ge=1970, description="Year the car was made.")
    price: float = Field(None, description="Car price.")
    engine: str = Field("V4", description="Car engine.")
    autonomous: bool = Field(None, description="Car autonomous.")
    sold: list[CountryCodes] = Field(None, description="Car sold countries.")
