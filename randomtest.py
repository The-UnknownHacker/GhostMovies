from gradio_client import Client

user_input = input('Enter A Prompt: ')

client = Client("https://bytedance-animatediff-lightning.hf.space")  # Replace with the correct URL
result = client.predict(
    prompt=user_input,  # Any text prompt
    base="ToonYou",  # Can be ToonYou or epiCRealism
    motion="",  # Can be Zoom in, Zoom out, Tilt up, Tilt down, Pan left, Pan right, Roll left, Roll right
    step="4",  # 2, 4, 6, 8
    api_name="/generate_image"
)
print(result)
