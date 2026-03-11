from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

from app.models.listing import Listing, ListingFilters, PropertyType

STUB_LISTINGS: list[Listing] = [
    Listing(
        listing_id="L001",
        address="245 Route des Érables",
        city="Quebec City",
        price=Decimal("155000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.6,
        zoning="Residential",
        description="Wooded lot in Beauport, municipal water and sewer at street.",
        listed_at=datetime(2026, 1, 5, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L002",
        address="88 Rue des Pins",
        city="Laval",
        price=Decimal("189000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.35,
        zoning="Residential",
        description="Flat serviced lot in Sainte-Rose, close to école and parc.",
        listed_at=datetime(2026, 1, 9, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L003",
        address="12 Chemin du Lac",
        city="Gatineau",
        price=Decimal("210000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.8,
        zoning="Residential",
        description="Quiet cul-de-sac lot backing onto greenbelt, all services at lot line.",
        listed_at=datetime(2026, 1, 12, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L004",
        address="330 Rang de la Montagne",
        city="Sherbrooke",
        price=Decimal("98000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=1.1,
        zoning="Residential",
        description="Large lot with mountain views, septic and well required.",
        listed_at=datetime(2026, 1, 18, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L005",
        address="1450 Rang Saint-François",
        city="Montreal",
        price=Decimal("320000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.45,
        zoning="Residential",
        description="Corner lot in Rivière-des-Prairies, fully serviced, ready to build.",
        listed_at=datetime(2026, 1, 22, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L006",
        address="77 Avenue des Chênes",
        city="Longueuil",
        price=Decimal("245000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.3,
        zoning="Residential",
        description="Premium lot in Saint-Hubert, serviced, paved street, near highway.",
        listed_at=datetime(2026, 1, 28, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L007",
        address="500 Route de l'Église",
        city="Quebec City",
        price=Decimal("175000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.5,
        zoning="Residential",
        description="Serviced lot in Charlesbourg, mature trees on perimeter.",
        listed_at=datetime(2026, 2, 3, tzinfo=timezone.utc),
    ),
    Listing(
        listing_id="L008",
        address="19 Croissant des Érables",
        city="Laval",
        price=Decimal("390000"),
        property_type=PropertyType.RESIDENTIAL_LOT,
        lot_size_acres=0.4,
        zoning="Residential",
        description="Premium cul-de-sac lot in Vimont, all services, ready for permit.",
        listed_at=datetime(2026, 2, 8, tzinfo=timezone.utc),
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
