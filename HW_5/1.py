import asyncio
import os
from hashlib import md5
from http import HTTPStatus

import aiofiles
import aiofiles.os
import aiohttp


async def download_images(folder, count, max_tasks=20):
    url = "https://picsum.photos/200"  # Также работает и с https://thispersondoesnotexist.com/

    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    # Считывание существующих хэшей из файлов в папке, чтобы избежать дубликатов
    known_hashes = set()
    for f in await aiofiles.os.listdir(folder):
        if await aiofiles.os.path.isfile(os.path.join(folder, f)):
            known_hashes.add(f.split(".")[0])

    counter = asyncio.Lock()
    counter.value = 0
    counter.max = count

    semaphore = asyncio.Semaphore(max_tasks)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(max_tasks):
            task = asyncio.create_task(download_image(session, url, folder, known_hashes, counter, semaphore))
            tasks.append(task)

        await asyncio.gather(*tasks)


async def download_image(session, url, folder, known_hashes, counter, semaphore):
    async with semaphore:
        while True:
            async with counter:
                # Проверка, достигнуто ли желаемое количество загрузок
                if counter.value >= counter.max:
                    return

            async with session.get(url) as response:
                if response.status == HTTPStatus.OK:
                    data = await response.read()
                    file_hash = md5(data).hexdigest()

                    # Проверка на уникальность файла
                    if file_hash not in known_hashes:
                        async with counter:
                            # Повторная проверка после получения блокировки
                            if counter.value >= counter.max:
                                return

                            known_hashes.add(file_hash)
                            counter.value += 1

                        filename = f"{folder}/{file_hash}.jpg"

                        async with aiofiles.open(filename, mode="wb") as file:
                            await file.write(data)
                            print(f"Downloaded {filename}")

                    else:
                        print("Duplicate found, redownloading...")
                        await asyncio.sleep(1)

                else:
                    print("Failed to download image, retrying...")
                    await asyncio.sleep(1)


if __name__ == "__main__":
    count = 100
    folder = "downloaded_images"
    asyncio.run(download_images(folder, count))
