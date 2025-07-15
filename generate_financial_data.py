import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define the Q4 2024 date range
start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 12, 31)

# Define sample data for various fields
transaction_types = ['Journal', 'VendBill', 'Payment', 'Invoice', 'CreditMemo']
subsidiaries = [
    ('Optiver Services BV', 'NL', 'EU', 'EUR'),
    ('Optiver Pty Limited', 'AU', None, 'AUD'),
    ('Optiver UK Limited', 'GB', None, 'GBP'),
    ('Optiver Services US LLC', 'US', None, 'USD'),
    ('Optiver FX Limited', 'GB', None, 'USD'),
    ('Optiver Trading Hong Kong Limited', 'HK', None, 'HKD'),
    ('Optiver Singapore Pte Ltd', 'SG', None, 'SGD'),
    ('Optiver Trading Taiwan Limited', 'TW', None, 'TWD'),
    ('Optiver Services India Private Limited', 'IN', None, 'INR'),
    ('Optiver Trading (Shanghai) Co., Ltd.', 'CN', None, 'CNY')
]

# Cost centers hierarchy
l1_cost_centres = [
    (1, 'Business Operations'),
    (302, 'Trading'),
    (303, 'Technology'),
    (304, 'Control'),
    (306, 'General'),
    (688, 'Business support')
]

l2_cost_centres = [
    (337, 'Legal', 688),
    (343, 'Finance', 688),
    (347, 'Risk', 304),
    (349, 'People', 1),
    (355, 'Other Business Operations', 1),
    (358, 'General', 306),
    (687, 'Other Business Support', 688),
    (1308, 'IXO', 302),
    (1406, 'Research Platform', 303),
    (1409, 'SSO', 302),
    (2000, 'Enterprise Technology', 303),
    (2100, 'Trading Infrastructure', 303)
]

l3_cost_centres = [
    (338, 'Legal', 337),
    (344, 'Finance', 343),
    (350, 'People', 349),
    (359, 'General', 358),
    (571, 'Other Business Operation', 355),
    (1203, 'Enterprise Technology', 2000),
    (1205, 'Trading Infrastructure', 2100),
    (1206, 'Research Infrastructure', 1406),
    (1210, 'People Advisory', 349),
    (1211, 'Control Change and Assurance', 687),
    (1212, 'Risk Management', 347),
    (1901, 'D1 Cash', 302),
    (576, 'SSO', 1409)
]

# Profit centers
profit_centres = [
    (102, 'Index Options', 1308, 'IXO'),
    (109, 'D1', None, 'D1'),
    (112, 'FICC', None, 'FICC'),
    (328, 'Single Stock Options', 1409, 'SSO'),
    (1710, 'Currencies', 112, 'FICC'),
    (2008, 'D1 Cash', 109, 'D1'),
    (2009, 'D1 High Frequency Trading', 109, 'D1'),
    (2010, 'D1 Medium Frequency Strategy', 109, 'D1')
]

# Account information
accounts = [
    (1327, '50111001', 'Gross salary', 'Personnel expenses', 'Wages', 'Wages staff'),
    (1330, '50111201', 'Severance and sign-off', 'Personnel expenses', 'Wages', 'Wages staff'),
    (1331, '50111202', 'Sign-on allowance < 250K MHNP', 'Personnel expenses', 'Wages', 'Wages staff'),
    (1334, '50111205', 'Temporary External Staff', 'Personnel expenses', 'Wages', 'Wages staff'),
    (1345, '50121001', 'Social security', 'Personnel expenses', 'Social security', 'Social security on wages'),
    (1348, '50131001', 'Pension expenses', 'Personnel expenses', 'Pensions', 'Pensions'),
    (1351, '50141001', 'Variable pay - as % of fixed pay NMH', 'Personnel expenses', 'Variable pay - as % of fixed pay', 'Variable pay - as % of fixed pay'),
    (1366, '50173001', 'Travel - Public transport', 'Personnel expenses', 'Other personnel expenses', 'Travel'),
    (1368, '50173003', 'Travel', 'Personnel expenses', 'Other personnel expenses', 'Travel'),
    (1371, '50173006', 'Travel - Accommodation', 'Personnel expenses', 'Other personnel expenses', 'Travel'),
    (1382, '50175002', 'Recruitment placements costs', 'Personnel expenses', 'Other personnel expenses', 'Recruitment'),
    (1386, '50175401', 'Interns', 'Personnel expenses', 'Other personnel expenses', 'Recruitment'),
    (1398, '50182001', 'Share rights', 'Personnel expenses', 'Profit rights / share rights', 'Share rights'),
    (1403, '50121002', 'Bonus – accrual', 'Personnel expenses', 'Social security', 'Social security on wages'),
    (1426, '50331004', 'Legal', 'General and administrative expenses', 'Consulting expenses', 'Consulting expenses'),
    (1429, '50331007', 'Finance', 'General and administrative expenses', 'Consulting expenses', 'Consulting expenses')
]

# Categories
categories = [
    (118, 'Pensions'),
    (139, 'Severance sign-off and other'),
    (189, 'Witheld travel - Other (WKR Final Tax)'),
    (1316, 'Travel - Airfare (Overseas)'),
    (1403, 'Bonus – accrual'),
    (2919, 'Intercompany Share Rights'),
    (9917, 'Workers Comp Insurance'),
    (12295, 'Temporary External Staff')
]

# Shared labels
shared_labels = [
    (5, 'Shared - All'),
    (8, 'Optiver Holding BV'),
    (11, 'Optiver Services BV')
]

# Spend keys
spend_keys = [
    (90, 'Shared - AMS Office'),
    (91, 'Shared - CHI Office'),
    (92, 'Shared - SYD Office'),
    (93, 'Shared - LON Office'),
    (94, 'Shared - HK Office'),
    (95, 'Shared - SG Office')
]

# Regions
regions = ['TA', 'APAC', 'EMEA', 'AMER']

# Exchange rates (approximations for Q4 2024)
exchange_rates = {
    'EUR': {'EUR': 1.0, 'AUD': 0.61, 'USD': 0.92, 'CNY': 0.13, 'INR': 0.011, 'GBP': 1.19, 'SGD': 0.68, 'TWD': 0.029},
    'AUD': {'EUR': 1.64, 'AUD': 1.0, 'USD': 1.51, 'CNY': 0.21, 'INR': 0.018, 'GBP': 1.95, 'SGD': 1.12, 'TWD': 0.048},
    'USD': {'EUR': 1.09, 'AUD': 0.66, 'USD': 1.0, 'CNY': 0.14, 'INR': 0.012, 'GBP': 1.29, 'SGD': 0.74, 'TWD': 0.032},
    'GBP': {'EUR': 0.84, 'AUD': 0.51, 'USD': 0.77, 'CNY': 0.11, 'INR': 0.009, 'GBP': 1.0, 'SGD': 0.57, 'TWD': 0.025},
    'HKD': {'EUR': 0.14, 'AUD': 0.085, 'USD': 0.13, 'CNY': 0.018, 'INR': 0.0015, 'GBP': 0.17, 'SGD': 0.095, 'TWD': 0.0041},
    'SGD': {'EUR': 1.47, 'AUD': 0.89, 'USD': 1.35, 'CNY': 0.19, 'INR': 0.016, 'GBP': 1.75, 'SGD': 1.0, 'TWD': 0.043},
    'TWD': {'EUR': 34.5, 'AUD': 20.8, 'USD': 31.5, 'CNY': 4.4, 'INR': 0.38, 'GBP': 41.0, 'SGD': 23.4, 'TWD': 1.0},
    'INR': {'EUR': 91.2, 'AUD': 55.1, 'USD': 83.5, 'CNY': 11.6, 'INR': 1.0, 'GBP': 108.4, 'SGD': 61.9, 'TWD': 2.65},
    'CNY': {'EUR': 7.85, 'AUD': 4.74, 'USD': 7.18, 'CNY': 1.0, 'INR': 0.086, 'GBP': 9.33, 'SGD': 5.33, 'TWD': 0.23}
}

def generate_financial_data(num_rows=10000):
    data = []
    
    # Generate transaction IDs
    transaction_id_start = 8000000
    
    for i in range(num_rows):
        # Basic transaction info
        transaction_id = transaction_id_start + random.randint(1, 100000)
        transaction_line_id = random.randint(1, 500)
        transaction_type = random.choice(transaction_types)
        
        # Generate date within Q4 2024
        days_offset = random.randint(0, (end_date - start_date).days)
        transaction_date = start_date + timedelta(days=days_offset)
        
        # Determine accounting period based on transaction date
        if transaction_date.month == 10:
            accounting_period_id = 291
            period_name = 'Oct-24'
            period_start = '2024-10-01'
            period_end = '2024-10-31'
        elif transaction_date.month == 11:
            accounting_period_id = 292
            period_name = 'Nov-24'
            period_start = '2024-11-01'
            period_end = '2024-11-30'
        else:
            accounting_period_id = 293
            period_name = 'Dec-24'
            period_start = '2024-12-01'
            period_end = '2024-12-31'
        
        period_parent = 'Q4 2024'
        
        # Select subsidiary
        subsidiary = random.choice(subsidiaries)
        subsidiary_name, country, suffix, currency = subsidiary
        subsidiary_id = random.randint(80, 160)
        
        # Select cost centres
        l3_cc = random.choice(l3_cost_centres)
        l3_cost_centre_id, l3_cost_centre_name, l2_parent_id = l3_cc
        
        # Find matching L2
        l2_cc = next((cc for cc in l2_cost_centres if cc[0] == l2_parent_id), l2_cost_centres[0])
        l2_cost_centre_id, l2_cost_centre_name, l1_parent_id = l2_cc
        
        # Find matching L1
        l1_cc = next((cc for cc in l1_cost_centres if cc[0] == l1_parent_id), l1_cost_centres[0])
        l1_cost_centre_id, l1_cost_centre_name = l1_cc
        
        # Select profit centres
        pc = random.choice(profit_centres)
        l3_profit_centre_id = pc[0] if random.random() > 0.3 else None
        l3_profit_centre_name = pc[3] if l3_profit_centre_id else None
        l2_profit_centre_id = pc[0]
        l2_profit_centre_name = pc[1]
        l1_profit_centre_id = pc[2] if pc[2] else 109
        l1_profit_centre_name = pc[3] if pc[3] else 'D1'
        
        # Select category
        category = random.choice(categories) if random.random() > 0.3 else (None, None)
        category_id, category_name = category if category else (None, None)
        
        # Select shared label and spend key
        shared_label = random.choice(shared_labels) if random.random() > 0.5 else (None, None)
        shared_label_id, shared_label_name = shared_label if shared_label else (None, None)
        
        spend_key = random.choice(spend_keys) if random.random() > 0.5 else (None, None)
        spend_key_id, spend_key_name = spend_key if spend_key else (None, None)
        
        # APAC tax status
        apac_tax_status_id = None
        apac_tax_status_name = None
        
        # Select account
        account = random.choice(accounts)
        account_id, account_number, account_l4_name, account_l1_name, account_l2_name, account_l3_name = account
        
        # Rules and allocations
        rules = ['Timesheet', 'Marble', 'Direct', 'Allocation']
        rule = random.choice(rules)
        
        # Account types
        account_type_id = 'Expense'
        is_income_statement = True
        is_balance_sheet = False
        accounting_period_is_closed = True
        
        # Generate amounts
        base_amount = random.uniform(-50000, 50000)
        amount = round(base_amount, 2)
        
        # Calculate amounts in different currencies
        local_rate = exchange_rates.get(currency, exchange_rates['USD'])
        amount_eur = round(amount * local_rate['EUR'], 2)
        amount_aud = round(amount * local_rate['AUD'], 2)
        amount_usd = round(amount * local_rate['USD'], 2)
        amount_cny = round(amount * local_rate['CNY'], 2)
        amount_inr = round(amount * local_rate['INR'], 2)
        amount_gbp = round(amount * local_rate['GBP'], 2)
        amount_sgd = round(amount * local_rate['SGD'], 2)
        amount_twd = round(amount * local_rate['TWD'], 2)
        
        # Exchange rates
        exchange_rate_local_eur = local_rate['EUR']
        exchange_rate_aud_eur = 0.61
        exchange_rate_usd_eur = 0.92
        exchange_rate_cny_eur = 0.13
        exchange_rate_inr_eur = 0.011
        exchange_rate_gbp_eur = 1.19
        exchange_rate_sgd_eur = 0.68
        exchange_rate_twd_eur = 0.029
        
        # Regions and allocation
        from_region = random.choice(regions)
        to_region = random.choice(regions)
        allocation_country = country
        
        # Keys and IDs
        key_id = f"{rule.upper()}{accounting_period_id}{country}{suffix or ''}{l3_cost_centre_id}"
        allocation_id = f"{country}{l2_profit_centre_id}"
        
        # Comment
        comment = f'"{rule}" transaction line allocated using "{rule}" allocation key.'
        
        # Employee and FTE data
        employee_id = None
        allocation = None
        timesheet_profit_centre = None
        fte = None
        fte_allocation = None
        marbles = None
        marble_allocation = None
        
        # Capital flag
        is_capital = False if random.random() > 0.05 else True
        
        # NSPB names
        nspb_l2_name = 'Operating expenses'
        nspb_l3_name = account_l2_name
        nspb_l4_name = account_l3_name if random.random() > 0.3 else None
        
        # Create row
        row = {
            'transaction_id': transaction_id,
            'transaction_line_id': transaction_line_id,
            'transaction_type': transaction_type,
            'transaction_date': transaction_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'accounting_period_id': accounting_period_id,
            'accounting_period_start_date': period_start,
            'accounting_period_end_date': period_end,
            'accounting_period_name': period_name,
            'accounting_period_parent_name': period_parent,
            'l3_profit_centre_id': l3_profit_centre_id,
            'l3_profit_centre_name': l3_profit_centre_name,
            'subsidiary_id': subsidiary_id,
            'subsidiary_name': subsidiary_name,
            'subsidiary_country': country,
            'subsidiary_suffix': suffix,
            'currency_symbol': currency,
            'l3_cost_centre_id': l3_cost_centre_id,
            'l3_cost_centre_name': l3_cost_centre_name,
            'l2_cost_centre_id': l2_cost_centre_id,
            'l2_cost_centre_name': l2_cost_centre_name,
            'l1_cost_centre_id': l1_cost_centre_id,
            'l1_cost_centre_name': l1_cost_centre_name,
            'category_id': category_id,
            'category_name': category_name,
            'shared_label_id': shared_label_id,
            'shared_label_name': shared_label_name,
            'spend_key_id': spend_key_id,
            'spend_key_name': spend_key_name,
            'apac_tax_status_id': apac_tax_status_id,
            'apac_tax_status_name': apac_tax_status_name,
            'account_id': account_id,
            'account_number': account_number,
            'rule': rule,
            'account_l1_name': account_l1_name,
            'account_l2_name': account_l2_name,
            'account_l3_name': account_l3_name,
            'account_l4_name': account_l4_name,
            'nspb_l2_name': nspb_l2_name,
            'nspb_l3_name': nspb_l3_name,
            'nspb_l4_name': nspb_l4_name,
            'account_type_id': account_type_id,
            'is_income_statement': is_income_statement,
            'is_balance_sheet': is_balance_sheet,
            'accounting_period_is_closed': accounting_period_is_closed,
            'amount': amount,
            'l2_profit_centre_id': l2_profit_centre_id,
            'l2_profit_centre_name': l2_profit_centre_name,
            'l1_profit_centre_id': l1_profit_centre_id,
            'l1_profit_centre_name': l1_profit_centre_name,
            'allocation_country': allocation_country,
            'key_id': key_id,
            'allocation_id': allocation_id,
            'comment': comment,
            'amount_eur': amount_eur,
            'amount_aud': amount_aud,
            'amount_usd': amount_usd,
            'amount_cny': amount_cny,
            'amount_inr': amount_inr,
            'amount_gbp': amount_gbp,
            'amount_sgd': amount_sgd,
            'amount_twd': amount_twd,
            'exchange_rate_local_eur': exchange_rate_local_eur,
            'exchange_rate_aud_eur': exchange_rate_aud_eur,
            'exchange_rate_usd_eur': exchange_rate_usd_eur,
            'exchange_rate_cny_eur': exchange_rate_cny_eur,
            'exchange_rate_inr_eur': exchange_rate_inr_eur,
            'exchange_rate_gbp_eur': exchange_rate_gbp_eur,
            'exchange_rate_sgd_eur': exchange_rate_sgd_eur,
            'exchange_rate_twd_eur': exchange_rate_twd_eur,
            'from_region': from_region,
            'to_region': to_region,
            'employee_id': employee_id,
            'allocation': allocation,
            'timesheet_profit_centre': timesheet_profit_centre,
            'fte': fte,
            'fte_allocation': fte_allocation,
            'marbles': marbles,
            'marble_allocation': marble_allocation,
            'is_capital': is_capital
        }
        
        data.append(row)
    
    return pd.DataFrame(data)

# Generate the data
print("Generating financial data...")
df = generate_financial_data(200000)

# Save to CSV
output_path = '/Users/rajan/Library/Mobile Documents/com~apple~CloudDocs/repo/svelte-tailwind4-starter/static/data/q4_2024_financial_data_200k.csv'
df.to_csv(output_path, index=False)

print(f"Successfully generated {len(df)} rows of financial data")
print(f"Data saved to: {output_path}")
print(f"\nData summary:")
print(f"- Date range: Q4 2024 (Oct, Nov, Dec)")
print(f"- Unique transaction IDs: {df['transaction_id'].nunique()}")
print(f"- Transaction types: {df['transaction_type'].value_counts().to_dict()}")
print(f"- Subsidiaries: {df['subsidiary_name'].nunique()}")
print(f"- Total amount (EUR): {df['amount_eur'].sum():,.2f}")