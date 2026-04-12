import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject

# Cấu hình Token của bạn
API_TOKEN = '8630175808:AAF2HxYop3A0jjHo7HHmc6s05hhs9SDm4DA'
ADMIN_ID = 5636904068  # ID Telegram của bạn để quản lý bot


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Xử lý lệnh /like {uid}
@dp.message(Command("like"))
async def handle_like_command(message: types.Message, command: CommandObject):
    # command.args sẽ lấy phần nội dung sau chữ /like
    uid = command.args

    # 1. Kiểm tra xem người dùng có nhập UID không
    if not uid:
        return await message.reply(
            "⚠️ Vui lòng nhập ID sau lệnh.\n"
            "Ví dụ: `/like 123456789`",
            parse_mode="Markdown"
        )

    # 2. Kiểm tra định dạng UID (phải là số và có độ dài hợp lệ)
    if uid.isdigit() and 8 <= len(uid) <= 12:
        status_msg = await message.reply(f"🚀 Đang gửi yêu cầu Like đến ID: `{uid}`...")
        
        # --- ĐOẠN NÀY KẾT NỐI VỚI PHẦN 1 (LÕI XỬ LÝ) ---
        # Giả lập gọi API buff like
        await asyncio.sleep(2) 
        success = True 
        # ----------------------------------------------

        if success:
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=status_msg.message_id,
                text=f"✅ **Thành công!**\nID: `{uid}` đã được cộng Like.",
                parse_mode="Markdown"
            )
        else:
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=status_msg.message_id,
                text="❌ Lỗi kết nối máy chủ Buff."
            )
    else:
        await message.reply("⚠️ ID không hợp lệ. ID Free Fire phải là dãy số từ 8-12 ký tự.")

async def main():
    print("Bot đang sẵn sàng nhận lệnh /like...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    