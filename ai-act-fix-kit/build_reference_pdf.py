#!/usr/bin/env python3
"""
Converts writing-skus/ai-act-fix-kit-content.md into a real, on-brand PDF --
the "reference file" both Gumroad listings' description copy already
promises ("This listing also includes a reference file with the same
disclosure patterns and platform placement notes") but which, as of
2026-07-28, was never actually attached to either listing. Found while
answering Brandon's question about the single-tier-deliverable-file gap:
the real gap wasn't tier differentiation (the Content-tab pages are
already correctly per-tier and verified) -- it was an unfulfilled promise
in live copy. Same file attached to both tiers deliberately: the live
personalized on-page unlock (verified per-tier: 1 touchpoint vs 3) is the
actual paid differentiator; this PDF is bonus/backup reference material,
same for both, same as most SaaS help docs don't gate by pricing tier.
"""
import os
import re
from fpdf import FPDF
from fpdf.enums import XPos, YPos

_orig_multi_cell = FPDF.multi_cell


def _mc(self, w, h=None, txt="", *args, **kwargs):
    # Every multi_cell() call in this file is a full-width paragraph block
    # (w=0); fpdf2's own default leaves the cursor at the right margin
    # instead of resetting to the left, which corrupts every following
    # block. cell() (used for header/footer/table columns, which genuinely
    # need to stay on the same line) is left with its original default.
    kwargs.setdefault("new_x", XPos.LMARGIN)
    kwargs.setdefault("new_y", YPos.NEXT)
    return _orig_multi_cell(self, w, h, txt, *args, **kwargs)


FPDF.multi_cell = _mc

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets_lib", "fonts")
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "writing-skus", "ai-act-fix-kit-content.md")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "listing-art", "ai-act-fix-kit-reference.pdf")

INK = (30, 42, 42)
DIM = (100, 120, 118)
MINT = (16, 150, 110)
CARD = (240, 247, 245)


class RefPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Sans", "", 8)
        self.set_text_color(*DIM)
        self.cell(0, 8, "THE AI ACT FIX KIT -- REFERENCE", align="L")
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Sans", "", 8)
        self.set_text_color(*DIM)
        self.cell(0, 10, f"Click Coded -- clickcoded.com  |  Page {self.page_no()}", align="C")


def clean(s):
    s = s.replace("—", "-").replace("–", "-").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("→", "->").replace("×", "x")
    return s


def render_line(pdf, line):
    line = clean(line.rstrip())
    if not line.strip():
        pdf.ln(3)
        return
    if line.startswith("## "):
        pdf.ln(4)
        pdf.set_font("Serif", "B", 16)
        pdf.set_text_color(*INK)
        pdf.multi_cell(0, 8, line[3:])
        pdf.set_draw_color(*MINT)
        pdf.set_line_width(0.6)
        y = pdf.get_y() + 1
        pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
        pdf.ln(5)
        return
    if line.startswith("# "):
        pdf.set_font("Serif", "B", 22)
        pdf.set_text_color(*INK)
        pdf.multi_cell(0, 10, line[2:])
        pdf.ln(2)
        return
    if line.startswith("---"):
        pdf.ln(2)
        return
    if line.startswith("**") and line.endswith("**") and line.count("**") == 2:
        pdf.set_font("Sans", "B", 10.5)
        pdf.set_text_color(*INK)
        pdf.multi_cell(0, 6, line.strip("*"))
        pdf.ln(1)
        return
    if line.startswith("> "):
        pdf.set_font("Mono", "", 10)
        pdf.set_text_color(*MINT)
        pdf.set_fill_color(*CARD)
        pdf.multi_cell(0, 6.5, line[2:], fill=True)
        pdf.ln(2)
        return
    if line.startswith("- [ ] "):
        pdf.set_font("Sans", "", 10)
        pdf.set_text_color(*INK)
        pdf.multi_cell(0, 6, "  [ ]  " + strip_md(line[6:]))
        return
    if line.startswith("```"):
        return
    if line.startswith("    <") or line.startswith("<meta") or line.startswith("<!--"):
        pdf.set_font("Mono", "", 8.5)
        pdf.set_text_color(*DIM)
        pdf.multi_cell(0, 5, line)
        return
    if line.startswith("|"):
        return  # table rows handled separately
    if line.startswith("*") and line.endswith("*") and not line.startswith("**"):
        pdf.set_font("Sans", "I", 9.5)
        pdf.set_text_color(*DIM)
        pdf.multi_cell(0, 6, strip_md(line.strip("*")))
        pdf.ln(1)
        return
    pdf.set_font("Sans", "", 10.5)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 6.2, strip_md(line))
    pdf.ln(1)


def strip_md(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    s = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", s)
    return s


def render_table(pdf, rows):
    """Rendered as a definition list, not a grid -- a 4-column table with
    variable-height wrapped cells is fragile in fpdf2 (manual x/y tracking
    across cells + rows is easy to get subtly wrong, and it broke silently
    on the first attempt: rows overlapped and swallowed each other, and
    header-white text color leaked into data rows making them invisible).
    A flowing list has no multi-cell coordinate math to get wrong."""
    cols = [c.strip() for c in rows[0].strip("|").split("|")]
    data_rows = [r for r in rows[2:] if r.strip().startswith("|")]

    pdf.ln(2)
    for row in data_rows:
        cells = [clean(strip_md(c.strip())) for c in row.strip().strip("|").split("|")]
        situation, duty, where, article = (cells + ["", "", "", ""])[:4]

        pdf.set_font("Sans", "B", 10)
        pdf.set_text_color(*INK)
        pdf.multi_cell(0, 6, situation)

        pdf.set_font("Sans", "", 9.5)
        pdf.set_text_color(*DIM)
        detail = duty
        if where and where != "-":
            detail += f"  --  where: {where}"
        detail += f"   [{article}]"
        pdf.multi_cell(0, 5.5, detail)
        pdf.ln(2)
    pdf.ln(2)


def main():
    pdf = RefPDF(format="Letter")
    pdf.add_font("Serif", "", os.path.join(FONTS, "Fraunces-Regular.ttf"))
    pdf.add_font("Serif", "B", os.path.join(FONTS, "Fraunces-Bold.ttf"))
    pdf.add_font("Sans", "", os.path.join(FONTS, "Inter-Regular.ttf"))
    pdf.add_font("Sans", "B", os.path.join(FONTS, "Inter-SemiBold.ttf"))
    pdf.add_font("Sans", "I", os.path.join(FONTS, "Inter-Regular.ttf"))
    pdf.add_font("Mono", "", os.path.join(FONTS, "IBMPlexMono-Regular.ttf"))
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(20, 20, 20)
    pdf.add_page()

    pdf.set_font("Mono", "", 9)
    pdf.set_text_color(*MINT)
    pdf.cell(0, 6, "CLICK CODED")
    pdf.ln(10)
    pdf.set_font("Serif", "B", 26)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 12, "The AI Act Fix Kit")
    pdf.set_font("Serif", "B", 14)
    pdf.set_text_color(*MINT)
    pdf.multi_cell(0, 8, "Reference: EU AI Act Article 50 Disclosure Patterns")
    pdf.ln(4)
    pdf.set_font("Sans", "", 10)
    pdf.set_text_color(*DIM)
    pdf.multi_cell(0, 6, "2026 Edition. Your personalized disclosure text lives live on clickcoded.com, "
                         "written with your business name -- this file is the backup reference: every "
                         "pattern, every citation, every placement note, in one place.")
    pdf.ln(8)

    with open(SRC, encoding="utf-8") as f:
        lines = f.read().split("\n")

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|---"):
            j = i
            table_lines = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                table_lines.append(lines[j])
                j += 1
            render_table(pdf, table_lines)
            i = j
            continue
        render_line(pdf, line)
        i += 1

    pdf.output(OUT)
    print(f"saved {OUT}")


if __name__ == "__main__":
    main()
