from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs


play(audio)

client = ElevenLabs(
    api_key="78041bd5c835902c252e9252489cd8fe"  # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
    text="Hello!",
    voice="Rachel",
    model="eleven_multilingual_v2"
)

play(audio)
