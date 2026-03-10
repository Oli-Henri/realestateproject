from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from app.models.listing import Listing, ListingFilters, PropertyType

STUB_LISTINGS: list[Listing] = [
    Listing(
        listing_id="L001",
        address="123 Rue Saint-Denis",
        city="Montreal",
        price=Decimal("450000"),
        property_type=PropertyType.PLEX,
        bedrooms=6,
        bathrooms=3,
        sqft=2400,
        description="Triplex in Plateau-Mont-Royal, fully rented.",
        listed_at=datetime(2026, 1, 10, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L002",
        address="45 Avenue du Parc",
        city="Montreal",
        price=Decimal("320000"),
        property_type=PropertyType.PLEX,
        bedrooms=4,
        bathrooms=2,
        sqft=1800,
        description="Duplex near Parc Lafontaine, needs renovation.",
        listed_at=datetime(2026, 1, 15, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L003",
        address="78 Rue des Érables",
        city="Quebec City",
        price=Decimal("275000"),
        property_type=PropertyType.SINGLE_FAMILY,
        bedrooms=3,
        bathrooms=1,
        sqft=1200,
        description="Bungalow in Sainte-Foy, good bones.",
        listed_at=datetime(2026, 1, 20, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L004",
        address="200 Boulevard Laurier",
        city="Quebec City",
        price=Decimal("380000"),
        property_type=PropertyType.CONDO,
        bedrooms=2,
        bathrooms=1,
        sqft=900,
        description="Modern condo in Sainte-Foy, low fees.",
        listed_at=datetime(2026, 1, 22, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L005",
        address="10 Rue Principale",
        city="Montreal",
        price=Decimal("550000"),
        property_type=PropertyType.COMMERCIAL,
        bedrooms=0,
        bathrooms=2,
        sqft=3000,
        description="Mixed-use commercial building, Rosemont.",
        listed_at=datetime(2026, 2, 1, tzinfo=timezone.utc),
    ),
]


class ListingRepository:
    def get_listings(self, filters: ListingFilters) -> tuple[list[Listing], int]:
        results = self._apply_filters(STUB_LISTINGS, filters)
        total = len(results)
        paginated = self._paginate(results, filters.page, filters.page_size)
        return paginated, total

    def _apply_filters(
        self, listings: list[Listing], filters: ListingFilters
    ) -> list[Listing]:
        results = listings
        if filters.city is not None:
            results = [l for l in results if l.city == filters.city]
        if filters.min_price is not None:
            results = [l for l in results if l.price >= filters.min_price]
        if filters.max_price is not None:
            results = [l for l in results if l.price <= filters.max_price]
        if filters.property_type is not None:
            results = [l for l in results if l.property_type == filters.property_type]
        return results

    def _paginate(
        self, listings: list[Listing], page: int, page_size: int
    ) -> list[Listing]:
        start = (page - 1) * page_size
        end = start + page_size
        return listings[start:end]
