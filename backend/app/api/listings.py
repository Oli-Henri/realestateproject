from __future__ import annotations

from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Depends, Query

from app.models.listing import ListingFilters, ListingsResponse, PropertyType
from app.services.listing_service import ListingService

router = APIRouter(prefix="/api/v1/listings", tags=["listings"])


def build_filters(
    city: Optional[str] = Query(default=None),
    min_price: Optional[Decimal] = Query(default=None),
    max_price: Optional[Decimal] = Query(default=None),
    property_type: Optional[PropertyType] = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> ListingFilters:
    return ListingFilters(
        city=city,
        min_price=min_price,
        max_price=max_price,
        property_type=property_type,
        page=page,
        page_size=page_size,
    )


@router.get("", response_model=ListingsResponse)
def get_listings(
    filters: ListingFilters = Depends(build_filters),
    service: ListingService = Depends(),
) -> ListingsResponse:
    return service.search_listings(filters)
