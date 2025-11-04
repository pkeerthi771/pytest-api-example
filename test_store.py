from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
import requests
from app.schemas import order

Base_URL= " http://localhost:8000"
def test_patch_order(order_data):
create_resp= requests.post(f"{base_URL}/store/order",json=order_data)
assert create_resp.status_code in[200,201]

order_id= order_data["id"]
patch_payload={
"status": "delivered",
"complete": True
}

patch_resp= requests.patch("f{Base_URL}/store/order/{order_id}", json= patch_payload)

assert patch_resp.status_code==200

json_resp= patch_resp.json()
assert json_resp.get("message")==" order and pet status updated successfully"

updated_order= order(**json_resp["order"])
assert updated_order.status == "delivered"
assert updated_order.complete is true

2) *Optional* Consider using @pytest.fixture to create unique test data for each run

import pytest    
import random

@pytest.fixture
def order_data():
"""fixture that creates a unique order payload for each test run."""
return{
"id": random.randint(1000,9999),
"petid": random.randint(100,999),
"quantity":1,
"shipDate": "2025-11-04T00:00:00.000z",
"status": "placed",
"complete": false
}
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
 from pydantic import Basemodel
 from typing import Optional

 Class Order(Basemodel):
 id: int
 petId: int
 quantity: int
 shipDate: Optional[Str]= None
 status: str
 complete: bool

3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"

'''
def test_patch_order_by_id():
    pass
