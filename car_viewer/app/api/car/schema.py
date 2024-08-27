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
