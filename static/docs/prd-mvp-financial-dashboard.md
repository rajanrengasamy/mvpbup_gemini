# PRD: Financial Performance Dashboard MVP

## MVP Feature Name/Title
Optiver Global Financial Performance Dashboard

## Core Problem to Solve
Financial leaders at Optiver need a single, unified view to quickly track real-time P&L, monitor operational expenses, and identify underperforming business units across different countries and cost centers to enable faster data-driven decisions on resource allocation.

## MVP User Story
As a financial analyst or business leader at Optiver, I want to view aggregated financial metrics by country and drill down to profit center level, so that I can quickly identify profit/loss trends and make informed decisions about resource allocation without manual report generation.

## Core Functional Requirements (MVP Scope)

1. **Country-Level Financial Overview**
   - Display aggregated financial metrics for each country (AU, CN, SG, IN, TW, NL, GB, US)
   - Show key metrics: Net Trading Income, Other Income, Total Income, Operating Expense, Operating Margin, Non Operating Expense, Profit Before Tax, Tax, Profit After Tax, Capital, Return on Equity

2. **Time Period Filtering**
   - Enable filtering by time period: Daily, Weekly, Monthly
   - Default view: Current month-to-date
   - Allow comparison between current period and previous period

3. **Drill-Down Navigation**
   - Allow users to click on a country to view profit center breakdown
   - Display profit centers: D1, IXO, FICC, SSO
   - Show same financial metrics at profit center level

4. **Time Series Analysis**
   - Display monthly trend data for each financial metric
   - Show month-over-month (MoM) percentage changes
   - Visualize trends using sparkline charts or trend indicators
   - Highlight significant monthly changes (>10% deviation)
   - Enable viewing of October, November, December data from Q4 2024

5. **Data Display Requirements**
   - Present data in tabular format with clear column headers
   - Use consistent currency format (K for thousands)
   - Apply color coding: Green for positive trends, Red for negative trends
   - Include Grand Total row for all aggregations
   - Show monthly breakdown columns when time series view is enabled

6. **Basic Performance Indicators**
   - Calculate and display Return on Equity percentage for each entity
   - Show Operating Margin for quick profitability assessment

## Non-Goals (What's Explicitly Out of Scope)

1. **Advanced predictive analytics** - No forecasting or trend prediction algorithms
2. **User comments/annotations on data points** - No collaborative features
3. **Complex custom calculations** - Only pre-defined metrics listed above
4. **Integration with other data sources** - MVP uses only current financial data source
5. **Mobile app version** - Desktop web application only
6. **Real-time data refresh** - Daily batch updates are sufficient
7. **Customizable dashboard layouts** - Fixed layout for all users
8. **Export functionality** - No PDF/Excel export in MVP
9. **User access control** - Single access level for all users
10. **Historical data beyond 13 months** - Limited to current year + previous year
11. **Alerts and notifications** - No automated alerts for threshold breaches
12. **Multi-currency support** - All values in single currency (K)

## Lean UI/UX Considerations

1. **Navigation Structure**
   - Top-level view: Country overview table
   - Second-level view: Profit center breakdown (accessed via country click)
   - Breadcrumb navigation for easy return to country view

2. **Visual Design**
   - Clean, professional interface matching Optiver branding (dark blue header)
   - High contrast for readability
   - Minimal visual elements to reduce cognitive load

3. **Data Presentation**
   - Fixed-width columns for consistent scanning
   - Right-aligned numbers for easy comparison
   - Zebra striping for improved row tracking
   - Sticky headers when scrolling

4. **Interaction Patterns**
   - Single-click to drill down
   - Dropdown for time period selection
   - Toggle for time series/trend view

## MVP Success Metrics

1. **Adoption Rate**: At least 50% of target users (financial analysts and business leaders) access the dashboard at least 3 times per week within the first month

2. **Time Reduction**: 80% reduction in time spent generating manual financial reports (from average 2 hours to under 15 minutes)

## Open Questions

1. **Data Source**: What is the specific database/API endpoint for accessing the financial data?
2. **Authentication**: What authentication method should be used (SSO, LDAP, etc.)?
3. **Data Refresh Schedule**: What specific time should the daily data refresh occur?
4. **Browser Support**: What is the minimum browser version requirement?
5. **Performance Requirements**: What is the acceptable page load time for the dashboard?
6. **Error Handling**: How should the system behave when data is unavailable or incomplete?
7. **Audit Requirements**: Do we need to log user access and actions for compliance?