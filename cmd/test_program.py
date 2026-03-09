from pathlib import Path

from src.config_loader import load_config
from src.db.db_manager import json_into_db, cur

from src.main import generate_analysis_file, generate_fig_folder, delete_pycache_dirs
from src.analysis.plotting import plot_bar_chart, prep_data

config = load_config()
r = "commodities_prices_all"

if __name__ == "__main__":
    json_into_db(r)
    generate_analysis_file(r)
    generate_fig_folder(r)

    res = cur.execute("""SELECT DISTINCT AVG(price_sell_avg) AS price_sell, commodity_name 
from commodities_prices_all
WHERE price_sell_avg > 0
GROUP BY commodity_name
ORDER BY price_sell asc;
                      """)
    
    x,y = prep_data(res)
    plot_bar_chart(x, y, "Value", "Commodity", "Average price of commodities", False)

    delete_pycache_dirs()