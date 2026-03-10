from __future__ import annotations

from app.models.listing import ListingFilters, ListingsResponse
from app.repositories.listing_repository import ListingRepository


class ListingService:
    def __init__(self, repository: ListingRepository) -> None:
        self._repository = repository

    def search_listings(self, filters: ListingFilters) -> ListingsResponse:
        listings, total = self._repository.get_listings(filters)
        return ListingsResponse(
            listings=listings,
            total=total,
            page=filters.page,
            page_size=filters.page_size,
        )
