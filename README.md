# asyncbargpt.py

async lib for bargpt.app

![logo](https://github.com/aminobotskek/bargpt/assets/94906343/752ea161-f0f0-4549-9007-ca184ac819ac)


# Install
```
git clone https://github.com/aminobotskek/asyncbargpt
```

### Example
```python3
import asyncbargpt
import asyncio
async def main():
	client=asyncbargpt.AsyncBargpt()
	data= await client.get_cocktail_count()
	print(data)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
