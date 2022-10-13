# tickers
# --------------------------------------------------------------------------
tickers_dict = {

    "eth_usd": {
        
        "daily": {
            
            "ticker": "ETH-USD",
            "ylabel": "U.S. dollar ($)",
            "date_train_init": "2021-01-01",
            "date_train_end": "2022-09-30",
            "date_predict_init": "2022-10-01",
            "date_predict_end": "2022-10-31",
            "model_parameters": (1,1,3,1,2,1,7), #1,1,3,1,2,1,7
            "dependent_variable": 'close',
            "independent_variables": ['high','low'],
            "freq": "D",
            "style_graph": "default",
            "color1": "royalblue",
            "color2": "darkorange",
            "color3": "crimson",
            "color4": "black",
            "color5": "red",
            "p_value_accepted": 0.05,
            
            "dummy": {}
            
        },
        
        "monthly": {
            
            "ticker": "ETH-USD",
            "ylabel": "U.S dollar ($)",
            "date_train_init": "2017-01-01",
            "date_train_end": "2022-06-01",
            "date_predict_init": "2022-07-01",
            "date_predict_end": "2022-12-31",
            "model_parameters": (0,1,1,1,0,0,12), #0,1,1,1,0,0,12
            "dependent_variable": 'close',
            "independent_variables": ['high','low'],
            "freq": "MS",
            "style_graph": "default",
            "color1": "royalblue",
            "color2": "goldenrod",
            "color3": "crimson",
            "color4": "black",
            "color5": "red",
            "p_value_accepted": 0.05,
            
            "dummy": {}
            
        }
        
    },

    "btc_usd": {
        
        "daily": {
            
            "ticker": "BTC-USD",
            "ylabel": "U.S. dollar ($)",
            "date_train_init": "2021-02-01",
            "date_train_end": "2022-09-30",
            "date_predict_init": "2022-10-01",
            "date_predict_end": "2022-10-31",
            "model_parameters": (0,1,2,2,2,0,7), #0,1,2,2,2,0,7
            "dependent_variable": 'close',
            "independent_variables": ['high','low'],
            "freq": "D",
            "style_graph": "default",
            "color1": "royalblue",
            "color2": "darkorange",
            "color3": "crimson",
            "color4": "black",
            "color5": "red",
            "p_value_accepted": 0.05,
            
            "dummy": {}
            
        },
        
        "monthly": {
            
            "ticker": "BTC-USD",
            "ylabel": "U.S dollar ($)",
            "date_train_init": "2017-01-01",
            "date_train_end": "2022-06-01",
            "date_predict_init": "2022-07-01",
            "date_predict_end": "2022-12-31",
            "model_parameters": (1,1,5,1,1,1,12), #1,1,3,1,1,1,12
            "dependent_variable": 'close',
            "independent_variables": ['volume','low','open'],
            "freq": "MS",
            "style_graph": "default",
            "color1": "royalblue",
            "color2": "goldenrod",
            "color3": "crimson",
            "color4": "black",
            "color5": "red",
            "p_value_accepted": 0.05,
            
            "dummy": {}
            
        }
        
    }

}

# --------------------------------------------------------------------------

# x13 arima path
path_x13_arima = "C:/Program Files (x86)/x12arima"
#path_x13_arima = "/home/x13as/"
