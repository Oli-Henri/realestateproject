from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

from app.models.listing import Listing, ListingFilters, PropertyType

STUB_LISTINGS: list[Listing] = [
    Listing(
        listing_id="L001",
        address="1450 Rang Saint-François",
        city="Montreal",
        price=Decimal("320000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.45,
        zoning="Residential",
        description="Corner lot in Rivière-des-Prairies, fully serviced, ready to build.",
        listed_at=datetime(2026, 1, 10, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L002",
        address="890 Boulevard Industriel",
        city="Montreal",
        price=Decimal("780000"),
        property_type=PropertyType.INDUSTRIAL,
        lot_size_acres=2.1,
        zoning="Industrial",
        description="Flat industrial lot near Port of Montreal, rail access available.",
        listed_at=datetime(2026, 1, 15, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L003",
        address="245 Route des Érables",
        city="Quebec City",
        price=Decimal("155000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.6,
        zoning="Residential",
        description="Wooded lot in Beauport, municipal water and sewer on street.",
        listed_at=datetime(2026, 1, 20, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L004",
        address="1200 Chemin de la Rivière",
        city="Laval",
        price=Decimal("1250000"),
        property_type=PropertyType.AGRICULTURAL,
        lot_size_acres=48.0,
        zoning="Agricultural",
        description="Prime agricultural land with river frontage, drainage in place.",
        listed_at=datetime(2026, 1, 22, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L005",
        address="300 Avenue du Commerce",
        city="Laval",
        price=Decimal("540000"),
        property_type=PropertyType.COMMERCIAL_LOT,
        lot_size_acres=1.2,
        zoning="Commercial",
        description="High-visibility commercial lot on major artery, zoned C2.",
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
