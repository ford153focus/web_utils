import asyncio
import os
import sys
import time

import nest_asyncio

from pyppeteer import launch

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

import libbrowser
import gaemz.genshin.genshin_shared_utils as gsu

os.environ['PYTHONASYNCIODEBUG'] = '1'


url = "https://act.hoyoverse.com/ys/event/e20220526yelan-q8ne/index.html"


async def main():
    for profile in gsu.profile_names:
        libbrowser.launch_options["userDataDir"] = libbrowser.get_chromium_user_data_dir(profile)
        browser = await launch(libbrowser.launch_options)
        page = await browser.newPage()
        await page.goto(url)
        if await gsu.check_auth(page) is False: raise Exception("Auth problem!")  # check auth

        time.sleep(15)

        # start
        await libbrowser.click_if_exists(page, "button.mihoyo-cookie-tips__button")  # click cookie button
        for span in await page.xpath('//span[contains(text(), "Click to Start")]'):
            await page.evaluate('(element) => element.click()', span)

        time.sleep(15)

        # dialog with millelith
        while await page.querySelector("div.gal-text__content") is not None:
            await page.click('div.gal-text__content')
            time.sleep(10)

        time.sleep(15)

        # share page
        for div in await page.xpath('//div[contains(text(), "Share to gain more information")]'):
            await page.evaluate('(element) => element.click()', div)
        div = (await page.querySelectorAll("div.me-share-popover__item"))[3]
        await page.evaluate('(element) => element.click()', div)

        time.sleep(15)

        # desc page
        for div in await page.querySelectorAll('div'):
            if await page.evaluate('(element) => element.className.includes("---close---")', div):
                await page.evaluate('(element) => element.click()', div)
                break

        time.sleep(15)

        # dialogs with workers
        while await page.querySelector("div.gal-text__content") is not None:
            await page.click('div.gal-text__content')
            time.sleep(10)

        time.sleep(15)

        # desc page
        for x in range(5):
            await libbrowser.click_if_exists(page, 'svg > g')
            time.sleep(1)

        time.sleep(15)

        # select suspect
        loop.run_until_complete(page.click('div.swiper-next'))
        time.sleep(10)
        for span in loop.run_until_complete(page.querySelectorAll('span[id^=option]')):
            loop.run_until_complete(page.evaluate('(element) => element.click()', span))
            time.sleep(5)
        for div in await page.xpath('//div[contains(text(), "Identify the suspect")]'):
            await page.evaluate('(element) => element.click()', div)
        time.sleep(3)
        for div in await page.xpath('//div[contains(text(), "Confirm")]'):
            await page.evaluate('(element) => element.click()', div)
        time.sleep(3)

        time.sleep(15)

        # final scene
        loop.run_until_complete(page.click('div.gal-text__content'))

        time.sleep(15)

        await browser.close()

loop = asyncio.get_event_loop()
nest_asyncio.apply(loop)
loop.run_until_complete(main())
