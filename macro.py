import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Bật logging để theo dõi hoạt động
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Menu chính
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 *Danh sách game:*\n\n"
        "1. Liên Quân (/lienquan)\n"
        "2. Free Fire (/freefire)\n"
        "3. PUBG Mobile (/pubg)\n",
        parse_mode="Markdown"
    )

# ---------------- Liên Quân ----------------
async def lienquan_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ *Liên Quân* — Chọn vai trò:\n\n"
        "1️⃣ Đỡ đòn (/lq_dodon)\n"
        "2️⃣ Đấu sĩ (/lq_dausi)\n"
        "3️⃣ Sát thủ (/lq_sathu)\n"
        "4️⃣ Pháp sư (/lq_phapsu)\n"
        "5️⃣ Xạ thủ (/lq_xathu)\n"
        "6️⃣ Trợ thủ (/lq_trothu)\n",
        parse_mode="Markdown"
    )

async def lq_dodon(update, context): await update.message.reply_text("💪 *Đỡ đòn*:\n- Toro\n- Mganga\n- Thane\n", parse_mode="Markdown")
async def lq_dausi(update, context): await update.message.reply_text("⚔️ *Đấu sĩ*:\n- Wukong\n- Florentino\n- Rourke\n", parse_mode="Markdown")
async def lq_sathu(update, context): await update.message.reply_text("🔪 *Sát thủ*:\n- Nakroth\n- Murad\n- Zill\n", parse_mode="Markdown")
async def lq_phapsu(update, context): await update.message.reply_text("🔮 *Pháp sư*:\n- Lauriel\n- Ilumia\n- Diao Chan\n", parse_mode="Markdown")
async def lq_xathu(update, context): await update.message.reply_text("🏹 *Xạ thủ*:\n- Valhein\n- Tel'Annas\n- Capheny\n", parse_mode="Markdown")
async def lq_trothu(update, context): await update.message.reply_text("🛡️ *Trợ thủ*:\n- Alice\n- Annette\n- Chaugnar\n", parse_mode="Markdown")

# ---------------- Free Fire ----------------
async def freefire_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ *Free Fire* — Chọn nhân vật:\n\n"
        "1️⃣ Chrono (/ff_chrono)\n"
        "2️⃣ Alok (/ff_alok)\n"
        "3️⃣ Kelly (/ff_kelly)\n"
        "4️⃣ K (/ff_k)\n"
        "5️⃣ Hayato (/ff_hayato)\n",
        parse_mode="Markdown"
    )

async def ff_chrono(update, context): await update.message.reply_text("🛡️ *Chrono*:\n- Tạo lá chắn năng lượng chặn sát thương.\n", parse_mode="Markdown")
async def ff_alok(update, context): await update.message.reply_text("🎵 *Alok*:\n- Tạo hào quang hồi máu và tăng tốc.\n", parse_mode="Markdown")
async def ff_kelly(update, context): await update.message.reply_text("🏃 *Kelly*:\n- Tăng tốc độ chạy khi chuyển hướng.\n", parse_mode="Markdown")
async def ff_k(update, context): await update.message.reply_text("✂️ *K*:\n- Chuyển trạng thái tăng cận chiến hoặc máu tối đa.\n", parse_mode="Markdown")
async def ff_hayato(update, context): await update.message.reply_text("⚔️ *Hayato*:\n- Tăng xuyên giáp theo % HP mất.\n", parse_mode="Markdown")

# ---------------- PUBG ----------------
async def pubg_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ *PUBG Mobile* — Chọn loại vũ khí:\n\n"
        "1️⃣ AR (/pubg_ar)\n"
        "2️⃣ SMG (/pubg_smg)\n"
        "3️⃣ Sniper (/pubg_sniper)\n"
        "4️⃣ Shotgun (/pubg_shotgun)\n",
        parse_mode="Markdown"
    )

async def pubg_ar(update, context): await update.message.reply_text("🔫 *AR*:\n- M416\n- AKM\n- SCAR-L\n", parse_mode="Markdown")
async def pubg_smg(update, context): await update.message.reply_text("🔫 *SMG*:\n- UMP45\n- Vector\n- MP5K\n", parse_mode="Markdown")
async def pubg_sniper(update, context): await update.message.reply_text("🔫 *Sniper*:\n- AWM\n- Kar98k\n- M24\n", parse_mode="Markdown")
async def pubg_shotgun(update, context): await update.message.reply_text("🔫 *Shotgun*:\n- S1897\n- S686\n- DBS\n", parse_mode="Markdown")

# ---------------- Unknown command ----------------
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❗ Lệnh không hợp lệ. Gõ /menu để xem danh sách.")

# ---------------- Main ----------------
if __name__ == '__main__':
    app = ApplicationBuilder().token("YOUR_TOKEN_HERE").build()

    # Menu chính
    app.add_handler(CommandHandler("menu", menu))

    # Liên Quân
    app.add_handler(CommandHandler("lienquan", lienquan_menu))
    app.add_handler(CommandHandler("lq_dodon", lq_dodon))
    app.add_handler(CommandHandler("lq_dausi", lq_dausi))
    app.add_handler(CommandHandler("lq_sathu", lq_sathu))
    app.add_handler(CommandHandler("lq_phapsu", lq_phapsu))
    app.add_handler(CommandHandler("lq_xathu", lq_xathu))
    app.add_handler(CommandHandler("lq_trothu", lq_trothu))

    # Free Fire
    app.add_handler(CommandHandler("freefire", freefire_menu))
    app.add_handler(CommandHandler("ff_chrono", ff_chrono))
    app.add_handler(CommandHandler("ff_alok", ff_alok))
    app.add_handler(CommandHandler("ff_kelly", ff_kelly))
    app.add_handler(CommandHandler("ff_k", ff_k))
    app.add_handler(CommandHandler("ff_hayato", ff_hayato))

    # PUBG
    app.add_handler(CommandHandler("pubg", pubg_menu))
    app.add_handler(CommandHandler("pubg_ar", pubg_ar))
    app.add_handler(CommandHandler("pubg_smg", pubg_smg))
    app.add_handler(CommandHandler("pubg_sniper", pubg_sniper))
    app.add_handler(CommandHandler("pubg_shotgun", pubg_shotgun))

    # Handler cho lệnh không xác định
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    app.run_polling()
