import logging

import azure.functions as func
import azure.durable_functions as df


async def main(mytimer: func.TimerRequest, starter: str) -> None:
    client = df.DurableOrchestrationClient(starter)

    entityId = df.EntityId("message_store", "my_message_store")

    logging.info("persisting saved messages")
    await client.signal_entity(entityId, "persist", None)

    logging.info("persisted saved messages")
