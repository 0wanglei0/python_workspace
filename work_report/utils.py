def use_js_change_value(_browser, element_id, value):
    js = f"""
        element = document.getElementById("{element_id}")
        element.value = '{value}'
    """
    #
    # print(js)
    # print(value)
    _browser.execute_script(js)