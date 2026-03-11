from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class PropertyType(str, Enum):
    RESIDENTIAL_LOT = "residential_lot"
    COMMERCIAL_LOT = "commercial_lot"
    AGRICULTURAL = "agricultural"
    INDUSTRIAL = "industrial"


class Listing(BaseModel):
    listing_id: str
    address: str
    city: str
    price: Decimal
    property_type: PropertyType
    lot_size_acres: float
    zoning: str
    description: str
    listed_at: datetime


class ListingFilters(BaseModel):
    city: Optional[str] = None
    min_price: Optional[Decimal] = None
    max_price: Optional[Decimal] = None
    property_type: Optional[PropertyType] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)


class ListingsResponse(BaseModel):
    listings: list[Listing]
    total: int
    page: int
    page_size: int
