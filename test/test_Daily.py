import pytest

from src.alpha_views import AlphaViews

test_data = {
    "1234": {"symbol": "IBM", "interval": 5, "stock_api": "iseries"},
    "1235": {"symbol": "IBM", "interval": 5, "slice": (1,5), "stock_api": "ieseries", 'content': "application/x-download"},
     "1236": {"symbol": "IBM", "stock_api": "dseries"},
    "1237": {"symbol": "IBM", "stock_api": "daseries"},
    "1238": {"symbol": "IBM", "stock_api": "wseries"},
    # "1239": {"symbol": "IBM", "stock_api": "waseries"},
    "1240": {"symbol": "IBM", "stock_api": "mseries"}
    # "1241": {"symbol": "IBM", "stock_api": "maseries"}

}


@pytest.mark.parametrize("tdata", test_data)
def test_time_series_daily(tdata, get_env, init_conf_prop):

    series = test_data[tdata].get('stock_api', '')
    print(series)
    alpha_base = AlphaViews(init_conf_prop, get_env, series)
    symbol = test_data[tdata].get('symbol', 'IBM')
    interval = test_data[tdata].get('interval', 0)
    slice = test_data[tdata].get('slice', (0, 0))
    content = test_data[tdata].get('content', 'application/json')
    alpha_base.get_stock_response(series, symbol, interval, slice)
    if series != 'ieseries':
        alpha_base.alpha_schema_validation(series)
        alpha_base.data_error_validation()
        alpha_base.data_time_data_validation(series == 'mseries')
        alpha_base.basic_response_validation(content_type=content)


#
# @pytest.mark.skip
# def test_time_series_daily(get_env, init_conf_prop):
#     alpha_base = AlphaViews(init_conf_prop, get_env)
#     response = alpha_base.get_stock_response("dseries", "IBM")
#     alpha_base.basic_response_validation(response, content_type= "application/json")
#     alpha_base.data_error_validation(response.json())
