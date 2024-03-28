from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="78041bd5c835902c252e9252489cd8fe"
)

audio = client.generate(
    text="Hello!",
    voice=Voice(
        voice_id='EXAVITQu4vr4xnSDxMaL',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

play(audio)

client = ElevenLabs(
  api_key="78041bd5c835902c252e9252489cd8fe"     # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
  text="Hello!",
  voice="Rachel",
  model="eleven_multilingual_v2"
)
play(audio)