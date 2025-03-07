import asyncio
from telegram import Bot
from ummalqura.hijri_date import HijriDate 
from datetime import date

TOKEN = "6894579573:AAHbFFEG3E566Gp-KWS5ItUVzpa-N-NZizM"
CHAT_ID = "-1001664031492"
THREAD_ID = 8961

async def send_poll():
    bot = Bot(token=TOKEN)

    
    today_gregorian = date.today()
    hijri_date = HijriDate(today_gregorian.year, today_gregorian.month, today_gregorian.day, gr=True)
    hijri_today = f"{hijri_date.day} {hijri_date.month_name} {hijri_date.year} H"

    
    await bot.send_poll(
        chat_id=CHAT_ID,
        message_thread_id=THREAD_ID, 
        question=f"ABSENSI ({hijri_today}) - Sudah tilawah berapa juz?",
        options=["1 Juz", "2 Juz", "3 Juz", "4 Juz", "5 Juz"],
        is_anonymous=False
    )

if __name__ == "__main__":
    asyncio.run(send_poll())
