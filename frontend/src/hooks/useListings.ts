import { useState, useEffect, useCallback } from 'react';
import { fetchListings } from '../services/listings';
import type { Listing, ListingFilters } from '../services/listings';

interface UseListingsState {
  listings: Listing[];
  total: number;
  loading: boolean;
  error: string | null;
}

export function useListings(filters: ListingFilters): UseListingsState {
  const [listings, setListings] = useState<Listing[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchListings(filters);
      setListings(data.listings);
      setTotal(data.total);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  }, [JSON.stringify(filters)]);

  useEffect(() => { load(); }, [load]);

  return { listings, total, loading, error };
}
