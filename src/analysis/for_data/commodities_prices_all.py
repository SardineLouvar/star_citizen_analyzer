import matplotlib.pyplot as plt

from src.db.db_manager import cur
from src.analysis.plotting import plot_bar_chart, prep_data

if __name__ == "__main__":
    res = cur.execute("""SELECT DISTINCT AVG(price_sell_avg) AS price_sell, commodity_name 
from commodities_prices_all
WHERE price_sell_avg > 0
GROUP BY commodity_name
ORDER BY price_sell asc;
                      """)
    
    x,y = prep_data(res)
    plot_bar_chart(x, y, "Value", "Commodity", "Average price of commodities", True)
