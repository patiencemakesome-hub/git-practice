from orderlab.csv_report import revenue_from_csv


def test_sample_orders_revenue():
    assert revenue_from_csv("data/sample_orders.csv") == 55_000
