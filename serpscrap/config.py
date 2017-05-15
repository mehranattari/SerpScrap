#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
SerpScrap.Config
"""


class Config():
    """
    Config
    This modul is used to hold and handle the required configuration settings

    Attributes:
        config: dict of configuration keys and values
        apply (dict): method to set a new configuration
        get (): return the current configuration
        set (string, mixed): set an new value for an existing config key
    """

    config = {
        'use_own_ip': True,
        'search_engines': ['google'],
        'num_pages_for_keyword': 2,
        'scrape_method': 'selenium',
        'sel_browser': 'phantomjs',
        'executable_path': '',
        'do_caching': True,
        'cachedir': '/tmp/.serpscrap/',
        'dir_screenshot': '/tmp/screenshots/',
        'database_name': '/tmp/serpscrap',
        'minimize_caching_files': True,
        'clean_cache_after': 24,
        'output_filename': None,
        # 'print_results': 'all',
        'scrape_urls': True,
        'url_threads': 6,
        'log_level': 'INFO',
        'num_workers': 1,
        'num_results_per_page': 10,
        'sleeping_min': 5,
        'sleeping_max': 15,
        'search_type': 'normal',
        'google_search_url': 'https://www.google.com/search?',
        'bing_search_url': 'http://www.bing.com/search?',
        'headers': {
            'Accept': '*/*',
            'Accept-Language': 'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.de/'
        },
        'proxy_file': '',
        'proxy_check_url': 'http://canihazip.com/s',
        'proxy_info_url': 'http://ipinfo.io/json',
        'stop_on_detection': True,
    }

    def get(self):
        """get the config dictionary

        Returns:
            dict: the ccurrent config
        """

        return self.config

    def set(self, key, value):
        """set or update a value of a config key

        Args:
            key (string): the config key
            value (int|string|None): the config key value
        """

        self.config.__setitem__(key, value)

    def apply(self, config):
        """apply an individual conig

        Args:
            config (dict): new configuration
        """

        self.config = config
