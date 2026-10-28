import sys, os, glob
from playwright.sync_api import sync_playwright
def render(html_path, out_dir, prefix):
    os.makedirs(out_dir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width":1200,"height":1500}, device_scale_factor=1)
        pg.goto("file://"+os.path.abspath(html_path)); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(500)
        for i, el in enumerate(pg.query_selector_all("section.slide"), 1):
            el.screenshot(path=os.path.join(out_dir, "%s_%02d.png" % (prefix, i)))
        b.close()
if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], sys.argv[3])
