import logging

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)

    message = req.get_json()

    logging.info(f"received {message}")

    entityId = df.EntityId("message_store", "my_message_store")

    logging.info(f"saving {message}")
    await client.signal_entity(entityId, "save", message)

    logging.info(f"saved {message}")
