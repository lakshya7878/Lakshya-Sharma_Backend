from datetime import datetime
import json
def trade_serializer(item) -> dict : 
    return{
        "trade_id" : str(item["trade_id"]),
        "asset_class": str(item["asset_class"]),
        "instrument_id": str(item["instrument_id"]),
        "counterparty": str(item["counterparty"]),
        "instrument_name": str(item["instrument_name"]),
        "trade_date_time": item["trade_date_time"],
        "trader": str(item["trader"]),
        'trade_details' : {
            'buySellIndicator' : str(item['trade_details']['buySellIndicator']),
            'price' : float(item['trade_details']['price']),
            'quantity' : int(item['trade_details']['quantity'])
        }
    }

def trades_serializer(items) -> list :
    return [trade_serializer(item) for item in items]

def convertTradedetails(item) -> dict :
    ret = {}
    for keys,vals in item :
        ret[keys] = vals
    return(ret)