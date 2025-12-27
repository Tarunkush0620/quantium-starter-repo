# Ensure ChromeDriver is available for Selenium via auto-installer
try:
    import chromedriver_autoinstaller as cda
    cda.install()
except Exception as e:
    # Tests will surface a clearer error if webdriver is missing
    print("Warning: chromedriver auto-install failed:", e)
