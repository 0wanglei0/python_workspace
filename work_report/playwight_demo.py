from playwright.sync_api import sync_playwright

"""
在这个示例中，我们首先导入了Playwright的同步API，并使用sync_playwright()方法创建一个Playwright的同步实例。
然后，我们使用chromium.launch()方法创建一个浏览器实例，并使用new_context()方法创建一个浏览器上下文。
接着，我们使用new_page()方法创建一个新的页面对象。通过调用page.goto()方法，我们可以指定要访问的网页URL。
在本例中，我们访问了一个示例网站(https://www.example.com)。您可以将其替换为您想要访问的任何网页。
然后，我们使用page.screenshot()方法将当前页面截图并保存为一个图片文件。
您可以指定一个文件路径作为参数，例如path="example.png"，Playwright将自动创建并保存一个名为example.png的图片文件。
最后，我们使用browser.close()方法关闭浏览器实例。这个方法会等待所有正在进行的操作完成后再关闭浏览器。
"""
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.example.com")
    page.screenshot(path="example.png")
    browser.close()