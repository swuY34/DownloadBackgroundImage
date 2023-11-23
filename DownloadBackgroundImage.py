# !/usr/usuari/des python
#  -*- coding: utf-8 -*-
"""
@Author        : swuY
@Time          : 2022/9/14 20:37
@FileName      : DownloadBackgroundImage.py
@LastEditors   : None
@Editors       : PyCharm
"""

import httpx
import asyncio
import os

def JutgeAtFolder() -> str:
    FolderName = input('要保存到的文件夹的文件夹名: ')
    if FolderName in os.listdir(os.getcwd() + r'\BackgroundImages'):
        pass
    else:
        os.mkdir(fr'{os.getcwd()}\BackgroundImages\{FolderName}')

    return FolderName

async def SaveImage(ImageUrl: str, Headers: dict, FolderName: str) -> None:
    async with httpx.AsyncClient() as Client:
        ImageContent = await Client.get(ImageUrl, headers = Headers)
        FileName = len(os.listdir(os.getcwd() + rf"\BackgroundImages\{FolderName}")) + 1
        with open(rf'BackgroundImages\{FolderName}\{FileName}.png', 'wb') as f:
            f.write(ImageContent.content)
            print(f'{FileName}.png \t--\t 保存完成 WAW')

def main() -> str:
    TaskList = []

    Headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    with open('BackgroundImagesUrls.txt', 'r', encoding = 'utf-8') as f:
        ImageUrls = f.readlines()

    FolderName = JutgeAtFolder()

    for ImageUrl in ImageUrls:
        ImageUrl = ImageUrl.replace('\n', '')
        TaskList.append(SaveImage(ImageUrl, Headers, FolderName))

    Loop = asyncio.get_event_loop()
    Loop.run_until_complete(asyncio.wait(TaskList))

    return 'Finish'

if __name__ == '__main__':
    print(main())