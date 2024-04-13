from dotenv import load_dotenv

load_dotenv()

import fal_client





def generate_image(text):
    IMAGE_GEN_PROMPT = f"illustrative art of {text}.  Muted, colorful, painterly, concept art."
    handler = fal_client.submit(
        "fal-ai/fast-lightning-sdxl",
        arguments={
            "image_size" : {
                "width": 768,
                "height": 768
            },
            "prompt": IMAGE_GEN_PROMPT
        },
    )

    log_index = 0
    for event in handler.iter_events(with_logs=True):
        if isinstance(event, fal_client.InProgress):
            new_logs = event.logs[log_index:]
            for log in new_logs:
                print(log["message"])
            log_index = len(event.logs)

    result = handler.get()
    return result['images'][0]['url']

text = input("Please enter your dream idea: ")
print(generate_image(text))