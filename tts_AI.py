from elevenlabs import play, VoiceSettings
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key="78041bd5c835902c252e9252489cd8fe"  # Defaults to ELEVEN_API_KEY
)


def ai_tts(text):
    audio = client.generate(
        text=text,
        voice="Bill",
        model="eleven_multilingual_v2",
        voice_settings=VoiceSettings(stability=0.01, similarity_boost=1.0, style=0.0, use_speaker_boost=True)
    )
    play(audio)
