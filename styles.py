"""Styling constants for the digital twin Gradio app."""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

:root {
  --twin-gold: #ecad0a;
  --twin-blue: #3ec3ff;
  --twin-blue-deep: #1a8fd4;
  --twin-purple: #b07cff;
  --twin-bg: #07070c;
  --twin-surface: rgba(18, 18, 28, 0.82);
  --twin-surface-2: #1d1b2b;
  --twin-border: rgba(255, 255, 255, 0.08);
  --twin-border-strong: rgba(255, 255, 255, 0.16);
  --twin-text: #f4f4f8;
  --twin-muted: #9a97ab;
  --twin-user: linear-gradient(135deg, #3ec3ff 0%, #6a7dff 100%);
}

body:not(.dark) {
  --twin-bg: #eef1f7;
  --twin-surface: rgba(255, 255, 255, 0.86);
  --twin-surface-2: #f3f0fa;
  --twin-border: rgba(20, 16, 40, 0.08);
  --twin-border-strong: rgba(20, 16, 40, 0.14);
  --twin-text: #16141f;
  --twin-muted: #6b6680;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app {
  background:
    radial-gradient(1200px 700px at 12% -10%, rgba(176, 124, 255, 0.22), transparent 55%),
    radial-gradient(900px 600px at 110% 10%, rgba(62, 195, 255, 0.18), transparent 50%),
    radial-gradient(800px 500px at 50% 120%, rgba(236, 173, 10, 0.08), transparent 45%),
    var(--twin-bg) !important;
  min-height: 100%;
}

.gradio-container {
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 760px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 28px 18px 40px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

.gradio-container h1 {
  font-family: 'Outfit', sans-serif !important;
  color: var(--twin-text) !important;
  font-size: 30px !important;
  font-weight: 700 !important;
  letter-spacing: -0.04em !important;
  margin: 0 0 6px !important;
  text-align: left !important;
  border: 0 !important;
  padding: 0 !important;
}
.gradio-container h1::after {
  content: '';
  display: inline-block;
  width: 8px;
  height: 8px;
  margin-left: 10px;
  margin-bottom: 3px;
  border-radius: 50%;
  background: #3ee08f;
  box-shadow: 0 0 0 4px rgba(62, 224, 143, 0.18);
}
.gradio-container .prose,
.gradio-container p {
  color: var(--twin-muted) !important;
}

.block, .form { background: transparent !important; box-shadow: none !important; }

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 28px !important;
  min-height: 58vh !important;
  box-shadow:
    0 20px 60px rgba(0, 0, 0, 0.28),
    inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
  backdrop-filter: blur(18px);
  overflow: hidden !important;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.message-row.user-row,
.message-row[data-role="user"] {
  justify-content: flex-end !important;
}
.message-row.bot-row,
.message-row[data-role="assistant"] {
  justify-content: flex-start !important;
}

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  padding: 12px 16px !important;
  max-width: min(78%, 520px) !important;
  font-size: 15px !important;
  line-height: 1.55 !important;
}

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-user) !important;
  color: #071018 !important;
  border-radius: 20px 20px 6px 20px !important;
  box-shadow: 0 8px 24px rgba(62, 195, 255, 0.22) !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  border-radius: 20px 20px 20px 6px !important;
  border: 1px solid var(--twin-border) !important;
}

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 15px !important;
  line-height: 1.55 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: underline;
}

.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; }

textarea, input[type="text"] {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border-strong) !important;
  border-radius: 999px !important;
  color: var(--twin-text) !important;
  font-family: 'IBM Plex Sans', sans-serif !important;
  font-size: 15px !important;
  padding: 14px 20px !important;
  line-height: 1.4 !important;
  min-height: 52px !important;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.18) !important;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-purple) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(176, 124, 255, 0.22) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

button {
  font-family: 'Outfit', sans-serif !important;
  letter-spacing: 0.02em !important;
  text-transform: none !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  border: 1px solid transparent !important;
  background: transparent !important;
  color: var(--twin-text) !important;
  padding: 0 16px !important;
  min-height: 52px !important;
  border-radius: 999px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: transform 0.12s ease, filter 0.12s ease, box-shadow 0.12s ease;
}
button:hover { filter: brightness(1.08); }

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-user) !important;
  border: 0 !important;
  color: #071018 !important;
  min-width: 52px !important;
  box-shadow: 0 8px 22px rgba(62, 195, 255, 0.28) !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  transform: translateY(-1px);
}

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  color: #071018 !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 16px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 999px !important;
  color: var(--twin-text) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'IBM Plex Sans', sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  padding: 10px 16px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
  backdrop-filter: blur(12px);
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;
  color: var(--twin-blue) !important;
  box-shadow: 0 0 0 3px rgba(62, 195, 255, 0.12) !important;
}

.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 4px !important;
  border-radius: 999px !important;
}
.icon-button:hover, .chatbot .icon-button:hover { color: var(--twin-gold) !important; }

::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--twin-border-strong); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); }

::selection { background: var(--twin-purple); color: #fff; }

@media (max-width: 640px) {
  .gradio-container { padding: 18px 12px 28px !important; }
  .gradio-container h1 { font-size: 24px !important; }
  .chatbot, .chatbot.block { min-height: 52vh !important; border-radius: 22px !important; }
  .message-row .message,
  .message-row .message-bubble,
  .message-row .bubble { max-width: 88% !important; }
}
"""

JS = """
() => {
  document.title = 'Guigão · Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
