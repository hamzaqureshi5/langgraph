

import time
import asyncio

async def coffee():
    print("Start Coffee...")
    await asyncio.sleep(3)
    print("End Coffee...")
    
async def shake():
    print("Start Shake...")
    await asyncio.sleep(4)
    print("End Shake...")
    
async def main():
    start_time = time.time()
    batch = asyncio.gather(coffee(), shake())
    c, s = await batch
    end_time = time.time()

    print("Time is ", end_time-start_time)

if __name__ == "__main__":    
    asyncio.run(main())