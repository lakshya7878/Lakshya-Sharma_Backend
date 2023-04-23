from fastapi import APIRouter
from typing import Optional
from config.database import conn
from models.trade_models import Trade,TradeDetails
from schemas.trade_schema import trades_serializer,trade_serializer
from datetime import datetime
from bson import BSON
import json



client = APIRouter()

@client.get("/trades")
async def List_Trades(search : Optional[str] = None,assetClass : Optional[str] = None,end : Optional[datetime] = None,maxPrice : Optional[float] = None,minPrice : Optional[float] = None,start : Optional[datetime] = None,tradeType : Optional[str] = None) :
    items = trades_serializer(conn.info.Trades.find()) 
    quer = []
    anyquery = (search != None or assetClass!=None or maxPrice!=None or minPrice!=None or start!=None or tradeType!=None)    
    if(not anyquery) :
        return items
    for item in items: 
        print(item)
        if(search!=None) :
            if(search not in item["trader"] and search not in item["counterparty"] and search not in item["instrument_id"] and search not in item["instrument_name"]) :
                continue
        if(assetClass!=None):
            if(assetClass!=item["asset_class"]) :
                continue
        if(maxPrice!=None):
            if(item["trade_details"]["price"]>maxPrice):
                continue
        if(minPrice!=None) :
            if(item["trade_details"]["price"]<minPrice):
                continue
        if(tradeType!=None) :
            if(item["buySellIndicator"]!=tradeType):
                continue
        if(start!=None) :
            if(start<item["trade_date_time"]) :
                continue
        if(end!=None):
            if(end>item["trade_date_time"]) :
                continue
        quer.append(item)  
    if(len(quer)==0):
        quer = {"No such trades found" }
    return quer


@client.get("/tradeById/{trade_id}") 
async def Trade_By_Id(trade_id : str) : 
    items = trades_serializer(conn.info.Trades.find()) 
    for item in items :
        if(item["trade_id"]==trade_id):
            return [item]
    return [{"Trade Id Not-Found"}]


@client.post("/addtrade")
async def Add_Trade(item : Trade):
    # if(conn.info.Trades.find({"trade_id" : item["trade_id"]}).count()>0):
        # return {"Trade ID already exists"}
    jss = json.dumps(item.__dict__,default=str)
    conn.info.Trades.insert_one(dict(jss))
    return item