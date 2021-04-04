import logging

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)

    req_body = req.get_json()
    message = req_body.get('msg')

    logging.info(f"received {message}")

    message_store_id = "my_message_store"
    entityId = df.EntityId("message_store", message_store_id)

    logging.info(f"saving {message}")
    await client.signal_entity(entityId, "save", message)

    logging.info(f"saved {message}")

    return func.HttpResponse("Successfully sent {message} to message_store@{message_store_id}", status_code=200)
