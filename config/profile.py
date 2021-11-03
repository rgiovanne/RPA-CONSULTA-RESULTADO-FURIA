# coding=utf-8

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def perfil(visivel, directory):
    option = Options()
    option.headless = visivel
    fp = webdriver.FirefoxProfile()
    fp.set_preference('browser.download.folderList', 2)
    fp.set_preference('browser.download.manager.showWhenStarting', False)
    fp.set_preference('browser.download.dir', directory)
    fp.set_preference("browser.cache.disk.enable", False)
    fp.set_preference("browser.cache.memory.enable", False)
    fp.set_preference("browser.cache.offline.enable", False)
    fp.set_preference("network.http.use-cache", False)
    fp.set_preference("browser.download.useDownloadDir", True)
    fp.set_preference("browser.download.viewableInternally.enabledTypes", "")
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                      "application/octet-stream;application/pdf;text/plain;application/text;text/xml;application/xml")
    fp.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(firefox_profile=fp, options=option)

    return driver
