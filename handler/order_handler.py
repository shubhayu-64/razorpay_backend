from fastapi import APIRouter,HTTPException, status
import models
import razorpay
import requests


client = razorpay.Client(auth=("rzp_test_mWdZk20UX7IlbJ", "MIr4H6uK6tebUGCpIYMGIHdp"))
client.set_app_details({"title" : "Flutter Backend", "version" : "0.1.0"})

router = APIRouter()

@router.post("/orderid")
async def get_order_id(order: models.Order):
    body = {
        "amount": order.amount*100,
        "currency": "INR",
        "receipt": order.receipt,
    }

    exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND)

    response = client.order.create(body)

    if response:
        print(response)
        return response
    else:
        raise exception