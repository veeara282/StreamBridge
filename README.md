# StreamBridge
Listen to Twitch streams on your phone

## System architecture

Key components:

### Client (`client/`)
- Captures audio from the user's PC and streams it to a WebSocket on the server

### Server (`server/`)

Functionality:
- Listens for incoming calls from the user (via Twilio webhooks)
- Patches the user into the stream audio (using a [bidirectional Media Stream][mediastream])

Structure:
- Webhooks for Twilio voice API calls (HTTPS)
- Input WebSocket for client audio stream
- Output WebSocket for Media Stream to Twilio
- State stored across HTTPS/WebSocket sessions

[mediastream]: https://www.twilio.com/docs/voice/media-streams
