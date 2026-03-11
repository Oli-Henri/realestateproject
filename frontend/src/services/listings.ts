const API_BASE = 'http://127.0.0.1:8000/api/v1';

export type PropertyType = 'residential_lot' | 'commercial_lot' | 'agricultural' | 'industrial';

export interface Listing {
  listing_id: string;
  address: string;
  city: string;
  price: number;
  property_type: PropertyType;
  lot_size_acres: number;
  zoning: string;
  description: string;
  listed_at: string;
}

export interface ListingsResponse {
  listings: Listing[];
  total: number;
  page: number;
  page_size: number;
}

export interface ListingFilters {
  city?: string;
  min_price?: number;
  max_price?: number;
  property_type?: PropertyType;
  page?: number;
  page_size?: number;
}

export async function fetchListings(filters: ListingFilters): Promise<ListingsResponse> {
  const params = new URLSearchParams();
  if (filters.city) params.set('city', filters.city);
  if (filters.min_price != null) params.set('min_price', String(filters.min_price));
  if (filters.max_price != null) params.set('max_price', String(filters.max_price));
  if (filters.property_type) params.set('property_type', filters.property_type);
  if (filters.page != null) params.set('page', String(filters.page));
  if (filters.page_size != null) params.set('page_size', String(filters.page_size));

  const response = await fetch(`${API_BASE}/listings?${params}`);
  if (!response.ok) throw new Error(`Failed to fetch listings: ${response.status}`);
  return response.json();
}
