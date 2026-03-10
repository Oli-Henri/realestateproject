from __future__ import annotations

from decimal import Decimal
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from app.models.listing import ListingFilters, ListingsResponse, PropertyType
from app.services.listing_service import ListingService


@pytest.fixture
def mock_service() -> MagicMock:
    return MagicMock(spec=ListingService)


@pytest.fixture
def client(mock_service: MagicMock) -> TestClient:
    app = create_app(listing_service=mock_service)
    return TestClient(app)


def make_response(**overrides) -> ListingsResponse:
    defaults = dict(listings=[], total=0, page=1, page_size=20)
    defaults.update(overrides)
    return ListingsResponse(**defaults)


class TestGetListings:
    def test_returns_200_with_no_filters(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        mock_service.search_listings.return_value = make_response()
        response = client.get("/api/v1/listings")
        assert response.status_code == 200

    def test_response_body_matches_schema(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        mock_service.search_listings.return_value = make_response(total=0, page=1, page_size=20)
        response = client.get("/api/v1/listings")
        body = response.json()
        assert "listings" in body
        assert "total" in body
        assert "page" in body
        assert "page_size" in body

    def test_passes_city_filter_to_service(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        mock_service.search_listings.return_value = make_response()
        client.get("/api/v1/listings?city=Montreal")
        called_filters: ListingFilters = mock_service.search_listings.call_args[0][0]
        assert called_filters.city == "Montreal"

    def test_passes_price_filters_to_service(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        mock_service.search_listings.return_value = make_response()
        client.get("/api/v1/listings?min_price=100000&max_price=500000")
        called_filters: ListingFilters = mock_service.search_listings.call_args[0][0]
        assert called_filters.min_price == Decimal("100000")
        assert called_filters.max_price == Decimal("500000")

    def test_passes_property_type_filter_to_service(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        mock_service.search_listings.return_value = make_response()
        client.get("/api/v1/listings?property_type=plex")
        called_filters: ListingFilters = mock_service.search_listings.call_args[0][0]
        assert called_filters.property_type == PropertyType.PLEX

    def test_passes_pagination_params_to_service(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        mock_service.search_listings.return_value = make_response(page=2, page_size=10)
        client.get("/api/v1/listings?page=2&page_size=10")
        called_filters: ListingFilters = mock_service.search_listings.call_args[0][0]
        assert called_filters.page == 2
        assert called_filters.page_size == 10

    def test_returns_422_for_invalid_page(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        response = client.get("/api/v1/listings?page=0")
        assert response.status_code == 422

    def test_returns_422_for_invalid_property_type(
        self, client: TestClient, mock_service: MagicMock
    ) -> None:
        response = client.get("/api/v1/listings?property_type=invalid")
        assert response.status_code == 422
