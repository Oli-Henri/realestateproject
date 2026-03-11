import type { Listing } from '../services/listings';

const PROPERTY_LABEL: Record<string, string> = {
  residential_lot: 'Residential Lot',
  commercial_lot: 'Commercial Lot',
  agricultural: 'Agricultural',
  industrial: 'Industrial',
};

interface Props {
  listing: Listing;
}

export function ListingCard({ listing }: Props) {
  const formattedPrice = new Intl.NumberFormat('en-CA', {
    style: 'currency',
    currency: 'CAD',
    maximumFractionDigits: 0,
  }).format(listing.price);

  return (
    <div style={styles.card}>
      <div style={styles.header}>
        <span style={styles.type}>{PROPERTY_LABEL[listing.property_type]}</span>
        <span style={styles.price}>{formattedPrice}</span>
      </div>
      <div style={styles.address}>{listing.address}</div>
      <div style={styles.city}>{listing.city}</div>
      <div style={styles.specs}>
        <span>{listing.lot_size_acres} acres</span>
        <span>Zoning: {listing.zoning}</span>
      </div>
      <div style={styles.description}>{listing.description}</div>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  card: {
    border: '1px solid #e0e0e0',
    borderRadius: 8,
    padding: '16px 20px',
    background: '#fff',
    display: 'flex',
    flexDirection: 'column',
    gap: 6,
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  type: {
    fontSize: 12,
    fontWeight: 600,
    textTransform: 'uppercase',
    color: '#6c757d',
    letterSpacing: 1,
  },
  price: {
    fontSize: 20,
    fontWeight: 700,
    color: '#1a1a2e',
  },
  address: {
    fontSize: 16,
    fontWeight: 600,
  },
  city: {
    fontSize: 14,
    color: '#6c757d',
  },
  specs: {
    display: 'flex',
    gap: 16,
    fontSize: 14,
    color: '#495057',
  },
  description: {
    fontSize: 13,
    color: '#6c757d',
    marginTop: 4,
  },
};
