from fastapi import FastAPI, HTTPException
import razorpay

app = FastAPI()

# Initialize Razorpay client with your API keys
razorpay_client = razorpay.Client(auth=("rzp_test_rmOhEnuL2Aq2jl", "NGbeJqNNro7dWBLVdYDgLW6A"))

@app.post("/create-payment")
async def create_payment(amount: int):
    # Create a Razorpay payment order
    payment_data = {
        "amount": amount * 100,  # Convert amount to paisa (currency's smallest unit)
        "currency": "INR",
        "receipt": "order_receipt_1",
        "payment_capture": 1
    }

    try:
        payment = razorpay_client.order.create(data=payment_data)
        return {"order_id": payment["id"]}
    except Exception as e:
        return {"error": str(e)}

# @app.get("/verify-payment/{order_id}")
# async def verify_payment(order_id: str):
#     try:
#         # Fetch the payment details from Razorpay using the order ID
#         order = razorpay_client.order.fetch(order_id)
#         payment_id = order.get("payments")[0]["payment_id"]
        
#         # Fetch the payment details using the payment ID
#         payment = razorpay_client.payment.fetch(payment_id)
        
#         # Check the payment status
#         status = payment.get("status")
#         return {"payment_status": status}
#     except Exception as e:
#         return {"error": str(e)}

# from fastapi import FastAPI, Form/create-payment
# import razorpay
# import json

# app = FastAPI()

# razorpay_key_id = "rzp_test_fGGHmOOCjnWlEA"
# razorpay_key_secret = "SXEE7L5VZTwilqFmDNuRUwp7j"

# razorpay_client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))
# @app.post('/charge')
# async def app_charge(razorpay_payment_id: str = Form(...), amount: int = Form(...)):
#     try:
#         # Your code to capture the payment using Razorpay client
#         # Use the 'razorpay_payment_id' and 'amount' parameters as needed in your payment capture logic

#         # Create a JSON-serializable response
#         payment = razorpay_client.payment.capture(razorpay_payment_id,amount)
#         # response_data = {"message": "Payment captured successfully"}
#         return payment

#     except razorpay.errors.RazorpayError as e:
#         return {"error": str(e)}




# rzp_test_fGGHmOOCjnWlEA key
# SXEE7L5VZTwilqFmDNuRUwp7 sc k








