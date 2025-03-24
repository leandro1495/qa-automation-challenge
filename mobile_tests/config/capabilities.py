from typing import Any, Dict


def get_capabilities() -> Dict[str, Any]:
    return {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": "com.google.android.dialer",
        "appActivity": "com.android.dialer.main.impl.MainActivity",
        "language": "en"
    }
