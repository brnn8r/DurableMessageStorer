import logging
import azure.durable_functions as df


def entity_function(context: df.DurableEntityContext):

    saved_messages: list = context.get_state(lambda: [])

    operation = context.operation_name

    if operation == "save":
        message = context.get_input()

        logging.info(f"saving {message} to existing state {saved_messages}")

        saved_messages.append(message)

        context.set_state(saved_messages)
        context.set_result(saved_messages)

    elif operation == "persist":

        logging.info(f"persisting {saved_messages}")

        context.destruct_on_exit()

        logging.info("purged saved messages after persisting")
    else:
        raise ValueError(f"Unknown operation {operation}")


main = df.Entity.create(entity_function)
