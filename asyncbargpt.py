import aiohttp,asyncio
class AsyncBargpt():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.api="https://www.bargpt.app/api"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def search_cocktails(self,q):
		async with self.session.get(f"{self.api}/searchcocktails?search={q}",headers=self.headers) as req:
			return await req.json()
	async def search_ingredient_list(self,q):
		async with self.session.get(f"{self.api}/searchingredientlist?search={q}",headers=self.headers) as req:
			return await req.json()
	async def like_recipe(self,cid):
		async with self.session.get(f"{self.api}/likerecipe?cid={cid}",headers=self.headers) as req:
			return await req.json()
	async def get_featured_cocktails(self):
		async with self.session.get(f"{self.api}/getfeaturedcocktails",headers=self.headers) as req:
			return await req.json()
	async def get_cocktail_count(self):
		async with self.session.get(f"{self.api}/getcocktailcount",headers=self.headers) as req:
			return await req.json()
	async def get_credits_for_user(self):
		async with self.session.get(f"{self.api}/getcreditsforuser",headers=self.headers) as req:
			return await req.json()