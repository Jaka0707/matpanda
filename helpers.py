def add_revenue(df):
    """Adds 'revenue' column: units * price."""
    df['revenue'] = df['units'] * df['price']
    return df