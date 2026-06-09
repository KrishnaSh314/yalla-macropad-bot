"""
================================================
  YALLA PIPS — MACROPAD TELEGRAM SALES BOT
  Selling the Yalla Macropad keyboard
  Website: yallapips.com
================================================

SETUP:
1. pip install python-telegram-bot
2. Replace YOUR_BOT_TOKEN with token from @BotFather
3. Fill in your details in CONFIGURATION section
4. Run: python macropad_bot.py
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ─────────────────────────────────────────────
#   ★  CONFIGURATION — FILL IN YOUR DETAILS  ★
# ─────────────────────────────────────────────

BOT_TOKEN        = "8891951081:AAG1YtCi8ejncPS-8mVM1X062esTdeNBDNQ"          # From @BotFather
WEBSITE_URL      = "https://yallapips.com"
PREORDER_LINK    = "https://yallapips.com/keyboard.html"
DEMO_LINK        = "https://yallapips.com/demo"   # Your live demo booking link
SUPPORT_USERNAME = "@yallamacropad_bot"          # Your Telegram username
CHANNEL_LINK     = "https://t.me/YallaPipsDigger"

# ─── MACROPAD SPECS ───────────────────────────
MACROPAD_SPECS = {
    "name":       "Yalla Macropad",
    "tagline":    "15 full-colour LCD keys. The entire trading desk in your hand.",
    "price":      "$590",
    "edition":    "Edition 01 — Only 250 units",
    "latency":    "<3ms",
    "keys":       "15 full-colour LCD keys",
    "actions":    "BUY · SELL · Partial Close · Break Even · Trail SL · Close All",
    "compatible": "MT4 · MT5 · TradingView · cTrader",
    "preorder":   PREORDER_LINK,
}

# ─── KEY FEATURES ─────────────────────────────
FEATURES = [
    ("⚡", "15 Full-Colour LCD Keys",
     "Every key has its own screen — showing live labels, colours and status in real time."),
    ("🎯", "One-Tap Trading Actions",
     "BUY, SELL, partial close, break even and trailing stop loss — all mapped to a single tap."),
    ("⚡", "<3ms Latency",
     "Near-instant execution. Between you pressing the key and MT4/MT5 receiving the command."),
    ("🎨", "Customisable Layout",
     "Remap every key to any function you need. Your desk, your rules."),
    ("📊", "Live Data on Keys",
     "Keys display live P&L, open positions, and market status directly on the LCD screen."),
    ("🔒", "Limited to 250 Units",
     "Edition 01 is strictly limited. Once they're gone, they're gone."),
    ("🖥", "Works with All Platforms",
     "Plug-and-play with MT4, MT5, TradingView and cTrader. No drivers needed."),
    ("📦", "Ships Worldwide",
     "We ship to India, UAE, UK, US and all major markets."),
]

# ─── FAQ ──────────────────────────────────────
FAQS = [
    ("What does the Macropad do?",
     "It's a physical keyboard with 15 full-colour LCD keys specifically designed for trading. "
     "Each key is mapped to a trading action — BUY, SELL, partial close, break even, "
     "trailing stop loss and more. One tap executes the action instantly on your platform."),

    ("Which platforms does it work with?",
     "MT4, MT5, TradingView and cTrader. Plug-and-play — no complex setup required."),

    ("How fast is it?",
     "Under 3 milliseconds latency from key press to platform execution. "
     "Faster than any mouse click or keyboard shortcut."),

    ("How many units are available?",
     "Edition 01 is strictly limited to 250 units worldwide. "
     "Once sold out, there is no guarantee of a second edition."),

    ("What is the price?",
     f"Pre-order price is {MACROPAD_SPECS['price']}. "
     "This is the launch price — price may increase after Edition 01 sells out."),

    ("When does it ship?",
     "Edition 01 is currently in pre-order. Shipping dates are on the website. "
     f"Book a live demo first to see it in action: {DEMO_LINK}"),

    ("Do I need any coding or technical knowledge?",
     "No. The Macropad comes pre-configured with the most common trading actions. "
     "Remapping keys is done through a simple drag-and-drop interface."),

    ("Is there a refund policy?",
     "Yes — if the Macropad doesn't work as described on arrival, "
     f"contact us at `{SUPPORT_USERNAME}` and we will resolve it."),
]


# ─────────────────────────────────────────────
#   KEYBOARDS
# ─────────────────────────────────────────────

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⌨️  What is the Macropad?",  callback_data="what")],
        [InlineKeyboardButton("🎯  Features & Specs",       callback_data="features"),
         InlineKeyboardButton("💰  Price & Pre-order",      callback_data="preorder")],
        [InlineKeyboardButton("🎬  Book a Live Demo",       url=DEMO_LINK)],
        [InlineKeyboardButton("❓  FAQ",                    callback_data="faq"),
         InlineKeyboardButton("📞  Support",               callback_data="support")],
        [InlineKeyboardButton("📢  Join Our Channel",       url=CHANNEL_LINK),
         InlineKeyboardButton("🌐  Visit Website",         url=WEBSITE_URL)],
    ])


def back_keyboard(extra_buttons=None):
    buttons = extra_buttons or []
    buttons.append([InlineKeyboardButton("⬅️  Back to menu", callback_data="menu")])
    return InlineKeyboardMarkup(buttons)


# ─────────────────────────────────────────────
#   COMMAND HANDLERS
# ─────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# ── /start ──────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name or "Trader"
    text = (
        f"👋 Welcome, {user}!\n\n"
        f"You've found the official bot for *Yalla Pips* — home of the\n"
        f"*Yalla Macropad* ⌨️\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"15 full-colour LCD keys.\n"
        f"BUY · SELL · Partial Close · Break Even · Trail SL.\n"
        f"The entire trading desk — in your hand.\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🔴 *Edition 01 — Only 250 units. Pre-order now.*\n\n"
        f"Use the menu below to explore, or type a command:\n\n"
        f"/what — What is the Macropad?\n"
        f"/features — Full features & specs\n"
        f"/preorder — Price & how to pre-order\n"
        f"/demo — Book a free live demo\n"
        f"/faq — Common questions\n"
        f"/support — Talk to us"
    )
    await update.message.reply_text(
        text, parse_mode="Markdown",
        reply_markup=main_menu_keyboard()
    )


# ── /what ────────────────────────────────────
async def what(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = (
        f"⌨️ *What is the Yalla Macropad?*\n\n"
        f"The Yalla Macropad is a *physical trading keyboard* — 15 full-colour "
        f"LCD keys, each mapped to a specific trading action.\n\n"
        f"*Instead of:*\n"
        f"❌ Right-clicking on MT4/MT5\n"
        f"❌ Clicking through menus to close a trade\n"
        f"❌ Manually calculating partial close lots\n"
        f"❌ Forgetting to set your break even\n\n"
        f"*With the Macropad:*\n"
        f"✅ One tap → BUY instantly\n"
        f"✅ One tap → SELL instantly\n"
        f"✅ One tap → 25% partial close\n"
        f"✅ One tap → 50% partial close\n"
        f"✅ One tap → Break Even SL\n"
        f"✅ One tap → Trailing Stop Loss\n"
        f"✅ One tap → Close ALL positions\n\n"
        f"*Speed:* Under 3ms from key press to execution.\n"
        f"*Edition 01:* Strictly 250 units worldwide.\n\n"
        f"🌐 See it in action: {WEBSITE_URL}/macropad"
    )
    keyboard = back_keyboard([
        [InlineKeyboardButton("🎬  Book Free Live Demo", url=DEMO_LINK)],
        [InlineKeyboardButton("💰  Pre-order — $590",    url=PREORDER_LINK)],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /features ───────────────────────────────
async def features(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = (
        f"🎯 *Yalla Macropad — Full Specs & Features*\n\n"
        f"⌨️ *Hardware*\n"
        f"• {MACROPAD_SPECS['keys']}\n"
        f"• Latency: {MACROPAD_SPECS['latency']}\n"
        f"• {MACROPAD_SPECS['edition']}\n\n"
        f"🎮 *Pre-mapped Actions*\n"
        f"• {MACROPAD_SPECS['actions']}\n\n"
        f"🖥 *Compatible Platforms*\n"
        f"• {MACROPAD_SPECS['compatible']}\n\n"
        f"✨ *Key Highlights*\n"
    )
    for icon, title, desc in FEATURES:
        text += f"\n{icon} *{title}*\n_{desc}_\n"

    keyboard = back_keyboard([
        [InlineKeyboardButton("💰  Pre-order — $590",    url=PREORDER_LINK)],
        [InlineKeyboardButton("🎬  Book Free Live Demo", url=DEMO_LINK)],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /preorder ────────────────────────────────
async def preorder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = (
        f"💰 *Pre-order the Yalla Macropad*\n\n"
        f"🏷 *Price:* {MACROPAD_SPECS['price']} _(pre-order rate)_\n"
        f"📦 *Edition:* {MACROPAD_SPECS['edition']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"*What's included in your pre-order:*\n\n"
        f"✅ Yalla Macropad — Edition 01\n"
        f"✅ USB-C cable\n"
        f"✅ Quick-start setup guide\n"
        f"✅ Access to key remapping software\n"
        f"✅ Priority shipping — Edition 01 buyers first\n"
        f"✅ Lifetime software updates\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"*How to pre-order:*\n\n"
        f"1️⃣ Visit the link below\n"
        f"2️⃣ Click *Pre-order · $590*\n"
        f"3️⃣ Complete payment (card / PayPal / crypto)\n"
        f"4️⃣ Receive confirmation + shipping update by email\n\n"
        f"⚠️ _Only 250 units available. Once sold out — no restock guaranteed._\n\n"
        f"Questions before buying? Message `{SUPPORT_USERNAME}`"
    )
    keyboard = back_keyboard([
        [InlineKeyboardButton("🛒  Pre-order Now — $590", url=PREORDER_LINK)],
        [InlineKeyboardButton("🎬  Book Free Demo First", url=DEMO_LINK)],
        [InlineKeyboardButton("❓  FAQ",                  callback_data="faq")],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /demo ────────────────────────────────────
async def demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = (
        f"🎬 *Book a Free 30-Minute Live Demo*\n\n"
        f"Not sure if the Macropad is right for you?\n\n"
        f"We offer a *free 1-on-1 live demo* — 30 minutes, no pressure, no sales pitch.\n\n"
        f"*In the demo you'll see:*\n"
        f"📊 The Macropad executing trades live on MT4/MT5\n"
        f"⚡ Real speed test — key press to order execution\n"
        f"🎨 How to remap keys to your own strategy\n"
        f"💡 Live data showing on the LCD keys\n"
        f"❓ Your questions answered in real time\n\n"
        f"*Duration:* 30 minutes\n"
        f"*Cost:* Completely free\n"
        f"*Format:* Video call (Zoom / Google Meet / Telegram)\n\n"
        f"👉 Book your slot here:\n{DEMO_LINK}"
    )
    keyboard = back_keyboard([
        [InlineKeyboardButton("🎬  Book My Free Demo", url=DEMO_LINK)],
        [InlineKeyboardButton("💰  Skip Demo — Pre-order Now", url=PREORDER_LINK)],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /faq ─────────────────────────────────────
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = f"❓ *Yalla Macropad — Frequently Asked Questions*\n\n"
    for i, (q, a) in enumerate(FAQS, 1):
        text += f"*{i}. {q}*\n{a}\n\n"
    keyboard = back_keyboard([
        [InlineKeyboardButton("💰  Pre-order — $590",    url=PREORDER_LINK)],
        [InlineKeyboardButton("🎬  Book Live Demo",      url=DEMO_LINK)],
        [InlineKeyboardButton("📞  More Questions",      callback_data="support")],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /support ─────────────────────────────────
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = (
        f"📞 *Yalla Pips — Support*\n\n"
        f"We're here to help with any questions about the Macropad.\n\n"
        f"💬 *Telegram:* `{SUPPORT_USERNAME}`\n"
        f"🌐 *Website:* {WEBSITE_URL}\n"
        f"📢 *Channel:* {CHANNEL_LINK}\n\n"
        f"*We can help with:*\n"
        f"• Questions before pre-ordering\n"
        f"• Compatibility with your platform\n"
        f"• Shipping and delivery questions\n"
        f"• Setup help after delivery\n"
        f"• Remapping keys to your strategy\n"
        f"• Any issues after purchase\n\n"
        f"*Response time:* Within a few hours\n\n"
        f"Or book a *free live demo* and we'll answer everything live:\n"
        f"👉 {DEMO_LINK}"
    )
    keyboard = back_keyboard([
        [InlineKeyboardButton("💬  Message Support",     url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}")],
        [InlineKeyboardButton("🎬  Book Live Demo",      url=DEMO_LINK)],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /compare ─────────────────────────────────
async def compare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = (
        f"⚖️ *Macropad vs Traditional Trading Setup*\n\n"
        f"*Without the Macropad:*\n"
        f"❌ Right-click → Trade → Modify → type lot size\n"
        f"❌ Forget to set break even mid-trade\n"
        f"❌ Miss partial close opportunity (took too long)\n"
        f"❌ Panic click wrong button under pressure\n"
        f"❌ 5–10 seconds per action minimum\n\n"
        f"*With the Yalla Macropad:*\n"
        f"✅ One tap → action done in <3ms\n"
        f"✅ Break even key always there — one tap\n"
        f"✅ Partial close at 25%, 50%, 75% — one tap each\n"
        f"✅ Never miss a move again\n"
        f"✅ Trade under pressure without mis-clicks\n\n"
        f"*The Macropad doesn't find trades for you.*\n"
        f"_It makes sure you execute them perfectly every time._\n\n"
        f"250 units. $590. One chance.\n"
        f"👉 {PREORDER_LINK}"
    )
    keyboard = back_keyboard([
        [InlineKeyboardButton("💰  Pre-order — $590",    url=PREORDER_LINK)],
        [InlineKeyboardButton("🎬  See It Live — Demo",  url=DEMO_LINK)],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /scarcity ────────────────────────────────
async def scarcity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows edition scarcity and urgency."""
    msg = update.message or update.callback_query.message
    text = (
        f"🔴 *Edition 01 — Why Only 250 Units?*\n\n"
        f"The Yalla Macropad Edition 01 is limited to *250 units worldwide.*\n\n"
        f"*Why limited?*\n"
        f"Each unit is hand-assembled with full-colour LCD keys. "
        f"This is a precision hardware product — not a mass-market keyboard.\n\n"
        f"*What happens after 250 units?*\n"
        f"❓ Edition 02 is not confirmed yet\n"
        f"❓ If it happens, price will be higher\n"
        f"❓ You may wait months for next batch\n\n"
        f"*Current status:*\n"
        f"🔴 Pre-orders are open\n"
        f"📦 Edition 01 — Limited units remaining\n\n"
        f"This is the only time you can get it at $590.\n\n"
        f"👉 Pre-order now: {PREORDER_LINK}"
    )
    keyboard = back_keyboard([
        [InlineKeyboardButton("🛒  Secure My Unit — $590", url=PREORDER_LINK)],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── /about ───────────────────────────────────
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    text = (
        f"ℹ️ *About Yalla Pips*\n\n"
        f"Yalla Pips builds professional trading tools — software and hardware — "
        f"for serious forex traders.\n\n"
        f"*Our Products:*\n"
        f"🤖 *Yalla Algo Bot* — Automated EA for MT4/MT5\n"
        f"📊 *Yalla Indicator* — Buy/sell signal indicator\n"
        f"⌨️ *Yalla Macropad* — 15-key LCD trading keyboard _(you're here)_\n\n"
        f"*Our Mission:*\n"
        f"Remove friction from trading execution. "
        f"Whether it's automation, signals, or hardware — "
        f"we build tools that let you trade at your best.\n\n"
        f"🌐 {WEBSITE_URL}\n"
        f"📢 {CHANNEL_LINK}"
    )
    keyboard = back_keyboard([
        [InlineKeyboardButton("🌐  Visit Website",       url=WEBSITE_URL)],
        [InlineKeyboardButton("📢  Join Channel",        url=CHANNEL_LINK)],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)


# ── Button handler ────────────────────────────
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    dispatch = {
        "menu":     lambda: query.message.reply_text(
                        "Choose an option:", reply_markup=main_menu_keyboard()),
        "what":     lambda: what(update, context),
        "features": lambda: features(update, context),
        "preorder": lambda: preorder(update, context),
        "demo":     lambda: demo(update, context),
        "faq":      lambda: faq(update, context),
        "support":  lambda: support(update, context),
        "compare":  lambda: compare(update, context),
        "scarcity": lambda: scarcity(update, context),
        "about":    lambda: about(update, context),
    }
    action = dispatch.get(query.data)
    if action:
        await action()


# ── Unknown messages ──────────────────────────
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are all available commands:\n\n"
        "/start — Main menu\n"
        "/what — What is the Macropad?\n"
        "/features — Full specs & features\n"
        "/preorder — Price & how to pre-order\n"
        "/demo — Book a free 30-min live demo\n"
        "/compare — Macropad vs traditional setup\n"
        "/faq — Frequently asked questions\n"
        "/support — Contact us\n"
        "/about — About Yalla Pips",
        reply_markup=main_menu_keyboard()
    )


# ─────────────────────────────────────────────
#   MAIN
# ─────────────────────────────────────────────

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",    start))
    app.add_handler(CommandHandler("what",     what))
    app.add_handler(CommandHandler("features", features))
    app.add_handler(CommandHandler("preorder", preorder))
    app.add_handler(CommandHandler("demo",     demo))
    app.add_handler(CommandHandler("faq",      faq))
    app.add_handler(CommandHandler("support",  support))
    app.add_handler(CommandHandler("compare",  compare))
    app.add_handler(CommandHandler("scarcity", scarcity))
    app.add_handler(CommandHandler("about",    about))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.ALL, unknown))

    print("✅ Yalla Macropad bot is running... Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
