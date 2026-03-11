from __future__ import annotations

from decimal import Decimal

import pytest

from app.models.listing import ListingFilters, PropertyType
from app.repositories.listing_repository import ListingRepository


@pytest.fixture
def repository() -> ListingRepository:
    return ListingRepository()


class TestGetListings:
    def test_returns_all_listings_when_no_filters(self, repository: ListingRepository) -> None:
        listings, total = repository.get_listings(ListingFilters())
        assert len(listings) > 0
        assert total == len(listings)

    def test_filters_by_city(self, repository: ListingRepository) -> None:
        filters = ListingFilters(city="Montreal")
        listings, total = repository.get_listings(filters)
        assert all(listing.city == "Montreal" for listing in listings)
        assert total == len(listings)

    def test_filters_by_min_price(self, repository: ListingRepository) -> None:
        min_price = Decimal("300000")
        filters = ListingFilters(min_price=min_price)
        listings, _ = repository.get_listings(filters)
        assert all(listing.price >= min_price for listing in listings)

    def test_filters_by_max_price(self, repository: ListingRepository) -> None:
        max_price = Decimal("400000")
        filters = ListingFilters(max_price=max_price)
        listings, _ = repository.get_listings(filters)
        assert all(listing.price <= max_price for listing in listings)

    def test_filters_by_property_type(self, repository: ListingRepository) -> None:
        filters = ListingFilters(property_type=PropertyType.RESIDENTIAL_LOT)
        listings, _ = repository.get_listings(filters)
        assert all(listing.property_type == PropertyType.RESIDENTIAL_LOT for listing in listings)

    def test_paginates_results(self, repository: ListingRepository) -> None:
        page1_filters = ListingFilters(page=1, page_size=2)
        page2_filters = ListingFilters(page=2, page_size=2)
        page1_listings, _ = repository.get_listings(page1_filters)
        page2_listings, _ = repository.get_listings(page2_filters)
        assert len(page1_listings) == 2
        page1_ids = {listing.listing_id for listing in page1_listings}
        page2_ids = {listing.listing_id for listing in page2_listings}
        assert page1_ids.isdisjoint(page2_ids)

    def test_total_reflects_filtered_count_not_page_count(self, repository: ListingRepository) -> None:
        filters = ListingFilters(city="Montreal", page=1, page_size=1)
        listings, total = repository.get_listings(filters)
        assert len(listings) == 1
        assert total > 1

    def test_returns_empty_list_for_unknown_city(self, repository: ListingRepository) -> None:
        filters = ListingFilters(city="UnknownCity")
        listings, total = repository.get_listings(filters)
        assert listings == []
        assert total == 0
