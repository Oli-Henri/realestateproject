from __future__ import annotations

from decimal import Decimal
from unittest.mock import MagicMock

import pytest

from app.models.listing import Listing, ListingFilters, ListingsResponse, PropertyType
from app.services.listing_service import ListingService


def make_listing(**overrides) -> Listing:
    from datetime import datetime, timezone

    defaults = dict(
        listing_id="L001",
        address="123 Rue Saint-Denis",
        city="Montreal",
        price=Decimal("450000"),
        property_type=PropertyType.PLEX,
        bedrooms=6,
        bathrooms=3,
        sqft=2400,
        description="Triplex in Plateau.",
        listed_at=datetime(2026, 1, 10, tzinfo=timezone.utc),
    )
    defaults.update(overrides)
    return Listing(**defaults)


@pytest.fixture
def mock_repository() -> MagicMock:
    return MagicMock()


@pytest.fixture
def service(mock_repository: MagicMock) -> ListingService:
    return ListingService(repository=mock_repository)


class TestSearchListings:
    def test_returns_listings_response(
        self, service: ListingService, mock_repository: MagicMock
    ) -> None:
        mock_repository.get_listings.return_value = ([make_listing()], 1)
        result = service.search_listings(ListingFilters())
        assert isinstance(result, ListingsResponse)

    def test_delegates_to_repository_with_filters(
        self, service: ListingService, mock_repository: MagicMock
    ) -> None:
        filters = ListingFilters(city="Montreal")
        mock_repository.get_listings.return_value = ([], 0)
        service.search_listings(filters)
        mock_repository.get_listings.assert_called_once_with(filters)

    def test_response_contains_correct_listings(
        self, service: ListingService, mock_repository: MagicMock
    ) -> None:
        listing = make_listing(listing_id="L001")
        mock_repository.get_listings.return_value = ([listing], 1)
        result = service.search_listings(ListingFilters())
        assert result.listings == [listing]

    def test_response_reflects_total_from_repository(
        self, service: ListingService, mock_repository: MagicMock
    ) -> None:
        mock_repository.get_listings.return_value = ([make_listing()], 42)
        result = service.search_listings(ListingFilters(page=1, page_size=1))
        assert result.total == 42

    def test_response_reflects_pagination_params(
        self, service: ListingService, mock_repository: MagicMock
    ) -> None:
        mock_repository.get_listings.return_value = ([], 0)
        filters = ListingFilters(page=3, page_size=10)
        result = service.search_listings(filters)
        assert result.page == 3
        assert result.page_size == 10
