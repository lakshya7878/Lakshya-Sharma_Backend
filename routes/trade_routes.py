from fastapi import APIRouter
from typing import Optional
from config.database import conn
from models.trade_models import Trade,TradeDetails
from schemas.trade_schema import trades_serializer,trade_serializer,convertTradedetails
from datetime import datetime
import json
from bson import json_util
from fastapi_pagination import Page, add_pagination, paginate  


client = APIRouter()
add_pagination(client)


@client.get("/trades")
async def List_Trades(search : Optional[str] = None,assetClass : Optional[str] = None,end : Optional[datetime] = None,maxPrice : Optional[float] = None,minPrice : Optional[float] = None,start : Optional[datetime] = None,tradeType : Optional[str] = None)  -> Page[dict] :
    items = trades_serializer(conn.info.Trades.find()) 
    quer = []
    anyquery = (search != None or assetClass!=None or maxPrice!=None or minPrice!=None or start!=None or tradeType!=None)    
    if(not anyquery) :
        return paginate(items)
    for item in items: 
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
            if(item["trade_details"]["buySellIndicator"]!=tradeType):
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
    return paginate(quer)


@client.get("/tradeById/{trade_id}") 
async def Trade_By_Id(trade_id : str) : 
    items = trades_serializer(conn.info.Trades.find()) 
    for item in items :
        if(item["trade_id"]==trade_id):
            return [item]
    return [{"Trade Id Not-Found"}]




@client.get("/sortby/price")
async def Sort_Trades_By_Price() :
    items = trades_serializer(conn.info.Trades.find().sort("trade_details.price")) 
    return items


@client.post("/addtrade")
async def Add_Trade(item : Trade):
    if(conn.info.Trades.count_documents({"trade_id" : item.trade_id}, limit = 1)!=0):
        return {"Trade ID already exists"}

    ret = {}
    for name,value in item :
        if(name!="trade_details") :
            ret[name] = value
        else :
            ret[name] = convertTradedetails(value)
    conn.info.Trades.insert_one(ret)
    return ["Successfuly Inserted" ,trades_serializer(conn.info.Trades.find({"trade_id" : item.trade_id}))]


@client.put("/update/{trade_id}")
async def Update_Trade(trade_id : str ,asset_class: Optional[str] =None,trader: Optional[str] = None ) :
    if(conn.info.Trades.find({"trade_id" : trade_id})):
        filter = { 'trade_id': trade_id }
        if(asset_class!=None):
            newvalues = { "$set": { 'asset_class': asset_class } }
            conn.info.Trades.update_one(filter, newvalues)
        if(trader!=None) :
            newvalues = { "$set": { 'trader': trader } }
            conn.info.Trades.update_one(filter, newvalues)
        return ["Successfuly Updated" ,trades_serializer(conn.info.Trades.find(filter))]

    else :
        return {"No such ID exists"}
        
@client.delete("/delete/{trade_id}")
async def Delete_Trade(trade_id : str) :
    if(conn.info.Trades.find({"trade_id" : trade_id})):
        conn.info.Trades.delete_one({"trade_id" : trade_id})
        return {"Deleted Successfully"}
    else :
        return {"No such trade exists"}



