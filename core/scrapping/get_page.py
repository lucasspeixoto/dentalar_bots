# -*- coding: utf-8 -*-
# encoding: utf-8

"""
    :Args:
        
    :Returns:
"""


def get_page(self, page_url: str):

    try:
        self.driver.get(page_url)
        pass
    except Exception as error:
        print(f"Error Inside get_page function: {error}")
        return
    finally:
        self.uniform_wait(3, 4)

    return
