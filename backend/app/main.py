from __future__ import annotations

from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Depends, FastAPI, Query

from app.models.listing import ListingFilters, ListingsResponse, PropertyType
from app.repositories.listing_repository import ListingRepository
from app.services.listing_service import ListingService


def _build_listing_router(listing_service: ListingService) -> APIRouter:
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
    def get_listings(filters: ListingFilters = Depends(build_filters)) -> ListingsResponse:
        return listing_service.search_listings(filters)

    return router


def create_app(listing_service: Optional[ListingService] = None) -> FastAPI:
    if listing_service is None:
        listing_service = ListingService(repository=ListingRepository())

    app = FastAPI(title="RealEstate Investment Assistant", version="0.1.0")
    app.include_router(_build_listing_router(listing_service))
    return app


app = create_app()
