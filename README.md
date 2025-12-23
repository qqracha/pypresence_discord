Discord RPC Status ( ͡° ͜ʖ ͡°)

Simple Python script to set custom Discord Rich Presence status using pypresence.

- Clean config separation (.env)
- Error handling and logging

Quick Start

1) Create Discord Application at https://discord.com/developers/applications
2) Copy Application ID to .env
3) Install dependencies:

```text
pip install -r requirements.txt 
```


Example .env 

```text
CLIENT_ID=app_id_here
STATUS_STATE=Building something awesome
STATUS_DETAILS=Using pypresence
```
Works on Python 3.9+
