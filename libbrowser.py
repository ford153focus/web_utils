import os
import sys

import pyppeteer.page

launch_arguments = [
    "--start-maximized",
    "--disable-web-security",
    "--disable-features=IsolateOrigins,site-per-process"
]

launch_options = {
    'ignoreHTTPSErrors': True,
    'headless': False,
    'defaultViewport': None
}

if os.name == 'nt':
    if os.path.isfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"):
        launch_options['executablePath'] = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if os.path.isfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"):
        launch_options['executablePath'] = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
elif sys.platform == 'linux':
    if os.path.isfile("/usr/bin/google-chrome"): launch_options['executablePath'] = "/usr/bin/google-chrome"
    launch_arguments.append("--canvas-msaa-sample-count=0")
    launch_arguments.append("--disable-gpu-driver-bug-workarounds")
    launch_arguments.append("--disable-gpu-vsync")
    launch_arguments.append("--disable-features=InfiniteSessionRestore")
    launch_arguments.append("--disable-smooth-scrolling")
    launch_arguments.append("--enable-accelerated-2d-canvas")
    launch_arguments.append("--enable-direct-composition-layers")
    launch_arguments.append("--enable-gpu-rasterization")
    launch_arguments.append("--enable-hardware-overlays")
    launch_arguments.append("--enable-low-res-tiling")
    launch_arguments.append("--enable-native-gpu-memory-buffers")
    launch_arguments.append("--enable-tile-compression")
    launch_arguments.append("--enable-zero-copy")
    launch_arguments.append("--force-gpu-rasterization")
    launch_arguments.append("--gpu-rasterization-msaa-sample-count=0")
    launch_arguments.append("--ignore-gpu-blocklist")

launch_options['args'] = launch_arguments

def get_chromium_user_data_dir(user_name):
    return os.path.join(
        os.path.expanduser("~"),
        ".config",
        "com.ford-rt.web-utils",
        "chromium_user_data_dir",
        user_name
    )

async def click_if_exists(page:pyppeteer.page.Page, selector:str):
    if await page.querySelector(selector) is None: return
    await page.click(selector)
