import { useState } from 'react';
import type { ListingFilters } from '../services/listings';
import { useListings } from '../hooks/useListings';
import { ListingCard } from '../components/ListingCard';

const DEFAULT_MAX_BUDGET = 250000;

export function ListingsPage() {
  const [filters, setFilters] = useState<ListingFilters>({
    property_type: 'residential_lot',
    max_price: DEFAULT_MAX_BUDGET,
    page: 1,
    page_size: 20,
  });
  const [draft, setDraft] = useState({ city: '', max_price: String(DEFAULT_MAX_BUDGET) });
  const { listings, total, loading, error } = useListings(filters);

  function handleSearch(e: React.FormEvent) {
    e.preventDefault();
    setFilters({
      property_type: 'residential_lot',
      city: draft.city || undefined,
      max_price: draft.max_price ? Number(draft.max_price) : undefined,
      page: 1,
      page_size: 20,
    });
  }

  function handleReset() {
    setDraft({ city: '', max_price: String(DEFAULT_MAX_BUDGET) });
    setFilters({
      property_type: 'residential_lot',
      max_price: DEFAULT_MAX_BUDGET,
      page: 1,
      page_size: 20,
    });
  }

  return (
    <div style={styles.page}>
      <h1 style={styles.title}>Quebec Residential Lots</h1>
      <p style={styles.subtitle}>Residential lots only — set your budget to filter results.</p>

      <form onSubmit={handleSearch} style={styles.form}>
        <input
          style={styles.input}
          placeholder="City (e.g. Montreal)"
          value={draft.city}
          onChange={e => setDraft(d => ({ ...d, city: e.target.value }))}
        />
        <div style={styles.budgetWrapper}>
          <label style={styles.label}>Max budget (CAD)</label>
          <input
            style={styles.input}
            type="number"
            placeholder="250000"
            value={draft.max_price}
            onChange={e => setDraft(d => ({ ...d, max_price: e.target.value }))}
          />
        </div>
        <button type="submit" style={styles.btnPrimary}>Search</button>
        <button type="button" style={styles.btnSecondary} onClick={handleReset}>Reset</button>
      </form>

      {loading && <p style={styles.status}>Loading...</p>}
      {error && <p style={{ ...styles.status, color: '#dc3545' }}>Error: {error}</p>}

      {!loading && !error && (
        <>
          <p style={styles.count}>{total} lot{total !== 1 ? 's' : ''} found</p>
          <div style={styles.grid}>
            {listings.map(listing => (
              <ListingCard key={listing.listing_id} listing={listing} />
            ))}
          </div>
          {listings.length === 0 && (
            <p style={styles.status}>No lots match your filters.</p>
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
    marginBottom: 6,
    color: '#1a1a2e',
  },
  subtitle: {
    fontSize: 14,
    color: '#6c757d',
    marginBottom: 24,
  },
  form: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: 10,
    alignItems: 'flex-end',
    marginBottom: 24,
  },
  budgetWrapper: {
    display: 'flex',
    flexDirection: 'column',
    gap: 4,
  },
  label: {
    fontSize: 12,
    color: '#6c757d',
    fontWeight: 500,
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
