import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename = "logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(con):
    
    vendor_sales_summary = pd.read_sql_query("""with FreightSummary as (
    select
        VendorNumber,
        sum(Freight) as FreightCost
    from vendor_invoice
    group by VendorNumber
    ),
    
    PurchaseSummary as (
        select
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.PurchasePrice, 
        p.Description,
        pp.Volume, 
        pp.Price as ActualPrice, 
        sum(p.Quantity) as TotalPurchaseQuantity, 
        sum(p.Dollars) as TotalPurchaseDollars
        from purchases p 
        join purchase_prices pp 
        on p.Brand = pp.Brand
        where p.PurchasePrice > 0
        group by p.VendorNumber, p.VendorName, p.Brand, p.PurchasePrice, p.Description, pp.Volume, pp.Price
    ),
    
    SalesSummary as (
        select
        VendorNo, 
        Brand, 
        sum(SalesDollars) as TotalSalesDollars, 
        sum(SalesPrice) as TotalSalesPrice, 
        sum(SalesQuantity) as TotalSalesQuantity,
        sum(ExciseTax) as TotalExciseTax 
        from sales 
        group by VendorNo, Brand 
    )
    
    select 
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    from PurchaseSummary ps
    left join SalesSummary ss
        on ps.VendorNumber = ss.VendorNo
        and ps.Brand = ss.Brand
    left join FreightSummary fs
        on ps.VendorNumber = fs.VendorNumber
    order by ps.TotalPurchaseDollars desc
    """, con)
    return vendor_sales_summary


def clean_data(df):
    df['Volume'] = df['Volume'].astype(float)
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()
    df.fillna(0, inplace=True)

    # Business Metrics
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    
    df['ProfitMargin'] = (
        df['GrossProfit'] / df['TotalSalesDollars']
    ).replace([float('inf'), -float('inf')], 0) * 100

    df['StockTurnover'] = (
        df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    ).replace([float('inf'), -float('inf')], 0)

    df['SalesPurchaseRatio'] = (
        df['TotalSalesDollars'] / df['TotalPurchaseDollars']
    ).replace([float('inf'), -float('inf')], 0)

    return df


if __name__ == '__main__':
    con = sqlite3.connect('inventory.db')

    logging.info("Creating vendor summary table......")
    summary_df = create_vendor_summary(con)
    logging.info(summary_df.head())

    logging.info("Cleaning data......")
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info("Ingestion data......")
    ingest_db(clean_df, 'vendor_sales_summary',con)
    logging.info("Completed")