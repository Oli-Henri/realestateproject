import { useState } from 'react';
import type { ListingFilters, PropertyType } from '../services/listings';
import { useListings } from '../hooks/useListings';
import { ListingCard } from '../components/ListingCard';

const PROPERTY_TYPES: { value: PropertyType; label: string }[] = [
  { value: 'plex', label: 'Plex' },
  { value: 'single_family', label: 'Single Family' },
  { value: 'condo', label: 'Condo' },
  { value: 'commercial', label: 'Commercial' },
];

export function ListingsPage() {
  const [filters, setFilters] = useState<ListingFilters>({ page: 1, page_size: 20 });
  const [draft, setDraft] = useState({ city: '', min_price: '', max_price: '', property_type: '' });
  const { listings, total, loading, error } = useListings(filters);

  function handleSearch(e: React.FormEvent) {
    e.preventDefault();
    setFilters({
      city: draft.city || undefined,
      min_price: draft.min_price ? Number(draft.min_price) : undefined,
      max_price: draft.max_price ? Number(draft.max_price) : undefined,
      property_type: (draft.property_type as PropertyType) || undefined,
      page: 1,
      page_size: 20,
    });
  }

  function handleReset() {
    setDraft({ city: '', min_price: '', max_price: '', property_type: '' });
    setFilters({ page: 1, page_size: 20 });
  }

  return (
    <div style={styles.page}>
      <h1 style={styles.title}>Quebec Investment Properties</h1>

      <form onSubmit={handleSearch} style={styles.form}>
        <input
          style={styles.input}
          placeholder="City (e.g. Montreal)"
          value={draft.city}
          onChange={e => setDraft(d => ({ ...d, city: e.target.value }))}
        />
        <input
          style={styles.input}
          type="number"
          placeholder="Min price (CAD)"
          value={draft.min_price}
          onChange={e => setDraft(d => ({ ...d, min_price: e.target.value }))}
        />
        <input
          style={styles.input}
          type="number"
          placeholder="Max price (CAD)"
          value={draft.max_price}
          onChange={e => setDraft(d => ({ ...d, max_price: e.target.value }))}
        />
        <select
          style={styles.input}
          value={draft.property_type}
          onChange={e => setDraft(d => ({ ...d, property_type: e.target.value }))}
        >
          <option value="">All types</option>
          {PROPERTY_TYPES.map(pt => (
            <option key={pt.value} value={pt.value}>{pt.label}</option>
          ))}
        </select>
        <button type="submit" style={styles.btnPrimary}>Search</button>
        <button type="button" style={styles.btnSecondary} onClick={handleReset}>Reset</button>
      </form>

      {loading && <p style={styles.status}>Loading...</p>}
      {error && <p style={{ ...styles.status, color: '#dc3545' }}>Error: {error}</p>}

      {!loading && !error && (
        <>
          <p style={styles.count}>{total} listing{total !== 1 ? 's' : ''} found</p>
          <div style={styles.grid}>
            {listings.map(listing => (
              <ListingCard key={listing.listing_id} listing={listing} />
            ))}
          </div>
          {listings.length === 0 && (
            <p style={styles.status}>No listings match your filters.</p>
          )}
        </>
      )}
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  page: {
    maxWidth: 900,
    margin: '0 auto',
    padding: '32px 16px',
    fontFamily: 'system-ui, sans-serif',
  },
  title: {
    fontSize: 28,
    fontWeight: 700,
    marginBottom: 24,
    color: '#1a1a2e',
  },
  form: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: 10,
    marginBottom: 24,
  },
  input: {
    padding: '8px 12px',
    border: '1px solid #ced4da',
    borderRadius: 6,
    fontSize: 14,
    minWidth: 160,
  },
  btnPrimary: {
    padding: '8px 20px',
    background: '#1a1a2e',
    color: '#fff',
    border: 'none',
    borderRadius: 6,
    fontSize: 14,
    cursor: 'pointer',
  },
  btnSecondary: {
    padding: '8px 16px',
    background: 'transparent',
    color: '#6c757d',
    border: '1px solid #ced4da',
    borderRadius: 6,
    fontSize: 14,
    cursor: 'pointer',
  },
  count: {
    fontSize: 14,
    color: '#6c757d',
    marginBottom: 16,
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(380px, 1fr))',
    gap: 16,
  },
  status: {
    color: '#6c757d',
    fontSize: 14,
  },
};
