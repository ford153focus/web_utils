import pyppeteer.page

profile_names = [
    "ford153focus@gmail.com",
    "ff000206@gmail.com",
    "reg3@ford-rt.com",
    "reg2@ford-rt.com",

    "focus@ford-rt.com",
    "reg1@ford-rt.com",
    "reg5@ford-rt.com"
]


async def check_auth(page: pyppeteer.page.Page):
    cookies = await page.cookies()
    if len(list(filter(lambda cookie: cookie["name"] == "account_id", cookies))) == 0: return False
    if len(list(filter(lambda cookie: cookie["name"] == "cookie_token", cookies))) == 0: return False
